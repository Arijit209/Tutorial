from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

db = SQLAlchemy()

jwt = JWTManager()


def create_app():

    app = Flask(__name__)

    # =========================
    # CONFIG
    # =========================
    app.config.from_object('config.Config')

    # =========================
    # INIT DATABASE
    # =========================
    db.init_app(app)

    # =========================
    # INIT JWT
    # =========================
    jwt.init_app(app)

    with app.app_context():

        # =========================
        # IMPORT MODELS
        # =========================
        from app.models.user import User
        from app.models.customer import Customer
        from app.models.category import Category
        from app.models.product import Product
        from app.models.order import Order
        from app.models.order_item import OrderItem
        from app.models.address import Address

        # =========================
        # CREATE TABLES
        # =========================
        db.create_all()

    # =========================
    # IMPORT BLUEPRINTS
    # =========================
    from app.admin.routes import admin
    from app.web.routes import web
    from app.api.routes import api

    # =========================
    # REGISTER BLUEPRINTS
    # =========================
    app.register_blueprint(admin)

    app.register_blueprint(web)

    app.register_blueprint(api)

    # =========================
    # ERROR HANDLERS
    # =========================
    from app.errors.handlers import (
        register_error_handlers
    )

    register_error_handlers(app)

    return app

# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_jwt_extended import JWTManager

# db = SQLAlchemy()
# jwt = JWTManager()


# def create_app():

#     app = Flask(__name__)

#     # =========================
#     # CONFIG
#     # =========================
#     app.config.from_object('config.Config')

#     # =========================
#     # INIT EXTENSIONS
#     # =========================
#     db.init_app(app)
#     jwt.init_app(app)

#     # =========================
#     # IMPORT MODELS (IMPORTANT: only register)
#     # =========================
#     from app.models.user import User
#     from app.models.customer import Customer
#     from app.models.category import Category
#     from app.models.product import Product
#     from app.models.order import Order
#     from app.models.order_item import OrderItem
#     from app.models.address import Address

#     # =========================
#     # CREATE TABLES (DEV ONLY)
#     # =========================
#     with app.app_context():
#         db.create_all()
#         print("✅ Tables created successfully")

#     # =========================
#     # BLUEPRINTS
#     # =========================
#     from app.admin.routes import admin
#     from app.web.routes import web
#     from app.api.routes import api

#     app.register_blueprint(admin)
#     app.register_blueprint(web)
#     app.register_blueprint(api)

#     # =========================
#     # ERROR HANDLERS
#     # =========================
#     from app.errors.handlers import register_error_handlers
#     register_error_handlers(app)

#     return app