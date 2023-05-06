import random
from typing import List

from sqlalchemy.orm import Session

from deformation import *
from lib.db_service import DbService
from models.models import Customer, ProductCategory, Manufacturer, Order, Payment, Product, OrderItem, Comment, \
    Packaging, Discount, Shipping, Supplier


class ModelsGenerator:
    customers = []
    categories = []
    manufactors = []
    orders = []
    products = []
    payments = []
    suppliers = []
    shipping = []
    comments = []
    discounts = []
    packaging = []
    order_items = []
    session = None
    db_service = None

    def __init__(self, ses: Session):
        self.session = ses
        self.db_service = DbService(self.session)

    def generate_manufacturer(self, count: int, deformator: ManufacturerDeformationInterface) -> List[Manufacturer]:
        rows = (Manufacturer() for _ in range(count))
        res = [deformator.spoil(row) for row in rows]
        self.manufactors.extend(res)
        return res

    def generate_packaging(self, count: int) -> List[Packaging]:
        rows = (Packaging() for _ in range(count))
        self.packaging.extend(rows)
        return rows

    def generate_discount(self, count: int) -> List[Discount]:
        rows = (Discount() for _ in range(count))
        self.discounts.extend(rows)
        return rows

    def generate_shipping(self, count: int) -> List[Shipping]:
        rows = (Shipping() for _ in range(count))
        self.shipping.extend(rows)
        return rows

    def generate_supplier(self, count: int) -> List[Supplier]:
        rows = (Supplier() for _ in range(count))
        self.suppliers.extend(rows)
        return rows

    def generate_orders(self, count: int, deformator: OrderDeformationInterface) -> List[Order]:
        temp_customers = self.db_service.get_instances(count, Customer)
        temp_shipping = self.db_service.get_instances(count, Shipping)
        rows = (Order(random.choice(temp_customers), random.choice(temp_shipping)) for _ in range(count))
        res = [deformator.spoil(row) for row in rows]
        self.orders.extend(res)
        return res

    def generate_categories(self, count: int, deformator: CategoryDeformationInterface) -> List[ProductCategory]:
        rows = (ProductCategory() for _ in range(count))
        res = [deformator.spoil(row) for row in rows]
        self.categories.extend(res)
        return res

    def generate_customers(self, count: int, deformator: CustomerDeformationInterface) -> List[Customer]:
        rows = (Customer() for _ in range(count))
        res = [deformator.spoil(row) for row in rows]
        self.customers.extend(res)
        return res

    def generate_payments(self, count: int, deformator: PaymentDeformationInterface) -> List[Payment]:
        temp_orders = self.db_service.get_instances(count, Order)
        rows = (Payment(random.choice(temp_orders)) for _ in range(count))
        res = [deformator.spoil(row) for row in rows]
        self.payments.extend(res)
        return res

    def generate_products(self, count: int, deformator: ProductDeformationInterface) -> List[Product]:
        temp_manufactors = self.db_service.get_instances(count, Manufacturer)
        temp_categories = self.db_service.get_instances(5, ProductCategory)
        temp_discounts = self.db_service.get_instances(5, Discount)
        temp_packaging = self.db_service.get_instances(5, Packaging)
        temp_suppliers = self.db_service.get_instances(5, Supplier)
        rows = (Product(category=random.choice(temp_categories),
                        manufacturer=random.choice(temp_manufactors),
                        discount=random.choice(temp_discounts),
                        supplier=random.choice(temp_suppliers),
                        packaging=random.choice(temp_packaging)) for _ in range(count)
                )
        res = [deformator.spoil(row) for row in rows]
        self.products.extend(res)
        return res

    def generate_order_item(self, count: int, deformator: OrderItemDeformationInterface) -> List[OrderItem]:
        temp_products = self.db_service.get_instances(count, Product)
        temp_orders = self.db_service.get_instances(count, Order)
        rows = (OrderItem(random.choice(temp_products), random.choice(temp_orders)) for _ in range(count))
        res = [deformator.spoil(row) for row in rows]
        self.order_items.extend(res)
        return res

    def generate_comment(self, count: int, deformator: CommentDeformationInterface) -> List[Comment]:
        temp_products = self.db_service.get_instances(count, Product)
        temp_customers = self.db_service.get_instances(count, Customer)
        rows = (Comment(random.choice(temp_products), random.choice(temp_customers)) for _ in range(count))
        res = [deformator.spoil(row) for row in rows]
        self.comments.extend(res)
        return res

    def load_by_lst(self, lst: list) -> None:
        self.session.bulk_save_objects(lst)
        self.session.commit()

    def load_all(self) -> None:
        pass
