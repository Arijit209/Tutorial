from flask import (
    Blueprint,
    request,
    jsonify
)

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity
)

from app import db

from app.models.customer import Customer
from app.models.category import Category
from app.models.product import Product
from app.models.order import Order
from app.models.order_item import OrderItem


# =========================================
# API BLUEPRINT
# =========================================
api = Blueprint(
    'api',
    __name__,
    url_prefix='/api'
)


# =========================================
# API HOME
# =========================================
@api.route('/')
def api_home():

    return jsonify({
        'success': True,
        'message': 'Flask Ecommerce API'
    })


# =========================================
# CUSTOMER REGISTER API
# =========================================
@api.route('/register', methods=['POST'])
def api_register():

    data = request.get_json()

    name = data.get('name')

    email = data.get('email')

    phone = data.get('phone')

    password = data.get('password')

    confirm_password = data.get(
        'confirm_password'
    )

    # VALIDATION
    if password != confirm_password:

        return jsonify({
            'success': False,
            'message': 'Password Does Not Match'
        }), 400

    # CHECK EMAIL EXISTS
    old_customer = Customer.query.filter_by(
        email=email
    ).first()

    if old_customer:

        return jsonify({
            'success': False,
            'message': 'Email Already Exists'
        }), 400

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

    return jsonify({
        'success': True,
        'message': 'Registration Successful'
    })


# =========================================
# CUSTOMER LOGIN API
# =========================================
@api.route('/login', methods=['POST'])
def api_login():

    data = request.get_json()

    email = data.get('email')

    password = data.get('password')

    customer = Customer.query.filter_by(
        email=email
    ).first()

    # EMAIL CHECK
    if not customer:

        return jsonify({
            'success': False,
            'message': 'Invalid Email'
        }), 401

    # PASSWORD CHECK
    if not check_password_hash(
        customer.password,
        password
    ):

        return jsonify({
            'success': False,
            'message': 'Invalid Password'
        }), 401

    # JWT TOKEN
    access_token = create_access_token(
        identity=str(customer.id)
    )

    return jsonify({
        'success': True,
        'message': 'Login Successful',
        'token': access_token,
        'customer': {
            'id': customer.id,
            'name': customer.name,
            'email': customer.email,
            'phone': customer.phone
        }
    })


# =========================================
# CUSTOMER PROFILE API
# =========================================
@api.route('/profile')
@jwt_required()
def profile():

    customer_id = get_jwt_identity()

    customer = Customer.query.get(
        customer_id
    )

    if not customer:

        return jsonify({
            'success': False,
            'message': 'Customer Not Found'
        }), 404

    return jsonify({
        'success': True,
        'customer': {
            'id': customer.id,
            'name': customer.name,
            'email': customer.email,
            'phone': customer.phone
        }
    })


# =========================================
# CATEGORY LIST API
# =========================================
@api.route('/categories')
def categories():

    categories = Category.query.order_by(
        Category.id.desc()
    ).all()

    category_data = []

    for category in categories:

        category_data.append({
            'id': category.id,
            'name': category.name
        })

    return jsonify({
        'success': True,
        'categories': category_data
    })


# =========================================
# PRODUCT LIST API
# =========================================
@api.route('/products')
def products():

    products = Product.query.order_by(
        Product.id.desc()
    ).all()

    product_data = []

    for product in products:

        gst = round(
            (product.price * 18) / 100,
            2
        )

        final_price = round(
            product.price + gst,
            2
        )

        product_data.append({
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'gst': gst,
            'final_price': final_price,
            'stock': product.stock,
            'description': product.description,
            'image': product.image,
            'category': product.category.name
        })

    return jsonify({
        'success': True,
        'products': product_data
    })


# =========================================
# SINGLE PRODUCT API
# =========================================
@api.route('/product/<int:id>')
def single_product(id):

    product = Product.query.get_or_404(id)

    gst = round(
        (product.price * 18) / 100,
        2
    )

    final_price = round(
        product.price + gst,
        2
    )

    return jsonify({
        'success': True,
        'product': {
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'gst': gst,
            'final_price': final_price,
            'stock': product.stock,
            'description': product.description,
            'image': product.image,
            'category': product.category.name
        }
    })


# =========================================
# SEARCH PRODUCT API
# =========================================
@api.route('/search')
def search_product():

    keyword = request.args.get(
        'keyword',
        ''
    )

    products = Product.query.filter(
        Product.name.ilike(f'%{keyword}%')
    ).all()

    product_data = []

    for product in products:

        gst = round(
            (product.price * 18) / 100,
            2
        )

        final_price = round(
            product.price + gst,
            2
        )

        product_data.append({
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'final_price': final_price,
            'image': product.image
        })

    return jsonify({
        'success': True,
        'products': product_data
    })


# =========================================
# CREATE ORDER API
# =========================================
@api.route('/create-order', methods=['POST'])
@jwt_required()
def create_order():

    customer_id = get_jwt_identity()

    customer = Customer.query.get(
        customer_id
    )

    if not customer:

        return jsonify({
            'success': False,
            'message': 'Customer Not Found'
        }), 404

    data = request.get_json()

    address = data.get('address')

    phone = data.get('phone')

    payment_method = data.get(
        'payment_method'
    )

    items = data.get('items')

    if not items:

        return jsonify({
            'success': False,
            'message': 'No Items Found'
        }), 400

    subtotal = 0

    total_gst = 0

    grand_total = 0

    # CALCULATE TOTAL
    for item in items:

        product = Product.query.get(
            item['product_id']
        )

        if not product:

            continue

        quantity = item['quantity']

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

    # CREATE ORDER
    order = Order(
        customer_id=customer.id,
        address=address,
        phone=phone,
        payment_method=payment_method,
        total_amount=grand_total,
        status='Pending'
    )

    db.session.add(order)
    db.session.commit()

    # CREATE ORDER ITEMS
    for item in items:

        product = Product.query.get(
            item['product_id']
        )

        if not product:

            continue

        quantity = item['quantity']

        item_total = product.price * quantity

        gst = round(
            (item_total * 18) / 100,
            2
        )

        final_total = round(
            item_total + gst,
            2
        )

        order_item = OrderItem(
            order_id=order.id,
            product_id=product.id,
            product_name=product.name,
            product_price=product.price,
            product_image=product.image,
            quantity=quantity,
            gst=gst,
            subtotal=final_total
        )

        db.session.add(order_item)

    db.session.commit()

    return jsonify({
        'success': True,
        'message': 'Order Created Successfully',
        'order_id': order.id,
        'subtotal': subtotal,
        'gst': total_gst,
        'grand_total': grand_total
    })


# =========================================
# MY ORDERS API
# =========================================
@api.route('/my-orders')
@jwt_required()
def my_orders():

    customer_id = get_jwt_identity()

    orders = Order.query.filter_by(
        customer_id=customer_id
    ).order_by(
        Order.id.desc()
    ).all()

    order_data = []

    for order in orders:

        order_data.append({
            'id': order.id,
            'total_amount': order.total_amount,
            'payment_method': order.payment_method,
            'status': order.status,
            'address': order.address
        })

    return jsonify({
        'success': True,
        'orders': order_data
    })


# =========================================
# SINGLE ORDER API
# =========================================
@api.route('/order/<int:id>')
@jwt_required()
def single_order(id):

    customer_id = get_jwt_identity()

    order = Order.query.filter_by(
        id=id,
        customer_id=customer_id
    ).first()

    if not order:

        return jsonify({
            'success': False,
            'message': 'Order Not Found'
        }), 404

    items = []

    for item in order.items:

        items.append({
            'product_name': item.product_name,
            'product_price': item.product_price,
            'quantity': item.quantity,
            'gst': item.gst,
            'subtotal': item.subtotal,
            'image': item.product_image
        })

    return jsonify({
        'success': True,
        'order': {
            'id': order.id,
            'total_amount': order.total_amount,
            'payment_method': order.payment_method,
            'status': order.status,
            'address': order.address,
            'items': items
        }
    })