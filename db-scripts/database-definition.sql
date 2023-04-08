CREATE DATABASE IF NOT EXISTS pharmacy_shop;

USE pharmacy_shop;

CREATE TABLE IF NOT EXISTS customers
(
    id           INT PRIMARY KEY AUTO_INCREMENT,
    first_name   VARCHAR(50)  NOT NULL,
    last_name    VARCHAR(50)  NOT NULL,
    email        VARCHAR(50)  NOT NULL UNIQUE,
    phone_number VARCHAR(15)  NOT NULL,
    address      VARCHAR(150) NOT NULL,
    city         VARCHAR(50)  NOT NULL,
    state        VARCHAR(50)  NOT NULL,
    zip_code     VARCHAR(10)  NOT NULL,
    create_date  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    update_date  TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS product_categories
(
    id          INT PRIMARY KEY AUTO_INCREMENT,
    name        VARCHAR(50) NOT NULL,
    create_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    update_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS manufacturers
(
    id             INT PRIMARY KEY AUTO_INCREMENT,
    name           VARCHAR(50)   NOT NULL,
    description    VARCHAR(1000) NOT NULL,
    contact_person VARCHAR(100)  NOT NULL,
    # contact person name
    email          VARCHAR(50)   NOT NULL,
    create_date    TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    update_date    TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS products
(
    id              INT PRIMARY KEY AUTO_INCREMENT,
    name            VARCHAR(100)   NOT NULL,
    description     VARCHAR(1000)  NOT NULL,
    price           DECIMAL(10, 2) NOT NULL,
    quantity        SMALLINT       NOT NULL,
    manufacturer_id INT            NOT NULL,
    category_id     INT            NOT NULL,
    create_date     TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    update_date     TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES product_categories (id),
    FOREIGN KEY (manufacturer_id) REFERENCES manufacturers (id)
);

CREATE TABLE IF NOT EXISTS orders
(
    id          INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT                                                 NOT NULL,
    order_date  TIMESTAMP                                                    DEFAULT CURRENT_TIMESTAMP,
    total       DECIMAL(10, 2)                                      NOT NULL,
    status      ENUM ('Accepted', 'InProgress', 'Done', 'Canceled') NOT NULL DEFAULT 'Accepted',
    create_date TIMESTAMP                                                    DEFAULT CURRENT_TIMESTAMP,
    update_date TIMESTAMP                                                    DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers (id)
);

CREATE TABLE IF NOT EXISTS order_items
(
    order_id   INT NOT NULL,
    product_id INT NOT NULL,
    quantity   INT NOT NULL,
    PRIMARY KEY (order_id, product_id),
    FOREIGN KEY (order_id) REFERENCES orders (id),
    FOREIGN KEY (product_id) REFERENCES products (id)
);

CREATE TABLE IF NOT EXISTS comments
(
    id           INT PRIMARY KEY AUTO_INCREMENT,
    product_id   INT          NOT NULL,
    customer_id  INT          NOT NULL,
    comment_text VARCHAR(255) NOT NULL,
    rating       SMALLINT     NOT NULL,
    # [1; 10] 
    create_date  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    update_date  TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products (id),
    FOREIGN KEY (customer_id) REFERENCES customers (id)
);

CREATE TABLE IF NOT EXISTS payments
(
    id             INT PRIMARY KEY AUTO_INCREMENT,
    order_id       INT            NOT NULL,
    payment_date   TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    payment_method VARCHAR(50)    NOT NULL,
    payment_amount DECIMAL(10, 2) NOT NULL,
    card_number    VARCHAR(20),
    card_holder    VARCHAR(100),
    card_exp_month INT,
    card_exp_year  INT,
    card_cvv       VARCHAR(10),
    FOREIGN KEY (order_id) REFERENCES orders (id)
);