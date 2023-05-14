import random
from datetime import datetime, timedelta
from typing import List

import mimesis
import sqlalchemy
from sqlalchemy import Column, Integer, String, DateTime, Float, SmallInteger, Enum, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, Mapped, sessionmaker
from sqlalchemy_utils import database_exists, create_database

Base = declarative_base()


class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    phone_number = Column(String(30), nullable=False)
    address = Column(String(150), nullable=False)
    city = Column(String(50), nullable=False)
    state = Column(String(50), nullable=False)
    zip_code = Column(String(10), nullable=False)
    create_date = Column(DateTime, default=datetime.utcnow() - timedelta(days=random.randint(0, 365)), nullable=False)
    update_date = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    orders: Mapped[List["Order"]] = relationship(backref="Customer")

    def __init__(self):
        self.first_name = mimesis.Person().first_name()
        self.last_name = mimesis.Person().last_name()
        self.email = mimesis.Person().email()
        self.phone_number = mimesis.Person().phone_number()
        self.address = mimesis.Address().address()
        self.city = mimesis.Address().city()
        self.state = mimesis.Address().state()
        self.zip_code = mimesis.Address().zip_code()

    def to_json(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'phone_number': self.phone_number,
            'address': self.address,
            'city': self.city,
            'state': self.state,
            'zip_code': self.zip_code,
            'create_date': self.create_date.isoformat() if self.create_date else None,
            'update_date': self.update_date.isoformat() if self.update_date else None
        }


class ProductCategory(Base):
    __tablename__ = 'product_categories'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    create_date = Column(DateTime, default=datetime.utcnow() - timedelta(days=random.randint(0, 365)), nullable=False)
    update_date = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    products: Mapped[List["Product"]] = relationship(backref="ProductCategory")

    def __init__(self):
        self.name = mimesis.Text().word()

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'create_date': self.create_date.isoformat() if self.create_date else None,
            'update_date': self.update_date.isoformat() if self.update_date else None
        }


class Manufacturer(Base):
    __tablename__ = 'manufacturers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    description = Column(String(1000), nullable=False)
    contact_person = Column(String(100), nullable=False)
    email = Column(String(50), nullable=False)
    create_date = Column(DateTime, default=datetime.utcnow() - timedelta(days=random.randint(0, 365)), nullable=False)
    update_date = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    products_ref = relationship('Product', backref='Manufacturer')

    def __init__(self):
        self.name = mimesis.Finance().company()
        self.description = mimesis.Text().sentence()
        self.contact_person = mimesis.Person().full_name()
        self.email = mimesis.Person().email()

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'contact_person': self.contact_person,
            'email': self.email,
            'create_date': self.create_date.isoformat() if self.create_date else None,
            'update_date': self.update_date.isoformat() if self.update_date else None
        }


class Supplier(Base):
    __tablename__ = 'suppliers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    contact_name = Column(String(100), nullable=False)
    phone_number = Column(String(1000), nullable=False)
    address = Column(String(150), nullable=False)
    email = Column(String(50), nullable=False)
    create_date = Column(DateTime, default=datetime.utcnow() - timedelta(days=random.randint(0, 365)), nullable=False)
    update_date = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    products_ref = relationship('Product', backref='Supplier')

    def __init__(self):
        self.name = mimesis.Finance().company()
        self.description = mimesis.Text().sentence()
        self.phone_number = mimesis.Person().phone_number()
        self.contact_name = mimesis.Person().full_name()
        self.contact_person = mimesis.Person().full_name()
        self.email = mimesis.Person().email()
        self.phone_number = mimesis.Person().phone_number()
        self.contact_name = mimesis.Person().full_name()
        self.address = mimesis.Address().address()

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'contact_name': self.contact_name,
            'phone_number': self.phone_number,
            'email': self.email,
            'address': self.address,
            'create_date': self.create_date.isoformat() if self.create_date else None,
            'update_date': self.update_date.isoformat() if self.update_date else None
        }


class Packaging(Base):
    __tablename__ = 'packaging'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    description = Column(String(1000), nullable=False)
    create_date = Column(DateTime, default=datetime.utcnow() - timedelta(days=random.randint(0, 365)), nullable=False)
    update_date = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    products_ref = relationship('Product', backref='Packaging')

    def __init__(self):
        self.name = mimesis.Food().spices() + random.choice(['XL', 'L', 'M', 'S', 'XS'])
        self.description = mimesis.Text().sentence()

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'create_date': self.create_date.isoformat() if self.create_date else None,
            'update_date': self.update_date.isoformat() if self.update_date else None
        }


class Discount(Base):
    __tablename__ = 'discounts'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(200), nullable=False)
    description = Column(String(1000), nullable=False)
    start_date = Column(DateTime, nullable=False)
    discount_percent = Column(Float(precision=2), nullable=False, default=5)
    end_date = Column(DateTime, nullable=False)

    create_date = Column(DateTime, default=datetime.utcnow() - timedelta(days=random.randint(0, 365)), nullable=False)
    update_date = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    products_ref = relationship('Product', backref='Discount')

    def __init__(self):
        now = datetime.now()
        self.title = mimesis.Text().word()
        self.description = mimesis.Text().sentence()
        self.discount_percent = random.randint(5, 100)
        # Generate a date in the past, but not older than 3 months
        three_months_ago = now - timedelta(days=90)
        self.start_date = three_months_ago + timedelta(
            seconds=random.randint(0, int((now - three_months_ago).total_seconds())))

        # Generate a date between now-1 month and now+7 months
        one_month_ago = now - timedelta(days=30)
        seven_months_future = now + timedelta(days=7 * 30)
        self.end_date = one_month_ago + timedelta(seconds=random.randint(0, int((seven_months_future - one_month_ago).total_seconds())))

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'start_date': self.start_date.isoformat() if self.start_date else None,
            'discount_percent': self.discount_percent,
            'end_date': self.end_date.isoformat() if self.end_date else None,
            'create_date': self.create_date.isoformat() if self.create_date else None,
            'update_date': self.update_date.isoformat() if self.update_date else None
        }


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    description = Column(String(1000), nullable=False)
    price = Column(Float(precision=2), nullable=False)
    quantity = Column(SmallInteger, nullable=False)
    manufacturer_id = Column(Integer, ForeignKey('manufacturers.id'), nullable=False)
    discount_id = Column(Integer, ForeignKey('discounts.id'), nullable=False)
    supplier_id = Column(Integer, ForeignKey('suppliers.id'), nullable=False)
    packaging_id = Column(Integer, ForeignKey('packaging.id'), nullable=False)
    category_id = Column(Integer, ForeignKey('product_categories.id'), nullable=False)

    create_date = Column(DateTime, default=datetime.utcnow() - timedelta(days=random.randint(0, 365)), nullable=False)
    update_date = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    category_ref = relationship('ProductCategory', backref='Product')
    manufacturer_ref = relationship('Manufacturer', backref='Product')
    discount_ref = relationship('Discount', backref='Product')
    supplier_ref = relationship('Supplier', backref='Product')
    packaging_ref = relationship('Packaging', backref='Product')
    order_items_ref = relationship('OrderItem', backref='Product')
    comments_ref = relationship('Comment', backref='Product')

    def __init__(self, category: ProductCategory, manufacturer: Manufacturer, discount: Discount, supplier: Supplier,
                 packaging: Packaging):
        self.name = f"{mimesis.Food().drink()}ol"
        self.description = mimesis.Text().text()
        self.price = random.randint(20, 200)
        self.quantity = random.randint(1, 50)
        self.category_id = category.id
        self.category_ref = category
        self.manufacturer_ref = manufacturer
        self.manufacturer_id = manufacturer.id
        self.discount_id = discount.id
        self.supplier_id = supplier.id
        self.packaging_id = packaging.id
        self.discount_ref = discount
        self.packaging_ref = packaging
        self.supplier_ref = supplier

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'quantity': self.quantity,
            'manufacturer_id': self.manufacturer_id,
            'discount_id': self.discount_id,
            'supplier_id': self.supplier_id,
            'packaging_id': self.packaging_id,
            'category_id': self.category_id,
            'description': self.description,
            'create_date': self.create_date.isoformat() if self.create_date else None,
            'update_date': self.update_date.isoformat() if self.update_date else None
        }


class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    comment_text = Column(String(255), nullable=False)
    rating = Column(SmallInteger, nullable=False)

    create_date = Column(DateTime, default=datetime.utcnow() - timedelta(days=random.randint(0, 365)), nullable=False)
    update_date = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    product = relationship('Product', backref='comments')
    customer = relationship('Customer', backref='comments')

    def __init__(self, product: Product, customer: Customer):
        self.comment_text = mimesis.Text().sentence()
        self.rating = random.Random().randint(0, 10)
        self.product = product
        self.customer = customer
        self.product_id = product.id
        self.customer_id = customer.id

    def to_json(self):
        return {
            'id': self.id,
            'product_id': self.product_id,
            'customer_id': self.customer_id,
            'comment_text': self.comment_text,
            'rating': self.rating,
            'create_date': self.create_date.isoformat() if self.create_date else None,
            'update_date': self.update_date.isoformat() if self.update_date else None
        }


class Shipping(Base):
    __tablename__ = 'shipping'

    id = Column(Integer, primary_key=True, autoincrement=True)
    delivery_date = Column(DateTime, nullable=False)
    carrier = Column(String(255), nullable=False)
    receiver = Column(String(255), nullable=False)
    tracking_number = Column(String(255), nullable=False)
    shipping_address = Column(String(255), nullable=False)
    shipping_city = Column(String(255), nullable=False)
    shipping_state = Column(String(255), nullable=False)
    shipping_zip = Column(String(255), nullable=False)

    create_date = Column(DateTime, default=datetime.utcnow() - timedelta(days=random.randint(0, 365)), nullable=False)
    update_date = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    orders: Mapped[List["Order"]] = relationship(backref="Shipping")

    def __init__(self):
        now = datetime.now()
        four_days_ago = now - timedelta(days=4)
        fifteen_days_future = now + timedelta(days=15)

        self.delivery_date = four_days_ago + timedelta(seconds=random.randint(0, int((fifteen_days_future - four_days_ago).total_seconds())))
        self.receiver = mimesis.Person().full_name()
        self.carrier = mimesis.Finance().company()
        self.shipping_address = mimesis.Address().address()
        self.shipping_zip = mimesis.Address().zip_code()
        self.shipping_city = mimesis.Address().city()
        self.shipping_state = mimesis.Address().state()
        self.tracking_number = mimesis.Payment().credit_card_number()

    def to_json(self):
        return {
            'id': self.id,
            'delivery_date': self.delivery_date.isoformat() if self.delivery_date else None,
            'carrier': self.carrier,
            'receiver': self.receiver,
            'tracking_number': self.tracking_number,
            'shipping_address': self.shipping_address,
            'shipping_city': self.shipping_city,
            'shipping_state': self.shipping_state,
            'shipping_zip': self.shipping_zip,
            'create_date': self.create_date.isoformat() if self.create_date else None,
            'update_date': self.update_date.isoformat() if self.update_date else None
        }


class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    shipping_id = Column(Integer, ForeignKey('shipping.id'), nullable=False)
    order_date = Column(DateTime, nullable=False)
    status = Column(Enum('Accepted', 'InProgress', 'Done', 'Canceled', name='order_status'), nullable=False, default='Accepted')

    create_date = Column(DateTime, default=datetime.utcnow() - timedelta(days=random.randint(0, 365)), nullable=False)
    update_date = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    customer = relationship("Customer", backref="Order")
    shipping = relationship("Shipping", backref="Order")

    def __init__(self, customer: Customer, shipping: Shipping):
        now = datetime.now()
        self.customer = customer
        self.shipping = shipping
        self.shipping_id = shipping.id
        self.customer_id = customer.id

        # Dates for 2 weeks ago and 4 hours ago
        two_weeks_ago = now - timedelta(weeks=2)
        four_hours_ago = now - timedelta(hours=4)
        total_seconds = int((four_hours_ago - two_weeks_ago).total_seconds())

        # Generate a random date between two_weeks_ago and four_hours_ago
        self.order_date = two_weeks_ago + timedelta(seconds=random.randint(0, total_seconds))
        self.status = random.choice(['Accepted', 'InProgress', 'Done', 'Canceled'])

    def to_json(self):
        return {
            'id': self.id,
            'customer_id': self.customer_id,
            'shipping_id': self.shipping_id,
            'order_date': self.order_date.isoformat() if self.order_date else None,
            'status': self.status,
            'create_date': self.create_date.isoformat() if self.create_date else None,
            'update_date': self.update_date.isoformat() if self.update_date else None
        }


class Payment(Base):
    __tablename__ = 'payments'

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    payment_date = Column(DateTime, default=datetime.utcnow, nullable=False)
    payment_method = Column(String(50), nullable=False)
    payment_amount = Column(Float(precision=2), nullable=False)
    card_number = Column(String(20))
    card_holder = Column(String(100))

    create_date = Column(DateTime, default=datetime.utcnow() - timedelta(days=random.randint(0, 365)), nullable=False)
    update_date = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    order = relationship('Order', backref='payments')

    def __init__(self, order: Order):
        now = datetime.now()
        self.card_number = mimesis.Payment().credit_card_number()[-4:]
        self.payment_method = mimesis.Payment().credit_card_network()
        self.card_holder = mimesis.Person().full_name()
        self.payment_amount = random.Random().randint(100, 1000) / 100
        self.order_id = order.id

        # Dates for 2 weeks ago and 4 hours ago
        two_weeks_ago = now - timedelta(weeks=2)
        four_hours_ago = now - timedelta(hours=4)
        total_seconds = int((four_hours_ago - two_weeks_ago).total_seconds())

        # Generate a random date between two_weeks_ago and four_hours_ago
        self.payment_date = two_weeks_ago + timedelta(seconds=random.randint(0, total_seconds))
        self.order = order

    def to_json(self):
        return {
            'id': self.id,
            'order_id': self.order_id,
            'payment_date': self.payment_date.isoformat() if self.payment_date else None,
            'payment_method': self.payment_method,
            'payment_amount': self.payment_amount,
            'card_number': self.card_number,
            'card_holder': self.card_holder,
        }


class OrderItem(Base):
    __tablename__ = 'order_items'

    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False, primary_key=True)
    quantity = Column(Integer, nullable=False)

    create_date = Column(DateTime, default=datetime.utcnow() - timedelta(days=random.randint(0, 365)), nullable=False)
    update_date = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    order = relationship('Order', backref='order_items')
    product = relationship('Product', backref='order_items')

    def __init__(self, product: Product, order: Order):
        self.quantity = random.Random().randint(1, 10)
        self.product_id = product.id
        self.order_id = order.id
        self.order = order
        self.product = product

    def to_json(self):
        return {
            'order_id': self.order_id,
            'product_id': self.product_id,
            'quantity': self.quantity,
        }


class DbHelper:
    engine = None
    session = None

    def __init__(self, connection_string: str):
        self.engine = sqlalchemy.create_engine(connection_string)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def connect(self):
        # Create database if it does not exist.
        if not database_exists(self.engine.url):
            create_database(self.engine.url)
        else:
            # Connect the database if exists.
            self.engine.connect()

    def create_tables(self):
        Base.metadata.create_all(self.engine)
