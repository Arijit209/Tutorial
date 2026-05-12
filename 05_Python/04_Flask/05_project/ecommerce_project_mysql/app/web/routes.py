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

from app import db

from app.models.customer import Customer
from app.models.category import Category
from app.models.product import Product
from app.models.order import Order
from app.models.order_item import OrderItem
from app.models.address import Address


# =========================================
# WEB BLUEPRINT
# =========================================
web = Blueprint(
    'web',
    __name__
)


# =========================================
# CUSTOMER LOGIN REQUIRED
# =========================================
def customer_login_required():

    if 'customer_id' not in session:

        return False

    return True


# =========================================
# HOME PAGE
# =========================================
@web.route('/')
def home():

    search = request.args.get('search', '')

    category_id = request.args.get('category', '')

    page = request.args.get(
        'page',
        1,
        type=int
    )

    products_query = Product.query

    # SEARCH
    if search:

        products_query = products_query.filter(
            Product.name.ilike(f'%{search}%')
        )

    # CATEGORY FILTER
    if category_id:

        products_query = products_query.filter_by(
            category_id=category_id
        )

    products = products_query.order_by(
        Product.id.desc()
    ).paginate(
        page=page,
        per_page=6
    )

    categories = Category.query.all()

    return render_template(
        'web/home.html',
        products=products,
        categories=categories,
        search=search,
        category_id=category_id
    )


# =========================================
# PRODUCT DETAILS
# =========================================
@web.route('/product/<int:id>')
def product_details(id):

    product = Product.query.get_or_404(id)

    gst = round(
        (product.price * 18) / 100,
        2
    )

    final_price = round(
        product.price + gst,
        2
    )

    related_products = Product.query.filter(
        Product.category_id == product.category_id,
        Product.id != product.id
    ).limit(4).all()

    return render_template(
        'web/product_details.html',
        product=product,
        gst=gst,
        final_price=final_price,
        related_products=related_products
    )


# =========================================
# CUSTOMER REGISTER
# =========================================
@web.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        name = request.form.get('name')

        email = request.form.get('email')

        phone = request.form.get('phone')

        password = request.form.get('password')

        confirm_password = request.form.get(
            'confirm_password'
        )

        # CHECK PASSWORD
        if password != confirm_password:

            flash(
                'Password Does Not Match',
                'danger'
            )

            return redirect(
                url_for('web.register')
            )

        # CHECK EMAIL EXISTS
        old_customer = Customer.query.filter_by(
            email=email
        ).first()

        if old_customer:

            flash(
                'Email Already Exists',
                'danger'
            )

            return redirect(
                url_for('web.register')
            )

        # HASH PASSWORD
        hashed_password = generate_password_hash(
            password
        )

        customer = Customer(
            name=name,
            email=email,
            phone=phone,
            password=hashed_password
        )

        db.session.add(customer)
        db.session.commit()

        flash(
            'Registration Successful',
            'success'
        )

        return redirect(
            url_for('web.login')
        )

    return render_template(
        'web/register.html'
    )


# =========================================
# CUSTOMER LOGIN
# =========================================
@web.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        email = request.form.get('email')

        password = request.form.get('password')

        customer = Customer.query.filter_by(
            email=email
        ).first()

        if not customer:

            flash(
                'Invalid Email',
                'danger'
            )

            return redirect(
                url_for('web.login')
            )

        if not check_password_hash(
            customer.password,
            password
        ):

            flash(
                'Invalid Password',
                'danger'
            )

            return redirect(
                url_for('web.login')
            )

        # SESSION
        session['customer_id'] = customer.id
        session['customer_name'] = customer.name

        flash(
            'Login Successful',
            'success'
        )

        return redirect(
            url_for('web.home')
        )

    return render_template(
        'web/login.html'
    )


# =========================================
# LOGOUT
# =========================================
@web.route('/logout')
def logout():

    session.clear()

    flash(
        'Logout Successful',
        'success'
    )

    return redirect(
        url_for('web.login')
    )


# =========================================
# ADD TO CART
# =========================================
@web.route('/add-to-cart/<int:id>')
def add_to_cart(id):

    product = Product.query.get_or_404(id)

    cart = session.get('cart', {})

    product_id = str(product.id)

    if product_id in cart:

        cart[product_id] += 1

    else:

        cart[product_id] = 1

    session['cart'] = cart

    flash(
        'Product Added To Cart',
        'success'
    )

    return redirect(
        url_for('web.cart')
    )


# =========================================
# CART PAGE
# =========================================
@web.route('/cart')
def cart():

    cart = session.get('cart', {})

    cart_items = []

    subtotal = 0

    total_gst = 0

    grand_total = 0

    for product_id, quantity in cart.items():

        product = Product.query.get(product_id)

        if product:

            item_total = product.price * quantity

            gst = round(
                (item_total * 18) / 100,
                2
            )

            final_total = round(
                item_total + gst,
                2
            )

            subtotal += item_total

            total_gst += gst

            grand_total += final_total

            cart_items.append({
                'product': product,
                'quantity': quantity,
                'gst': gst,
                'total': final_total
            })

    return render_template(
        'web/cart.html',
        cart_items=cart_items,
        subtotal=round(subtotal, 2),
        total_gst=round(total_gst, 2),
        grand_total=round(grand_total, 2)
    )


# =========================================
# REMOVE CART ITEM
# =========================================
@web.route('/remove-cart/<int:id>')
def remove_cart(id):

    cart = session.get('cart', {})

    product_id = str(id)

    if product_id in cart:

        del cart[product_id]

    session['cart'] = cart

    flash(
        'Item Removed From Cart',
        'success'
    )

    return redirect(
        url_for('web.cart')
    )


# =========================================
# CHECKOUT
# =========================================
@web.route('/checkout', methods=['GET', 'POST'])
def checkout():

    if not customer_login_required():

        flash(
            'Please Login First',
            'danger'
        )

        return redirect(
            url_for('web.login')
        )

    customer = Customer.query.get(
        session['customer_id']
    )

    cart = session.get('cart', {})

    if not cart:

        flash(
            'Cart Is Empty',
            'danger'
        )

        return redirect(
            url_for('web.home')
        )

    cart_items = []

    subtotal = 0

    total_gst = 0

    grand_total = 0

    for product_id, quantity in cart.items():

        product = Product.query.get(product_id)

        if product:

            item_total = product.price * quantity

            gst = round(
                (item_total * 18) / 100,
                2
            )

            final_total = round(
                item_total + gst,
                2
            )

            subtotal += item_total

            total_gst += gst

            grand_total += final_total

            cart_items.append({
                'product': product,
                'quantity': quantity,
                'gst': gst,
                'total': final_total
            })

    if request.method == 'POST':

        # phone = request.form.get('phone')

        # address = request.form.get('address')
        
        default_address = Address.query.filter_by(
            customer_id=customer.id,
            is_default=True
        ).first()
        
        phone = default_address.phone

        address = (
            f"{default_address.address}, "
            f"{default_address.city}, "
            f"{default_address.state} - "
            f"{default_address.pincode}"
        )

        payment_method = request.form.get(
            'payment_method'
        )

        # CREATE ORDER
        order = Order(
            customer_id=customer.id,
            phone=phone,
            address=address,
            payment_method=payment_method,
            total_amount=grand_total,
            status='Pending'
        )

        db.session.add(order)
        db.session.commit()

        # CREATE ORDER ITEMS
        for item in cart_items:

            order_item = OrderItem(
                order_id=order.id,
                product_id=item['product'].id,
                product_name=item['product'].name,
                product_price=item['product'].price,
                product_image=item['product'].image,
                quantity=item['quantity'],
                gst=item['gst'],
                subtotal=item['total']
            )

            db.session.add(order_item)

        db.session.commit()

        # CLEAR CART
        session['cart'] = {}

        flash(
            'Order Placed Successfully',
            'success'
        )

        return redirect(
            url_for('web.my_orders')
        )

    return render_template(
        'web/checkout.html',
        customer=customer,
        cart_items=cart_items,
        subtotal=round(subtotal, 2),
        total_gst=round(total_gst, 2),
        grand_total=round(grand_total, 2)
    )
    
# =========================================
# MY ORDERS
# =========================================
@web.route('/my-orders')
def my_orders():

    if not customer_login_required():

        flash(
            'Please Login First',
            'danger'
        )

        return redirect(
            url_for('web.login')
        )

    orders = Order.query.filter_by(
        customer_id=session['customer_id']
    ).order_by(
        Order.id.desc()
    ).all()

    return render_template(
        'web/my_orders.html',
        orders=orders
    )

# =========================================
# INCREMENT CART ITEM
# =========================================
@web.route('/cart/increment/<int:id>')
def increment_cart(id):

    cart = session.get('cart', {})

    product_id = str(id)

    if product_id in cart:

        cart[product_id] += 1

    session['cart'] = cart

    return redirect(
        url_for('web.cart')
    )
    
# =========================================
# DECREMENT CART ITEM
# =========================================
@web.route('/cart/decrement/<int:id>')
def decrement_cart(id):

    cart = session.get('cart', {})

    product_id = str(id)

    if product_id in cart:

        if cart[product_id] > 1:

            cart[product_id] -= 1

        else:

            del cart[product_id]

    session['cart'] = cart

    return redirect(
        url_for('web.cart')
    )
    
# =========================================
# CUSTOMER PROFILE
# =========================================
@web.route('/profile', methods=['GET', 'POST'])
def profile():

    if not customer_login_required():

        return redirect(
            url_for('web.login')
        )

    customer = Customer.query.get(
        session['customer_id']
    )

    if request.method == 'POST':

        customer.name = request.form.get('name')

        customer.phone = request.form.get('phone')

        db.session.commit()

        flash(
            'Profile Updated Successfully',
            'success'
        )

        return redirect(
            url_for('web.profile')
        )

    return render_template(
        'web/profile.html',
        customer=customer
    )
    
# =========================================
# ADD ADDRESS
# =========================================
@web.route('/add-address', methods=['GET', 'POST'])
def add_address():

    if not customer_login_required():

        return redirect(
            url_for('web.login')
        )

    if request.method == 'POST':

        address = Address(

            customer_id=session['customer_id'],

            full_name=request.form.get(
                'full_name'
            ),

            phone=request.form.get(
                'phone'
            ),

            address=request.form.get(
                'address'
            ),

            city=request.form.get(
                'city'
            ),

            state=request.form.get(
                'state'
            ),

            pincode=request.form.get(
                'pincode'
            ),

            country=request.form.get(
                'country'
            ),

            is_default=True
        )

        # REMOVE OLD DEFAULT
        old_addresses = Address.query.filter_by(
            customer_id=session['customer_id']
        ).all()

        for old in old_addresses:

            old.is_default = False

        db.session.add(address)

        db.session.commit()

        flash(
            'Address Added Successfully',
            'success'
        )

        return redirect(
            url_for('web.profile')
        )

    return render_template(
        'web/add_address.html'
    )