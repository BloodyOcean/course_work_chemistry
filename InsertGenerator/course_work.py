from datetime import datetime
from generators import *
from insert_manager import SQLServerInsertManager


CUSTOMERS_COUNT = 300
CATEGORIES = [
    'Medicines and Vitamins',
    'Personal Care',
    'Beauty and Skincare',
    'Baby and Childcare',
    'First Aid and Medical Supplies',
    'Digestive Health',
    'Pain Relief',
    'Allergy and Sinus',
    'Sexual Wellness',
    'Home Health Care'
]
MANUFACTURERS_COUNT = 30
PRODUCTS_COUNT = 500
ORDER_COUNT=1000
ORDER_ITEM_COUNT=4000
COMMENT_COUNT = 500
PAYMENT_COUNT = 950


#     id           INT PRIMARY KEY IDENTITY (1,1),
#     first_name   VARCHAR(50)  NOT NULL,
#     last_name    VARCHAR(50)  NOT NULL,
#     email        VARCHAR(50)  NOT NULL UNIQUE,
#     phone_number VARCHAR(15)  NOT NULL,
#     address      VARCHAR(150) NOT NULL,
#     city         VARCHAR(50)  NOT NULL,
#     state        VARCHAR(50)  NOT NULL,
#     zip_code     VARCHAR(10)  NOT NULL,
#     create_date  DATETIME DEFAULT CURRENT_TIMESTAMP,
#     update_date  DATETIME DEFAULT CURRENT_TIMESTAMP

def data_for_customers(table_name, db_name):
    generators = [ 
        NameGenerator(firstname=True, lastname=False),
        NameGenerator(firstname=False, lastname=True),
        EmailGenerator(domains=['lpnu.ua', 'gmail.com', 'ukr.net']),
        PhoneGenerator(),
        AddressGenerator(),
        SpecialGenerator(special_values=['Ukraine', 'Italy', 'France', 'Germany', 'China', 'USA']),
        SpecialGenerator(special_values=['Ukraine', 'Italy', 'France', 'Germany', 'China', 'USA']),
        NumberGenerator(start=100000, end=999999),
        DatetimeGenerator(datetime(2020, 1, 1), datetime(2022,1,1)),
        DatetimeGenerator(datetime(2023, 1, 2), datetime(2023,4,30))    
        ]
    manager = SQLServerInsertManager(generators, table_name, db_name)
    return manager.get_insert_query(CUSTOMERS_COUNT)


# id          INT PRIMARY KEY IDENTITY (1,1),
# name        VARCHAR(50) NOT NULL,
# create_date DATETIME DEFAULT CURRENT_TIMESTAMP,
# update_date DATETIME DEFAULT CURRENT_TIMESTAMP
def data_for_categories(table_name, db_name):
    generators = [
        SpecialGenerator(special_values=CATEGORIES),
        DatetimeGenerator(datetime(2020, 1, 1), datetime(2022, 1, 1)),
        DatetimeGenerator(datetime(2023, 1, 2), datetime(2023, 4, 30))
    ]
    manager = SQLServerInsertManager(generators, table_name, db_name)
    return manager.get_insert_query(len(CATEGORIES))


# id             INT PRIMARY KEY IDENTITY (1,1),
# name           VARCHAR(50)   NOT NULL,
# description    VARCHAR(1000) NOT NULL,
# contact_person VARCHAR(100)  NOT NULL,
# email          VARCHAR(50)   NOT NULL,
# create_date    DATETIME DEFAULT CURRENT_TIMESTAMP,
# update_date    DATETIME DEFAULT CURRENT_TIMESTAMP
def data_for_manufacturers(table_name, db_name):
    generators = [
        NameGenerator(firstname=False, lastname=True),
        LoremGenerator(20, 100),
        NameGenerator(firstname=True, lastname=True),
        EmailGenerator(domains=['gmail.com']),
        DatetimeGenerator(datetime(2020, 1, 1), datetime(2022, 1, 1)),
        DatetimeGenerator(datetime(2023, 1, 2), datetime(2023, 4, 30))
    ]
    manager = SQLServerInsertManager(generators, table_name, db_name)
    return manager.get_insert_query(MANUFACTURERS_COUNT)

# id              INT PRIMARY KEY IDENTITY (1,1),
# name            VARCHAR(100)   NOT NULL,
# description     VARCHAR(1000)  NOT NULL,
# price           DECIMAL(10, 2) NOT NULL,
# quantity        SMALLINT       NOT NULL,
# manufacturer_id INT            NOT NULL,
# category_id     INT            NOT NULL,
# create_date     DATETIME DEFAULT CURRENT_TIMESTAMP,
# update_date     DATETIME DEFAULT CURRENT_TIMESTAMP,
# FOREIGN KEY (category_id) REFERENCES product_categories (id),
# FOREIGN KEY (manufacturer_id) REFERENCES manufacturers (id)
def data_for_products(table_name, db_name):
    generators = [
        TemplatedGenerator([('medical product ', NumberGenerator(start=4563, queue_mode=True))]),
        LoremGenerator(min_words=20, max_words=100),
        FloatGenerator(start=12.50, end=700.00, brackets=False, precision=2),
        NumberGenerator(start=1000, end=20000),
        NumberGenerator(start=1, end=MANUFACTURERS_COUNT),
        NumberGenerator(start=1, end=len(CATEGORIES)),
        DatetimeGenerator(datetime(2020, 1, 1), datetime(2022, 1, 1)),
        DatetimeGenerator(datetime(2023, 1, 2), datetime(2023, 4, 30))
    ]
    manager = SQLServerInsertManager(generators, table_name, db_name)
    return manager.get_insert_query(PRODUCTS_COUNT)

# id          INT PRIMARY KEY IDENTITY (1,1),
# customer_id INT            NOT NULL,
# order_date  DATETIME                DEFAULT CURRENT_TIMESTAMP,
# status      VARCHAR(50)    NOT NULL DEFAULT 'Accepted',
# create_date DATETIME                DEFAULT CURRENT_TIMESTAMP,
# update_date DATETIME                DEFAULT CURRENT_TIMESTAMP,
# FOREIGN KEY (customer_id) REFERENCES customers (id)
def data_for_orders(table_name, db_name):
    generators = [
        NumberGenerator(start=1, end=CUSTOMERS_COUNT),
        DatetimeGenerator(datetime(2020, 1, 1), datetime(2023, 1, 1)),
        SpecialGenerator(special_values=['Accepted', 'InProgress', 'Done', 'Canceled']),
        DatetimeGenerator(datetime(2020, 1, 1), datetime(2022, 1, 1)),
        DatetimeGenerator(datetime(2023, 1, 2), datetime(2023, 4, 30))
    ]
    manager = SQLServerInsertManager(generators, table_name, db_name)
    return manager.get_insert_query(ORDER_COUNT)

# order_id   INT NOT NULL,
# product_id INT NOT NULL,
# quantity   INT NOT NULL,
# PRIMARY KEY (order_id, product_id),
# FOREIGN KEY (order_id) REFERENCES orders (id),
# FOREIGN KEY (product_id) REFERENCES products (id)
def data_for_order_items(table_name, db_name):

    part_size = ORDER_COUNT // (ORDER_ITEM_COUNT // ORDER_ITEM_COUNT);

    parts = []
    for i in range(ORDER_ITEM_COUNT // ORDER_COUNT):    
        generators = [
            NumberGenerator(start=i * part_size + 1, end=(i + 1) * part_size + 1, queue_mode=True, stay_for=4),
            NumberGenerator(start=1, end=PRODUCTS_COUNT, queue_mode=True),
            NumberGenerator(start=1, end=10)
        ]
        manager = SQLServerInsertManager(generators, table_name, db_name)
        # 1000 is the max number of records for an insert statement
        part = manager.get_insert_query(1000) 
        parts.append(part)
    return '\n'.join(parts)

# id           INT PRIMARY KEY IDENTITY (1,1),
# product_id   INT          NOT NULL,
# customer_id  INT          NOT NULL,
# comment_text VARCHAR(255) NOT NULL,
# rating       SMALLINT     NOT NULL,
# create_date  DATETIME DEFAULT CURRENT_TIMESTAMP,
# update_date  DATETIME DEFAULT CURRENT_TIMESTAMP,
# FOREIGN KEY (product_id) REFERENCES products (id),
# FOREIGN KEY (customer_id) REFERENCES customers (id)
def data_for_comment(table_name, db_name):
    generators = [
        NumberGenerator(start=1, end=PRODUCTS_COUNT),
        NumberGenerator(start=1, end=CUSTOMERS_COUNT),
        LoremGenerator(max_words=15, min_words=3),
        NumberGenerator(start=2, end=5),
        DatetimeGenerator(datetime(2020, 1, 1), datetime(2022, 1, 1)),
        DatetimeGenerator(datetime(2023, 1, 2), datetime(2023, 4, 30))
    ]
    manager = SQLServerInsertManager(generators, table_name, db_name)
    return manager.get_insert_query(COMMENT_COUNT)

# id             INT PRIMARY KEY IDENTITY (1,1),
# order_id       INT            NOT NULL,
# payment_date   DATETIME DEFAULT GETDATE(),
# payment_method VARCHAR(50)    NOT NULL,
# payment_amount DECIMAL(10, 2) NOT NULL,
# card_number    VARCHAR(20),
# card_holder    VARCHAR(100),
# card_exp_month INT,
# card_exp_year  INT,
# card_cvv       VARCHAR(10),
# FOREIGN KEY (order_id) REFERENCES orders (id)
def data_for_payments(table_name, db_name):
    generators = [
        NumberGenerator(start=1, end=ORDER_COUNT),
        DatetimeGenerator(datetime(2022, 1, 1), datetime(2023, 4, 1)),
        SpecialGenerator(special_values=['VISA', 'MASTERCARD', 'CASH']),
        FloatGenerator(start=12.50, end=700.00, brackets=False, precision=2),
        TemplatedGenerator([
            ['', NumberGenerator(start=10000000, end=99999999)],
            ['', NumberGenerator(start=10000000, end=99999999)]
        ]),
        NameGenerator(firstname=True, lastname=True),
        NumberGenerator(start=1, end=12),
        NumberGenerator(start=2025, end=2030),
        NumberGenerator(start=100, end=999)
    ]
    manager = SQLServerInsertManager(generators ,table_name, db_name)
    return manager.get_insert_query(PAYMENT_COUNT)


def fill(file_path, database_name):
    test_data = [
        data_for_customers('customers', database_name),
        data_for_categories('product_categories', database_name),
        data_for_manufacturers('manufacturers', database_name),
        data_for_products('products', database_name),
        data_for_orders('orders', database_name),
        data_for_order_items('order_items', database_name),
        data_for_comment('comments', database_name),
        data_for_payments('payments', database_name)
    ]
    script_code = '\n\n'.join(test_data);

    with open(file_path, 'w') as file:
        file.write(script_code)