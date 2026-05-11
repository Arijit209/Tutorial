from app import db

class Product(db.Model):

    __tablename__ = 'products'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(200),
        nullable=False
    )

    price = db.Column(
        db.Float,
        nullable=False
    )

    description = db.Column(
        db.Text
    )

    image = db.Column(
        db.String(255)
    )

    stock = db.Column(
        db.Integer,
        default=0
    )

    category_id = db.Column(
        db.Integer,
        db.ForeignKey('categories.id'),
        nullable=False
    )

    def __repr__(self):

        return f'<Product {self.name}>'