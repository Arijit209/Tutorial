import os

BASE_DIR = os.path.abspath(
    os.path.dirname(__file__)
)

class Config:

    SECRET_KEY = 'mysecretkey'

    SQLALCHEMY_DATABASE_URI = (
        'mysql+pymysql://root:root@localhost:3309/flask_ecommerce'
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    JWT_SECRET_KEY = 'jwt-secret-key'

    UPLOAD_FOLDER = os.path.join(
        BASE_DIR,
        'app/static/images'
    )