from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    session
)

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from werkzeug.utils import secure_filename

from app import db

from app.models.user import User
from app.models.category import Category
from app.models.product import Product
from app.models.order import Order

import os
import uuid


# =========================================
# ADMIN BLUEPRINT
# =========================================
admin = Blueprint(
    'admin',
    __name__,
    url_prefix='/admin'
)


# =========================================
# ADMIN LOGIN REQUIRED
# =========================================
def admin_login_required():

    if 'admin_id' not in session:
        return False

    return True


# =========================================
# SUPER ADMIN REQUIRED
# =========================================
def super_admin_required():

    if session.get('admin_role') != 'super_admin':

        flash(
            'Only Super Admin Can Access',
            'danger'
        )

        return False

    return True


# =========================================
# ADMIN REGISTER
# =========================================
@admin.route('/register', methods=['GET', 'POST'])
def admin_register():

    if request.method == 'POST':

        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        role = request.form.get('role')

        # CHECK EMAIL EXISTS
        old_user = User.query.filter_by(
            email=email
        ).first()

        if old_user:

            flash(
                'Email Already Exists',
                'danger'
            )

            return redirect(
                url_for('admin.admin_register')
            )

        # HASH PASSWORD
        hashed_password = generate_password_hash(
            password
        )

        # CREATE USER
        user = User(
            username=username,
            email=email,
            password=hashed_password,
            role=role
        )

        db.session.add(user)
        db.session.commit()

        flash(
            'Admin Registration Successful',
            'success'
        )

        return redirect(
            url_for('admin.admin_login')
        )

    return render_template(
        'admin/register.html'
    )


# =========================================
# ADMIN LOGIN
# =========================================
@admin.route('/login', methods=['GET', 'POST'])
def admin_login():

    if request.method == 'POST':

        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(
            email=email
        ).first()

        if not user:

            flash(
                'Invalid Email',
                'danger'
            )

            return redirect(
                url_for('admin.admin_login')
            )

        if not check_password_hash(
            user.password,
            password
        ):

            flash(
                'Invalid Password',
                'danger'
            )

            return redirect(
                url_for('admin.admin_login')
            )

        # STORE SESSION
        session['admin_id'] = user.id
        session['admin_name'] = user.username
        session['admin_role'] = user.role

        flash(
            'Login Successful',
            'success'
        )

        return redirect(
            url_for('admin.admin_dashboard')
        )

    return render_template(
        'admin/login.html'
    )


# =========================================
# ADMIN DASHBOARD
# =========================================
@admin.route('/dashboard')
def admin_dashboard():

    if not admin_login_required():

        return redirect(
            url_for('admin.admin_login')
        )

    total_categories = Category.query.count()

    total_products = Product.query.count()

    total_orders = Order.query.count()

    total_users = User.query.count()

    return render_template(
        'admin/dashboard.html',
        total_categories=total_categories,
        total_products=total_products,
        total_orders=total_orders,
        total_users=total_users
    )


# =========================================
# CATEGORY LIST
# =========================================
@admin.route('/categories')
def categories():

    if not admin_login_required():

        return redirect(
            url_for('admin.admin_login')
        )

    categories = Category.query.order_by(
        Category.id.desc()
    ).all()

    return render_template(
        'admin/categories/index.html',
        categories=categories
    )


# =========================================
# CREATE CATEGORY
# =========================================
@admin.route('/categories/create', methods=['GET', 'POST'])
def create_category():

    if not admin_login_required():

        return redirect(
            url_for('admin.admin_login')
        )

    if request.method == 'POST':

        name = request.form.get('name')

        category = Category(
            name=name
        )

        db.session.add(category)
        db.session.commit()

        flash(
            'Category Created Successfully',
            'success'
        )

        return redirect(
            url_for('admin.categories')
        )

    return render_template(
        'admin/categories/create.html'
    )


# =========================================
# EDIT CATEGORY
# =========================================
@admin.route('/categories/edit/<int:id>', methods=['GET', 'POST'])
def edit_category(id):

    if not admin_login_required():

        return redirect(
            url_for('admin.admin_login')
        )

    category = Category.query.get_or_404(id)

    if request.method == 'POST':

        category.name = request.form.get('name')

        db.session.commit()

        flash(
            'Category Updated Successfully',
            'success'
        )

        return redirect(
            url_for('admin.categories')
        )

    return render_template(
        'admin/categories/edit.html',
        category=category
    )


# =========================================
# DELETE CATEGORY
# =========================================
@admin.route('/categories/delete/<int:id>')
def delete_category(id):

    if not admin_login_required():

        return redirect(
            url_for('admin.admin_login')
        )

    category = Category.query.get_or_404(id)

    db.session.delete(category)
    db.session.commit()

    flash(
        'Category Deleted Successfully',
        'success'
    )

    return redirect(
        url_for('admin.categories')
    )


# =========================================
# PRODUCT LIST
# =========================================
@admin.route('/products')
def products():

    if not admin_login_required():

        return redirect(
            url_for('admin.admin_login')
        )

    products = Product.query.order_by(
        Product.id.desc()
    ).all()

    return render_template(
        'admin/products/index.html',
        products=products
    )


# =========================================
# CREATE PRODUCT
# =========================================
@admin.route('/products/create', methods=['GET', 'POST'])
def create_product():

    if not admin_login_required():

        return redirect(
            url_for('admin.admin_login')
        )

    categories = Category.query.all()

    if request.method == 'POST':

        name = request.form.get('name')

        price = request.form.get('price')

        stock = request.form.get('stock')

        description = request.form.get('description')

        category_id = request.form.get('category_id')

        image = request.files.get('image')

        filename = None

        # IMAGE UPLOAD
        if image and image.filename != '':

            ext = image.filename.split('.')[-1]

            filename = (
                str(uuid.uuid4()) +
                '.' +
                ext
            )

            image_path = os.path.join(
                'app/static/images',
                filename
            )

            image.save(image_path)

        product = Product(
            name=name,
            price=price,
            stock=stock,
            description=description,
            category_id=category_id,
            image=filename
        )

        db.session.add(product)
        db.session.commit()

        flash(
            'Product Created Successfully',
            'success'
        )

        return redirect(
            url_for('admin.products')
        )

    return render_template(
        'admin/products/create.html',
        categories=categories
    )