from app import db


class Address(db.Model):

    __tablename__ = 'addresses'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    customer_id = db.Column(
        db.Integer,
        db.ForeignKey('customers.id')
    )

    full_name = db.Column(
        db.String(100),
        nullable=False
    )

    phone = db.Column(
        db.String(20),
        nullable=False
    )

    address = db.Column(
        db.Text,
        nullable=False
    )

    city = db.Column(
        db.String(100)
    )

    state = db.Column(
        db.String(100)
    )

    pincode = db.Column(
        db.String(20)
    )

    country = db.Column(
        db.String(100),
        default='India'
    )

    is_default = db.Column(
        db.Boolean,
        default=False
    )

    customer = db.relationship(
        'Customer',
        backref='addresses'
    )