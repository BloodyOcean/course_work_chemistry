CREATE DATABASE pharmacy_shop;
GO

USE pharmacy_shop;
GO

IF NOT EXISTS(SELECT *
              FROM sys.tables
              WHERE name = 'customers')
CREATE TABLE customers
(
    id           INT PRIMARY KEY IDENTITY (1,1),
    first_name   VARCHAR(50)  NOT NULL,
    last_name    VARCHAR(50)  NOT NULL,
    email        VARCHAR(50)  NOT NULL UNIQUE,
    phone_number VARCHAR(15)  NOT NULL,
    address      VARCHAR(150) NOT NULL,
    city         VARCHAR(50)  NOT NULL,
    state        VARCHAR(50)  NOT NULL,
    zip_code     VARCHAR(10)  NOT NULL,
    create_date  DATETIME DEFAULT CURRENT_TIMESTAMP,
    update_date  DATETIME DEFAULT CURRENT_TIMESTAMP
);

IF NOT EXISTS(SELECT *
              FROM sys.tables
              WHERE name = 'product_categories')
CREATE TABLE product_categories
(
    id          INT PRIMARY KEY IDENTITY (1,1),
    name        VARCHAR(50) NOT NULL,
    create_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    update_date DATETIME DEFAULT CURRENT_TIMESTAMP
);

IF NOT EXISTS(SELECT *
              FROM sys.tables
              WHERE name = 'manufacturers')
CREATE TABLE manufacturers
(
    id             INT PRIMARY KEY IDENTITY (1,1),
    name           VARCHAR(50)   NOT NULL,
    description    VARCHAR(1000) NOT NULL,
    contact_person VARCHAR(100)  NOT NULL,
    email          VARCHAR(50)   NOT NULL,
    create_date    DATETIME DEFAULT CURRENT_TIMESTAMP,
    update_date    DATETIME DEFAULT CURRENT_TIMESTAMP
);

IF NOT EXISTS(SELECT *
              FROM sys.tables
              WHERE name = 'products')
CREATE TABLE products
(
    id              INT PRIMARY KEY IDENTITY (1,1),
    name            VARCHAR(100)   NOT NULL,
    description     VARCHAR(1000)  NOT NULL,
    price           DECIMAL(10, 2) NOT NULL,
    quantity        SMALLINT       NOT NULL,
    manufacturer_id INT            NOT NULL,
    category_id     INT            NOT NULL,
    create_date     DATETIME DEFAULT CURRENT_TIMESTAMP,
    update_date     DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES product_categories (id),
    FOREIGN KEY (manufacturer_id) REFERENCES manufacturers (id)
);

IF NOT EXISTS(SELECT *
              FROM sys.tables
              WHERE name = 'orders')
CREATE TABLE orders
(
    id          INT PRIMARY KEY IDENTITY (1,1),
    customer_id INT            NOT NULL,
    order_date  DATETIME                DEFAULT CURRENT_TIMESTAMP,
    status      VARCHAR(50)    NOT NULL DEFAULT 'Accepted',
    create_date DATETIME                DEFAULT CURRENT_TIMESTAMP,
    update_date DATETIME                DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers (id)
);

IF NOT EXISTS(SELECT *
              FROM sys.tables
              WHERE name = 'order_items')
CREATE TABLE order_items
(
    order_id   INT NOT NULL,
    product_id INT NOT NULL,
    quantity   INT NOT NULL,
    PRIMARY KEY (order_id, product_id),
    FOREIGN KEY (order_id) REFERENCES orders (id),
    FOREIGN KEY (product_id) REFERENCES products (id)
);

IF NOT EXISTS(SELECT *
              FROM sys.tables
              WHERE name = 'comments')
CREATE TABLE comments
(
    id           INT PRIMARY KEY IDENTITY (1,1),
    product_id   INT          NOT NULL,
    customer_id  INT          NOT NULL,
    comment_text VARCHAR(255) NOT NULL,
    rating       SMALLINT     NOT NULL,
    create_date  DATETIME DEFAULT CURRENT_TIMESTAMP,
    update_date  DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products (id),
    FOREIGN KEY (customer_id) REFERENCES customers (id)
);

IF NOT EXISTS(SELECT *
              FROM sys.tables
              WHERE name = 'payments')
CREATE TABLE payments
(
    id             INT PRIMARY KEY IDENTITY (1,1),
    order_id       INT            NOT NULL,
    payment_date   DATETIME DEFAULT GETDATE(),
    payment_method VARCHAR(50)    NOT NULL,
    payment_amount DECIMAL(10, 2) NOT NULL,
    card_number    VARCHAR(20),
    card_holder    VARCHAR(100),
    card_exp_month INT,
    card_exp_year  INT,
    card_cvv       VARCHAR(10),
    FOREIGN KEY (order_id) REFERENCES orders (id)
);
