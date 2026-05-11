import os

from flask import (
    render_template,
    request,
    redirect,
    url_for,
    flash,
    session
)

from werkzeug.utils import secure_filename

from app.admin import admin

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from app.models.user import User
from app.models.category import Category
from app.models.product import Product
from app.models.order import Order

from app import db



# =========================================
# ADMIN REGISTER
# =========================================
@admin.route('/admin/register', methods=['GET', 'POST'])
def admin_register():

    if 'admin_id' in session:

        return redirect(
            url_for('admin_dashboard')
        )

    if request.method == 'POST':

        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        # VALIDATION
        if not username or not email or not password:

            flash(
                'All fields are required',
                'warning'
            )

            return redirect(
                url_for('admin_register')
            )

        # CHECK EMAIL
        existing_user = User.query.filter_by(
            email=email
        ).first()

        if existing_user:

            flash(
                'Email already exists',
                'warning'
            )

            return redirect(
                url_for('admin_register')
            )

        # HASH PASSWORD
        hashed_password = generate_password_hash(
            password
        )

        try:

            user = User(
                username=username,
                email=email,
                password=hashed_password,
                is_admin=True
            )

            db.session.add(user)

            db.session.commit()

            flash(
                'Registration Successful',
                'success'
            )

            return redirect(
                url_for('admin_login')
            )

        except Exception as e:

            db.session.rollback()

            flash(
                f'Error: {e}',
                'danger'
            )

            return redirect(
                url_for('admin_register')
            )

    return render_template(
        'admin/register.html'
    )


# =========================================
# ADMIN LOGIN
# =========================================
@admin.route('/admin/login', methods=['GET', 'POST'])
def admin_login():

    if 'admin_id' in session:

        return redirect(
            url_for('admin_dashboard')
        )

    if request.method == 'POST':

        email = request.form.get('email')
        password = request.form.get('password')

        # VALIDATION
        if not email or not password:

            flash(
                'All fields are required',
                'warning'
            )

            return redirect(
                url_for('admin_login')
            )

        # FIND USER
        user = User.query.filter_by(
            email=email
        ).first()

        # CHECK PASSWORD
        if user and check_password_hash(
            user.password,
            password
        ):

            session['admin_id'] = user.id
            session['admin_name'] = user.username

            flash(
                'Login Successful',
                'success'
            )

            return redirect(
                url_for('admin_dashboard')
            )

        flash(
            'Invalid Email or Password',
            'danger'
        )

        return redirect(
            url_for('admin_login')
        )

    return render_template(
        'admin/login.html'
    )


# =========================================
# ADMIN DASHBOARD
# =========================================
@admin.route('/admin/dashboard')
def admin_dashboard():

    if 'admin_id' not in session:

        flash(
            'Please login first',
            'warning'
        )

        return redirect(
            url_for('admin_login')
        )

    return render_template(
        'admin/dashboard.html'
    )


# =========================================
# CATEGORY LIST + ADD
# =========================================
@admin.route('/admin/categories', methods=['GET', 'POST'])
def categories():

    if 'admin_id' not in session:

        flash(
            'Please login first',
            'warning'
        )

        return redirect(
            url_for('admin_login')
        )

    # ADD CATEGORY
    if request.method == 'POST':

        name = request.form.get('name')

        description = request.form.get(
            'description'
        )

        # VALIDATION
        if not name:

            flash(
                'Category name required',
                'warning'
            )

            return redirect(
                url_for('categories')
            )

        # CHECK DUPLICATE
        existing_category = Category.query.filter_by(
            name=name
        ).first()

        if existing_category:

            flash(
                'Category already exists',
                'warning'
            )

            return redirect(
                url_for('categories')
            )

        try:

            category = Category(
                name=name,
                description=description
            )

            db.session.add(category)

            db.session.commit()

            flash(
                'Category Added Successfully',
                'success'
            )

            return redirect(
                url_for('categories')
            )

        except Exception as e:

            db.session.rollback()

            flash(
                f'Error: {e}',
                'danger'
            )

            return redirect(
                url_for('categories')
            )

    # SHOW CATEGORY
    all_categories = Category.query.all()

    return render_template(
        'admin/categories.html',
        categories=all_categories
    )


# =========================================
# EDIT CATEGORY
# =========================================
@admin.route(
    '/admin/category/edit/<int:id>',
    methods=['GET', 'POST']
)
def edit_category(id):

    if 'admin_id' not in session:

        flash(
            'Please login first',
            'warning'
        )

        return redirect(
            url_for('admin_login')
        )

    category = Category.query.get_or_404(id)

    if request.method == 'POST':

        name = request.form.get('name')

        description = request.form.get(
            'description'
        )

        # VALIDATION
        if not name:

            flash(
                'Category name required',
                'warning'
            )

            return redirect(
                url_for(
                    'edit_category',
                    id=id
                )
            )

        try:

            category.name = name

            category.description = description

            db.session.commit()

            flash(
                'Category Updated Successfully',
                'success'
            )

            return redirect(
                url_for('categories')
            )

        except Exception as e:

            db.session.rollback()

            flash(
                f'Error: {e}',
                'danger'
            )

            return redirect(
                url_for(
                    'edit_category',
                    id=id
                )
            )

    return render_template(
        'admin/edit_category.html',
        category=category
    )


# =========================================
# DELETE CATEGORY
# =========================================
@admin.route('/admin/category/delete/<int:id>')
def delete_category(id):

    if 'admin_id' not in session:

        flash(
            'Please login first',
            'warning'
        )

        return redirect(
            url_for('admin_login')
        )

    category = Category.query.get_or_404(id)

    try:

        db.session.delete(category)

        db.session.commit()

        flash(
            'Category Deleted Successfully',
            'danger'
        )

    except Exception as e:

        db.session.rollback()

        flash(
            f'Error: {e}',
            'danger'
        )

    return redirect(
        url_for('categories')
    )


# =========================================
# PRODUCT LIST + ADD
# =========================================
@admin.route(
    '/admin/products',
    methods=['GET', 'POST']
)
def products():

    if 'admin_id' not in session:

        flash(
            'Please login first',
            'warning'
        )

        return redirect(
            url_for('admin_login')
        )

    all_categories = Category.query.all()

    # ADD PRODUCT
    if request.method == 'POST':

        name = request.form.get('name')

        price = request.form.get('price')

        description = request.form.get(
            'description'
        )

        stock = request.form.get('stock')

        category_id = request.form.get(
            'category_id'
        )

        image = request.files.get('image')

        filename = None

        # IMAGE UPLOAD
        if image and image.filename != '':

            filename = secure_filename(
                image.filename
            )

            image_path = os.path.join(
                app.config['UPLOAD_FOLDER'],
                filename
            )

            image.save(image_path)

        try:

            product = Product(
                name=name,
                price=price,
                description=description,
                stock=stock,
                image=filename,
                category_id=category_id
            )

            db.session.add(product)

            db.session.commit()

            flash(
                'Product Added Successfully',
                'success'
            )

            return redirect(
                url_for('products')
            )

        except Exception as e:

            db.session.rollback()

            flash(
                f'Error: {e}',
                'danger'
            )

            return redirect(
                url_for('products')
            )

    # SHOW PRODUCTS
    all_products = Product.query.all()

    return render_template(
        'admin/products.html',
        products=all_products,
        categories=all_categories
    )


# =========================================
# EDIT PRODUCT
# =========================================
@admin.route(
    '/admin/product/edit/<int:id>',
    methods=['GET', 'POST']
)
def edit_product(id):

    if 'admin_id' not in session:

        return redirect(
            url_for('admin_login')
        )

    product = Product.query.get_or_404(id)

    categories = Category.query.all()

    if request.method == 'POST':

        product.name = request.form.get('name')

        product.price = request.form.get(
            'price'
        )

        product.description = request.form.get(
            'description'
        )

        product.stock = request.form.get(
            'stock'
        )

        product.category_id = request.form.get(
            'category_id'
        )

        image = request.files.get('image')

        # NEW IMAGE
        if image and image.filename != '':

            filename = secure_filename(
                image.filename
            )

            image_path = os.path.join(
                app.config['UPLOAD_FOLDER'],
                filename
            )

            image.save(image_path)

            product.image = filename

        try:

            db.session.commit()

            flash(
                'Product Updated Successfully',
                'success'
            )

            return redirect(
                url_for('products')
            )

        except Exception as e:

            db.session.rollback()

            flash(
                f'Error: {e}',
                'danger'
            )

    return render_template(
        'admin/edit_product.html',
        product=product,
        categories=categories
    )


# =========================================
# DELETE PRODUCT
# =========================================
@admin.route('/admin/product/delete/<int:id>')
def delete_product(id):

    if 'admin_id' not in session:

        return redirect(
            url_for('admin_login')
        )

    product = Product.query.get_or_404(id)

    try:

        # DELETE IMAGE
        if product.image:

            image_path = os.path.join(
                app.config['UPLOAD_FOLDER'],
                product.image
            )

            if os.path.exists(image_path):

                os.remove(image_path)

        db.session.delete(product)

        db.session.commit()

        flash(
            'Product Deleted Successfully',
            'danger'
        )

    except Exception as e:

        db.session.rollback()

        flash(
            f'Error: {e}',
            'danger'
        )

    return redirect(
        url_for('products')
    )

# =========================================
# ALL ORDERS
# =========================================
@admin.route('/admin/orders')
def admin_orders():

    # LOGIN CHECK
    if 'admin_id' not in session:

        return redirect(
            url_for('admin_login')
        )

    orders = Order.query.order_by(
        Order.id.desc()
    ).all()

    return render_template(
        'admin/orders/index.html',
        orders=orders
    )


# =========================================
# ORDER DETAILS
# =========================================
@admin.route('/admin/order/<int:id>')
def admin_order_details(id):

    # LOGIN CHECK
    if 'admin_id' not in session:

        return redirect(
            url_for('admin_login')
        )

    order = Order.query.get_or_404(id)

    return render_template(
        'admin/orders/details.html',
        order=order
    )


# =========================================
# UPDATE ORDER STATUS
# =========================================
@admin.route(
    '/admin/order/status/<int:id>',
    methods=['POST']
)
def update_order_status(id):

    # LOGIN CHECK
    if 'admin_id' not in session:

        return redirect(
            url_for('admin_login')
        )

    order = Order.query.get_or_404(id)

    status = request.form.get(
        'status'
    )

    order.status = status

    db.session.commit()

    flash(
        'Order Status Updated',
        'success'
    )

    return redirect(
        url_for(
            'admin_order_details',
            id=order.id
        )
    )
# =========================================
# ADMIN LOGOUT
# =========================================
@admin.route('/admin/logout')
def admin_logout():

        session.clear()

        flash(
            'Logout Successful',
            'success'
        )

        return redirect(
            url_for('admin_login')
        )