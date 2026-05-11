from flask import (
    jsonify,
    request
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

from app.api import api

from app import db

from app.models.product import Product

from app.models.category import Category

from app.models.customer import Customer

from app.models.order import Order

from app.models.order_item import OrderItem




# =========================================
# API HOME
# =========================================
@api.route('/api')
def api_home():

    return jsonify({

        'status': True,

        'message': 'Flask Ecommerce API'
    })


# =========================================
# ALL PRODUCTS API
# =========================================
@api.route('/api/products')
def api_products():

    products = Product.query.all()

    data = []

    for product in products:

        data.append({

            'id': product.id,

            'name': product.name,

            'price': float(product.price),

            'stock': product.stock,

            'description': product.description,

            'image': product.image,

            'category': product.category.name
        })

    return jsonify({

        'status': True,

        'total': len(data),

        'products': data
    })


# =========================================
# SINGLE PRODUCT API
# =========================================
@api.route('/api/product/<int:id>')
def api_single_product(id):

    product = Product.query.get_or_404(id)

    gst = round(
        (product.price * 18) / 100,
        2
    )

    final_price = round(
        product.price + gst,
        2
    )

    data = {

        'id': product.id,

        'name': product.name,

        'price': float(product.price),

        'gst': gst,

        'final_price': final_price,

        'stock': product.stock,

        'description': product.description,

        'image': product.image,

        'category': product.category.name
    }

    return jsonify({

        'status': True,

        'product': data
    })


# =========================================
# ALL CATEGORIES API
# =========================================
@api.route('/api/categories')
def api_categories():

    categories = Category.query.all()

    data = []

    for category in categories:

        data.append({

            'id': category.id,

            'name': category.name
        })

    return jsonify({

        'status': True,

        'categories': data
    })


# =========================================
# CUSTOMER REGISTER API
# =========================================
@api.route(
    '/api/register',
    methods=['POST']
)
def api_register():

    data = request.get_json()

    name = data.get('name')

    email = data.get('email')

    password = data.get('password')

    # EMAIL CHECK
    existing_user = Customer.query.filter_by(
        email=email
    ).first()

    if existing_user:

        return jsonify({

            'status': False,

            'message': 'Email already exists'
        })

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

    return jsonify({

        'status': True,

        'message': 'Registration Successful'
    })


# =========================================
# CUSTOMER LOGIN API
# =========================================
@api.route(
    '/api/login',
    methods=['POST']
)
def api_login():

    data = request.get_json()

    email = data.get('email')

    password = data.get('password')

    customer = Customer.query.filter_by(
        email=email
    ).first()

    if customer and check_password_hash(
        customer.password,
        password
    ):

        # CREATE JWT TOKEN
        access_token = create_access_token(

            identity=customer.id
        )

        return jsonify({

            'status': True,

            'message': 'Login Successful',

            'token': access_token,

            'customer': {

                'id': customer.id,

                'name': customer.name,

                'email': customer.email
            }
        })

    return jsonify({

        'status': False,

        'message': 'Invalid Email or Password'
    })


# =========================================
# CUSTOMER PROFILE API
# =========================================
@api.route('/api/profile')
@jwt_required()
def api_profile():

    customer_id = get_jwt_identity()

    customer = Customer.query.get(
        customer_id
    )

    if not customer:

        return jsonify({

            'status': False,

            'message': 'Customer not found'
        })

    return jsonify({

        'status': True,

        'customer': {

            'id': customer.id,

            'name': customer.name,

            'email': customer.email
        }
    })


# =========================================
# CUSTOMER ORDERS API
# =========================================
@api.route('/api/orders')
@jwt_required()
def api_orders():

    customer_id = get_jwt_identity()

    orders = Order.query.filter_by(
        customer_id=customer_id
    ).order_by(
        Order.id.desc()
    ).all()

    data = []

    for order in orders:

        items = []

        for item in order.order_items:

            items.append({

                'product_name': item.product_name,

                'price': item.product_price,

                'quantity': item.quantity,

                'subtotal': item.subtotal
            })

        data.append({

            'order_id': order.id,

            'total_amount': order.total_amount,

            'status': order.status,

            'address': order.address,

            'created_at': order.created_at,

            'items': items
        })

    return jsonify({

        'status': True,

        'orders': data
    })


# =========================================
# PLACE ORDER API
# =========================================
@api.route(
    '/api/place-order',
    methods=['POST']
)
@jwt_required()
def api_place_order():

    customer_id = get_jwt_identity()

    data = request.get_json()

    address = data.get('address')

    products = data.get('products')

    if not products:

        return jsonify({

            'status': False,

            'message': 'No products found'
        })

    total_amount = 0

    order_items_data = []

    for item in products:

        product = Product.query.get(
            item['product_id']
        )

        if not product:

            continue

        quantity = item['quantity']

        subtotal = (
            float(product.price) *
            quantity
        )

        total_amount += subtotal

        order_items_data.append({

            'product_name': product.name,

            'product_price': float(
                product.price
            ),

            'quantity': quantity,

            'subtotal': subtotal
        })

    # GST
    gst = round(
        (total_amount * 18) / 100,
        2
    )

    final_total = round(
        total_amount + gst,
        2
    )

    # CREATE ORDER
    order = Order(

        customer_id=customer_id,

        total_amount=final_total,

        address=address
    )

    db.session.add(order)

    db.session.commit()

    # SAVE ORDER ITEMS
    for item in order_items_data:

        order_item = OrderItem(

            order_id=order.id,

            product_name=item[
                'product_name'
            ],

            product_price=item[
                'product_price'
            ],

            quantity=item[
                'quantity'
            ],

            subtotal=item[
                'subtotal'
            ]
        )

        db.session.add(order_item)

    db.session.commit()

    return jsonify({

        'status': True,

        'message': 'Order Placed Successfully',

        'order_id': order.id,

        'total_amount': final_total
    })