import argparse

from deformation import *
from lib.config_helper import ConfigHelper
from lib.models_generator import *
from models.models import DbHelper


def main():

    cfg_helper = ConfigHelper(path='configs/config.example.ini')
    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    db_helper = DbHelper(cfg_helper.get('db', 'connection_string'))
    db_helper.connect()
    db_helper.create_tables()

    generator = ModelsGenerator(db_helper.session)

    # Deformations
    customers_deformator = CustomerDeformation(0.0)
    shipping_deformator = ShippingDeformation(0.0)
    discount_deformator = DiscountDeformation(0.0)
    product_category_deformator = CategoryDeformation(0.0)
    manufacturer_deformator = ManufacturerDeformation(0.0)
    supplier_deformator = SupplierDeformation(0.0)
    packaging_deformator = PackagingDeformation(0.0)
    comments_deformator = CommentDeformation(0.0)
    payments_deformator = PaymentDeformation(0.0)
    order_items_deformator = OrderItemDeformation(0.0)
    products_deformator = ProductDeformation(0.0)
    orders_deformator = OrderDeformation(0.0)

    # Generate zero-level object
    generator.generate_customers(250, customers_deformator)
    generator.generate_shipping(250, shipping_deformator)
    generator.generate_discount(40, discount_deformator)
    generator.generate_categories(35, product_category_deformator)
    generator.generate_manufacturer(75, manufacturer_deformator)
    generator.generate_supplier(115, supplier_deformator)
    generator.generate_packaging(33, packaging_deformator)
    generator.load_by_lst(generator.customers)
    generator.load_by_lst(generator.shipping)
    generator.load_by_lst(generator.discounts)
    generator.load_by_lst(generator.categories)
    generator.load_by_lst(generator.manufactors)
    generator.load_by_lst(generator.suppliers)
    generator.load_by_lst(generator.packaging)

    # Generate first-level object
    generator.generate_products(50, products_deformator)
    generator.generate_orders(100, orders_deformator)
    generator.load_by_lst(generator.products)
    generator.load_by_lst(generator.orders)

    # Generate second-level object
    generator.generate_comment(60, comments_deformator)
    generator.generate_payments(99, payments_deformator)
    generator.generate_order_item(55, order_items_deformator)
    generator.load_by_lst(generator.comments)
    generator.load_by_lst(generator.payments)
    generator.load_by_lst(generator.order_items)

    db_helper.session.close()


def get_db_session():
    cfg_helper = ConfigHelper(path='configs/config.example.ini')
    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    db_helper = DbHelper(cfg_helper.get('db', 'connection_string'))
    db_helper.connect()
    db_helper.create_tables()
    
    return db_helper.session


if __name__ == '__main__':
    main()
