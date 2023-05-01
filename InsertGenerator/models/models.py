import random
from datetime import datetime
from typing import List

import mimesis
import sqlalchemy
from lorem.text import TextLorem
from sqlalchemy import Column, Integer, String, DateTime, Float, SmallInteger, Enum, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, Mapped, Session, sessionmaker
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
    create_date = Column(DateTime, default=datetime.utcnow, nullable=False)
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


class ProductCategory(Base):
    __tablename__ = 'product_categories'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    create_date = Column(DateTime, default=datetime.utcnow, nullable=False)
    update_date = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    products: Mapped[List["Product"]] = relationship(backref="ProductCategory")

    def __init__(self):
        self.name = mimesis.Text().word()


class Manufacturer(Base):
    __tablename__ = 'manufacturers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    description = Column(String(1000), nullable=False)
    contact_person = Column(String(100), nullable=False)
    email = Column(String(50), nullable=False)
    create_date = Column(DateTime, default=datetime.utcnow, nullable=False)
    update_date = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    products_ref = relationship('Product', backref='Manufacturer')

    def __init__(self):
        self.name = mimesis.Finance().company()
        self.description = mimesis.Text().sentence()
        self.contact_person = mimesis.Person().full_name()
        self.email = mimesis.Person().email()


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    description = Column(String(1000), nullable=False)
    price = Column(Float(precision=2), nullable=False)
    quantity = Column(SmallInteger, nullable=False)
    manufacturer_id = Column(Integer, ForeignKey('manufacturers.id'), nullable=False)
    category_id = Column(Integer, ForeignKey('product_categories.id'), nullable=False)
    create_date = Column(DateTime, default=datetime.utcnow, nullable=False)
    update_date = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    category_ref = relationship('ProductCategory', backref='Product')
    manufacturer_ref = relationship('Manufacturer', backref='Product')
    order_items_ref = relationship('OrderItem', backref='Product')
    comments_ref = relationship('Comment', backref='Product')

    def __init__(self, category: ProductCategory, manufacturer: Manufacturer):
        self.name = f"{mimesis.Food().drink()}ol"
        self.description = mimesis.Text().text()
        self.price = random.randint(20, 200)
        self.quantity = random.randint(1, 50)
        self.category_id = category.id
        self.category_ref = category
        self.manufacturer_ref = manufacturer
        self.manufacturer_id = manufacturer.id


class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    order_date = Column(DateTime, default=datetime.utcnow, nullable=False)
    total = Column(Float(precision=2), nullable=False)
    status = Column(Enum('Accepted', 'InProgress', 'Done', 'Canceled', name='order_status'), nullable=False,
                    default='Accepted')
    create_date = Column(DateTime, default=datetime.utcnow, nullable=False)
    update_date = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    customer = relationship("Customer", backref="Order")

    def __init__(self, customer: Customer):
        self.total = random.Random().randint(1, 100)
        self.customer = customer
        self.customer_id = customer.id
        self.status = random.choice(['Accepted', 'InProgress', 'Done', 'Canceled'])


class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    comment_text = Column(String(255), nullable=False)
    rating = Column(SmallInteger, nullable=False)
    create_date = Column(DateTime, default=datetime.utcnow, nullable=False)
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


class Payment(Base):
    __tablename__ = 'payments'

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    payment_date = Column(DateTime, default=datetime.utcnow, nullable=False)
    payment_method = Column(String(50), nullable=False)
    payment_amount = Column(Float(precision=2), nullable=False)
    card_number = Column(String(20))
    card_holder = Column(String(100))
    card_exp_month = Column(Integer)
    card_exp_year = Column(Integer)
    card_cvv = Column(String(10))

    order = relationship('Order', backref='payments')

    def __init__(self, order: Order):
        self.card_number = mimesis.Payment().credit_card_number()
        self.card_exp_year = random.randint(2025, 2030)
        self.card_exp_month = random.randint(1, 12)
        self.card_cvv = random.randint(100, 999)
        self.payment_method = mimesis.Payment().credit_card_network()
        self.card_holder = mimesis.Person().full_name()
        self.payment_amount = random.Random().randint(100, 1000) / 100
        self.order_id = order.id
        self.order = order


class OrderItem(Base):
    __tablename__ = 'order_items'

    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False, primary_key=True)
    quantity = Column(Integer, nullable=False)

    order = relationship('Order', backref='order_items')
    product = relationship('Product', backref='order_items')

    def __init__(self, product: Product, order: Order):
        self.quantity = random.Random().randint(1, 10)
        self.product_id = product.id
        self.order_id = order.id
        self.order = order
        self.product = product


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
