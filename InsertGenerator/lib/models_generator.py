import random
from typing import List, Type

from sqlalchemy.orm import Session

from lib.db_service import DbService
from models.models import Customer, ProductCategory, Manufacturer, Order, Payment, Product, OrderItem, Comment


class ModelsGenerator:
    customers = []
    categories = []
    manufactors = []
    orders = []
    products = []
    payments = []
    comments = []
    order_items = []
    session = None
    db_service = None

    def __init__(self, ses: Session):
        self.session = ses
        self.db_service = DbService(self.session)

    def generate_objects(self, count: int, obj_type: Type) -> List[object]:
        res = []
        for _ in range(count):
            obj = obj_type()
            res.append(obj)
            if isinstance(obj, Customer):
                self.customers.append(obj)
            elif isinstance(obj, ProductCategory):
                self.categories.append(obj)
            elif isinstance(obj, Manufacturer):
                self.manufactors.append(obj)
        return res

    def generate_orders(self, count: int) -> List[Order]:
        temp_customers = self.db_service.get_instances(count, Customer)
        res = [Order(random.choice(temp_customers)) for _ in range(count)]
        self.orders.extend(res)
        return res

    def generate_payments(self, count: int) -> List[Payment]:
        temp_orders = self.db_service.get_instances(count, Order)
        res = [Payment(random.choice(temp_orders)) for _ in range(count)]
        self.payments.extend(res)
        return res

    def generate_products(self, count: int) -> List[Product]:
        temp_manufactors = self.db_service.get_instances(count, Manufacturer)
        temp_categories = self.db_service.get_instances(5, ProductCategory)
        res = [Product(random.choice(temp_categories), random.choice(temp_manufactors)) for _ in range(count)]
        self.products.extend(res)
        return res

    def generate_order_item(self, count: int) -> List[OrderItem]:
        temp_products = self.db_service.get_instances(count, Product)
        temp_orders = self.db_service.get_instances(count, Order)
        res = [OrderItem(random.choice(temp_products), random.choice(temp_orders)) for _ in range(count)]
        self.order_items.extend(res)
        return res

    def generate_comment(self, count: int) -> List[Comment]:
        temp_products = self.db_service.get_instances(count, Product)
        temp_customers = self.db_service.get_instances(count, Customer)
        res = [Comment(random.choice(temp_products), random.choice(temp_customers)) for _ in range(count)]
        self.comments.extend(res)
        return res

    def load_by_lst(self, lst: list) -> None:
        self.session.bulk_save_objects(lst)
        self.session.commit()

    def load_all(self) -> None:
        pass
