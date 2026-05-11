from flask import (
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash
)

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from app.web import web

from app import db

from app.models.product import Product
from app.models.category import Category
from app.models.customer import Customer
from app.models.order import Order
from app.models.order_item import OrderItem




# =========================================
# HOME PAGE
# =========================================
@web.route('/')
def home():

    products = Product.query.all()

    categories = Category.query.all()

    return render_template(
        'web/index.html',
        products=products,
        categories=categories
    )


# =========================================
# PRODUCT DETAILS
# =========================================
@web.route('/product/<int:id>')
def product_details(id):

    product = Product.query.get_or_404(id)

    categories = Category.query.all()

    # GST
    gst = round(
        (product.price * 18) / 100,
        2
    )

    # FINAL PRICE
    final_price = round(
        product.price + gst,
        2
    )

    return render_template(
        'web/product_details.html',
        product=product,
        categories=categories,
        gst=gst,
        final_price=final_price
    )


# =========================================
# CATEGORY PRODUCTS
# =========================================
@web.route('/category/<int:id>')
def category_products(id):

    category = Category.query.get_or_404(id)

    products = Product.query.filter_by(
        category_id=id
    ).all()

    categories = Category.query.all()

    return render_template(
        'web/category_products.html',
        category=category,
        products=products,
        categories=categories
    )


# =========================================
# SEARCH PRODUCTS
# =========================================
@web.route('/search')
def search():

    keyword = request.args.get('keyword')

    products = Product.query.filter(
        Product.name.ilike(
            f'%{keyword}%'
        )
    ).all()

    categories = Category.query.all()

    return render_template(
        'web/search.html',
        products=products,
        keyword=keyword,
        categories=categories
    )


# =========================================
# CUSTOMER REGISTER
# =========================================
@web.route(
    '/register',
    methods=['GET', 'POST']
)
def register():

    # ALREADY LOGIN
    if 'customer_id' in session:

        return redirect(
            url_for('home')
        )

    if request.method == 'POST':

        name = request.form.get('name')

        email = request.form.get('email')

        password = request.form.get(
            'password'
        )

        # CHECK EMAIL EXISTS
        existing_user = Customer.query.filter_by(
            email=email
        ).first()

        if existing_user:

            flash(
                'Email already exists',
                'danger'
            )

            return redirect(
                url_for('register')
            )

        # HASH PASSWORD
        hashed_password = (
            generate_password_hash(
                password
            )
        )

        customer = Customer(
            name=name,
            email=email,
            password=hashed_password
        )

        db.session.add(customer)

        db.session.commit()

        flash(
            'Registration Successful',
            'success'
        )

        return redirect(
            url_for('login')
        )

    return render_template(
        'web/register.html',
        categories=Category.query.all()
    )


# =========================================
# CUSTOMER LOGIN
# =========================================
@web.route(
    '/login',
    methods=['GET', 'POST']
)
def login():

    # ALREADY LOGIN
    if 'customer_id' in session:

        return redirect(
            url_for('home')
        )

    if request.method == 'POST':

        email = request.form.get('email')

        password = request.form.get(
            'password'
        )

        customer = Customer.query.filter_by(
            email=email
        ).first()

        if customer and check_password_hash(
            customer.password,
            password
        ):

            # STORE SESSION
            session['customer_id'] = (
                customer.id
            )

            session['customer_name'] = (
                customer.name
            )

            flash(
                'Login Successful',
                'success'
            )

            return redirect(
                url_for('home')
            )

        flash(
            'Invalid Email or Password',
            'danger'
        )

    return render_template(
        'web/login.html',
        categories=Category.query.all()
    )


# =========================================
# CUSTOMER LOGOUT
# =========================================
@web.route('/logout')
def logout():

    session.pop(
        'customer_id',
        None
    )

    session.pop(
        'customer_name',
        None
    )

    flash(
        'Logout Successful',
        'success'
    )

    return redirect(
        url_for('home')
    )


# =========================================
# ADD TO CART
# =========================================
@web.route('/add-to-cart/<int:id>')
def add_to_cart(id):

    product = Product.query.get_or_404(id)

    # CREATE CART SESSION
    if 'cart' not in session:

        session['cart'] = {}

    cart = session['cart']

    product_id = str(product.id)

    # PRODUCT EXISTS
    if product_id in cart:

        cart[product_id]['quantity'] += 1

    else:

        cart[product_id] = {

            'name': product.name,

            'price': float(product.price),

            'quantity': 1,

            'image': product.image
        }

    session['cart'] = cart

    flash(
        'Product added to cart',
        'success'
    )

    return redirect(
        url_for('cart')
    )


# =========================================
# CART PAGE
# =========================================
@web.route('/cart')
def cart():

    cart_items = session.get(
        'cart',
        {}
    )

    subtotal = 0

    # SUBTOTAL
    for item in cart_items.values():

        subtotal += (
            item['price'] *
            item['quantity']
        )

    # GST
    gst = round(
        (subtotal * 18) / 100,
        2
    )

    # FINAL TOTAL
    final_total = round(
        subtotal + gst,
        2
    )

    return render_template(
        'web/cart.html',
        cart_items=cart_items,
        subtotal=subtotal,
        gst=gst,
        final_total=final_total,
        categories=Category.query.all()
    )


# =========================================
# UPDATE CART
# =========================================
@web.route('/update-cart/<product_id>')
def update_cart(product_id):

    action = request.args.get(
        'action'
    )

    cart = session.get(
        'cart',
        {}
    )

    if product_id in cart:

        if action == 'increase':

            cart[product_id]['quantity'] += 1

        elif action == 'decrease':

            if cart[product_id]['quantity'] > 1:

                cart[product_id]['quantity'] -= 1

    session['cart'] = cart

    return redirect(
        url_for('cart')
    )


# =========================================
# REMOVE CART ITEM
# =========================================
@web.route('/remove-cart/<product_id>')
def remove_cart(product_id):

    cart = session.get(
        'cart',
        {}
    )

    if product_id in cart:

        cart.pop(product_id)

    session['cart'] = cart

    flash(
        'Item removed from cart',
        'danger'
    )

    return redirect(
        url_for('cart')
    )


# =========================================
# CHECKOUT
# =========================================
@web.route(
    '/checkout',
    methods=['GET', 'POST']
)
def checkout():

    # LOGIN CHECK
    if 'customer_id' not in session:

        flash(
            'Please login first',
            'warning'
        )

        return redirect(
            url_for('login')
        )

    cart_items = session.get(
        'cart',
        {}
    )

    if not cart_items:

        flash(
            'Cart is empty',
            'warning'
        )

        return redirect(
            url_for('home')
        )

    subtotal = 0

    for item in cart_items.values():

        subtotal += (
            item['price'] *
            item['quantity']
        )

    # GST
    gst = round(
        (subtotal * 18) / 100,
        2
    )

    # FINAL TOTAL
    final_total = round(
        subtotal + gst,
        2
    )

    if request.method == 'POST':

        address = request.form.get(
            'address'
        )

        # CREATE ORDER
        order = Order(
            customer_id=session[
                'customer_id'
            ],
            total_amount=final_total,
            address=address
        )

        db.session.add(order)

        db.session.commit()

        # SAVE ORDER ITEMS
        for item in cart_items.values():

            order_item = OrderItem(

                order_id=order.id,

                product_name=item['name'],

                product_price=item['price'],

                quantity=item['quantity'],

                subtotal=(
                    item['price'] *
                    item['quantity']
                )
            )

            db.session.add(order_item)

        db.session.commit()

        # CLEAR CART
        session.pop('cart', None)

        flash(
            'Order Placed Successfully',
            'success'
        )

        return redirect(
            url_for('home')
        )

    return render_template(
        'web/checkout.html',
        cart_items=cart_items,
        subtotal=subtotal,
        gst=gst,
        final_total=final_total,
        categories=Category.query.all()
    )


# =========================================
# MY ORDERS
# =========================================
@web.route('/my-orders')
def my_orders():

    # LOGIN CHECK
    if 'customer_id' not in session:

        return redirect(
            url_for('login')
        )

    orders = Order.query.filter_by(
        customer_id=session[
            'customer_id'
        ]
    ).order_by(
        Order.id.desc()
    ).all()

    return render_template(
        'web/my_orders.html',
        orders=orders,
        categories=Category.query.all()
    )