from generators import *
from insert_manager import InsertManager


def data_for_customers():
    generators = [
        NameGenerator(firstname=True, lastname=True, brackets=True),
        NumberGenerator(start=18, end=105),
        #DatetimeGenerator(start='2017-01-01 00:00:00.000', end='2022-12-28 24:60:60.1000'),
        SpecialGenerator(special_values=['Ukraine', 'Italy', 'France', 'Germany', 'China', 'USA']),
        NumberGenerator(start=0, end=1),
        EmailGenerator(domains=['lpnu.ua', 'gmail.com', 'ukr.net']),
        HashGenerator(length=40, brackets=True),
        TemplatedGenerator([
            ['C:/UsersData/Pictures/', HashGenerator(length=15)],
            ['', SpecialGenerator(special_values=['.pdf', '.img'], brackets=False)]
        ]),
        NumberGenerator(start=0, end=0)
    ]
    manager = InsertManager(table_name='Customer', db_name='Variant3', generators=generators)
    return manager.get_insert_query(50)


def data_for_products():
    generators = [
        TemplatedGenerator([('medical product ', NumberGenerator(start=5555, queue_mode=True))]),
        LoremGenerator(min_words=15, max_words=25),
        SpecialGenerator(special_values=['medicines and vitamins', 'for children', 'beauty and care', 'daily hygiene', 'medical equipment']),
        FloatGenerator(start=12.50, end=700.00, brackets=False, precision=2),
        DatetimeGenerator(start='2021-01-01', end='2022-12-28'),
        DatetimeGenerator(start='2023-01-01', end='2024-12-28'),
        NumberGenerator(start=1000, end=20000),
        TemplatedGenerator([
            ['C:/ProductData/Pictures/', HashGenerator(length=15)],
            ['', SpecialGenerator(special_values=['.pdf', '.img'], brackets=False)]
        ]),
        NumberGenerator(start=1, end=50)
    ]
    manager = InsertManager(table_name='Product', db_name='Variant3', generators=generators)
    return manager.get_insert_query(100)


def data_for_producer():
    generators = [
        TemplatedGenerator([
           ['', NameGenerator(firstname=False, lastname=True)],
           [' ', NameGenerator(firstname=False, lastname=True)]
        ]),
        SpecialGenerator(special_values=['Ukraine', 'Italy', 'France', 'Germany', 'China', 'USA']),
        LoremGenerator(max_words=20),
    ]
    manager = InsertManager(table_name='Producer', db_name='Variant3', generators=generators)
    return manager.get_insert_query(50)


def data_for_order():
    generators = [
        DatetimeGenerator(start='2017-01-01 00:00:00.000', end='2022-12-28 23:59:59.999'),
        NumberGenerator(start=1, end=3),
        NumberGenerator(start=1, end=50)
    ]
    manager = InsertManager(table_name='Order', db_name='Variant3', generators=generators)
    return manager.get_insert_query(50)


def data_for_bind_product_to_customer():
    generators = [
        NumberGenerator(start=1, end=50),
        NumberGenerator(start=1, end=100),
        NumberGenerator(start=1, end=15)
    ]
    manager = InsertManager(table_name='BindProductToCustomer', db_name='Variant3', generators=generators)
    return manager.get_insert_query(50)


def data_for_bind_product_to_order():
    generators = [
        NumberGenerator(start=1, end=50, queue_mode=True),
        NumberGenerator(start=1, end=100),
        NumberGenerator(start=1, end=15)
    ]
    manager = InsertManager(table_name='BindProductToOrder', db_name='Variant3', generators=generators)
    return manager.get_insert_query(120)


def data_for_comment():
    generators = [
        LoremGenerator(max_words=15, min_words=3),
        NullGenerator(),
        NumberGenerator(start=1, end=50),
        NumberGenerator(start=1, end=100)
    ]
    manager = InsertManager(table_name='Comment', db_name='Variant3', generators=generators)
    return manager.get_insert_query(50)


def fill(file_path):
    test_data = [
        data_for_producer(),
        data_for_products(),
        data_for_customers(),
        data_for_order(),
        data_for_bind_product_to_order(),
        data_for_bind_product_to_customer(),
        data_for_comment()
    ]
    res = ''
    for td in test_data:
        res += td + '\n\n'

    with open(file_path, 'w') as file:
        file.write(res)