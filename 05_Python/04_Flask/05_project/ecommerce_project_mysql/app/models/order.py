from app import db
from datetime import datetime


class Order(db.Model):

    __tablename__ = 'orders'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    customer_id = db.Column(
        db.Integer,
        db.ForeignKey('customers.id'),
        nullable=False
    )

    total_amount = db.Column(
        db.Float,
        nullable=False
    )

    address = db.Column(
        db.Text,
        nullable=False
    )

    status = db.Column(
        db.String(50),
        default='Pending'
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    order_items = db.relationship(
        'OrderItem',
        backref='order',
        lazy=True
    )

    def __repr__(self):

        return f'<Order {self.id}>'