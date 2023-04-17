from variant3 import data_for_producer, data_for_products, data_for_customers, \
    data_for_order, data_for_bind_product_to_order, data_for_bind_product_to_customer, \
    data_for_comment, fill
from generators import *
from insert_manager import InsertManager

def data_for_seller():
    generators = [
        NameGenerator(firstname=False, lastname=True, brackets=True),
        SpecialGenerator(special_values=['Lviv', 'Kiyv', 'Kharkiv', 'Odesa', 'Sumy', 'Rivne', 'Vinnytsia']),
        FloatGenerator(start=0.02, end=0.40, round_to=3)
    ]
    manager = InsertManager(
        table_name='Seller',
        db_name='Purchase-sale_operations_Ivasiv',
        generators=generators,
        ending='GO'
    )
    return manager.get_insert_query(50)

def data_for_customer():
    generators = [
        NameGenerator(firstname=True, lastname=True, brackets=True),
        SpecialGenerator(special_values=['Lviv', 'Kiyv', 'Kharkiv', 'Odesa', 'Sumy', 'Rivne', 'Vinnytsia']),
        FloatGenerator(start=0.2, end=1.0, round_to=2),
        NumberGenerator(start=1, end=50)
    ]
    manager = InsertManager(
        table_name='Customer',
        db_name='Purchase-sale_operations_Ivasiv',
        generators=generators,
        ending='GO'
    )
    return manager.get_insert_query(50)


def data_for_order():
    generators = [
        FloatGenerator(start=50.0, end=5000.0, round_to=2),
        DatetimeGenerator(start='2020-01-01 00:00:00.000', end='2022-12-28 23:59:59.999'),
        NumberGenerator(start=1, end=50),
        NumberGenerator(start=1, end=50)
    ]
    manager = InsertManager(
        table_name='Order',
        db_name='Purchase-sale_operations_Ivasiv',
        generators=generators,
        ending='GO'
    )
    return manager.get_insert_query(50)


def fill_ps(file_path):
    test_data = [
        data_for_seller(),
        data_for_customer(),
        data_for_order()
    ]
    res = ''
    for td in test_data:
        res += td + '\n\n'

    with open(file_path, 'w') as file:
        file.write(res)


fill_ps(r'C:\Users\Oleh\Desktop\Studying\DB\LAB_2\SQL_sell-purchase_fill.sql')










