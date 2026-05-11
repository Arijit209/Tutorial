from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from flask_jwt_extended import JWTManager


# =========================================
# DATABASE
# =========================================
db = SQLAlchemy()


# =========================================
# JWT
# =========================================
jwt = JWTManager()


# =========================================
# CREATE APP
# =========================================
def create_app():

    app = Flask(__name__)

    # LOAD CONFIG
    app.config.from_object(
        'config.Config'
    )

    # INIT DATABASE
    db.init_app(app)

    # INIT JWT
    jwt.init_app(app)

    # =========================================
    # IMPORT MODELS
    # =========================================
    with app.app_context():

        from app.models.user import User

        from app.models.customer import Customer

        from app.models.category import Category

        from app.models.product import Product

        from app.models.order import Order

        from app.models.order_item import OrderItem

        db.create_all()

    # =========================================
    # REGISTER BLUEPRINTS
    # =========================================
    from app.admin import admin

    from app.web import web

    from app.api import api

    app.register_blueprint(admin)

    app.register_blueprint(web)

    app.register_blueprint(api)

    return app