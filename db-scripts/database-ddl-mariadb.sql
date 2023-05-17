CREATE DATABASE IF NOT EXISTS pharmacy_shop;

USE pharmacy_shop;

BEGIN;

CREATE TABLE IF NOT EXISTS discounts
(
    id               INT PRIMARY KEY AUTO_INCREMENT,
    title            VARCHAR(200)  NOT NULL,
    description      VARCHAR(1000) NOT NULL,
    start_date       TIMESTAMP     NOT NULL,
    end_date         TIMESTAMP     NOT NULL,
    discount_percent DECIMAL(5, 2) NOT NULL,
    create_date      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    update_date      TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS packaging
(
    id          INT PRIMARY KEY AUTO_INCREMENT,
    name        VARCHAR(50) NOT NULL,
    description VARCHAR(500),
    create_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    update_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS suppliers
(
    id           INT PRIMARY KEY AUTO_INCREMENT,
    name         VARCHAR(50)  NOT NULL,
    contact_name VARCHAR(50)  NOT NULL,
    phone_number VARCHAR(20)  NOT NULL,
    email        VARCHAR(50)  NOT NULL UNIQUE,
    address      VARCHAR(150) NOT NULL,
    create_date  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    update_date  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS customers
(
    id           INT PRIMARY KEY AUTO_INCREMENT,
    first_name   VARCHAR(50)  NOT NULL,
    last_name    VARCHAR(50)  NOT NULL,
    email        VARCHAR(50)  NOT NULL UNIQUE,
    phone_number VARCHAR(20)  NOT NULL,
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
    supplier_id     INT            NOT NULL,
    packaging_id    INT            NOT NULL,
    discount_id     INT            NOT NULL,
    category_id     INT            NOT NULL,
    create_date     TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    update_date     TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES product_categories (id),
    FOREIGN KEY (supplier_id) REFERENCES suppliers (id),
    FOREIGN KEY (packaging_id) REFERENCES packaging (id),
    FOREIGN KEY (discount_id) REFERENCES discounts (id),
    FOREIGN KEY (manufacturer_id) REFERENCES manufacturers (id)
);

CREATE TABLE IF NOT EXISTS shipping
(
    id               INT PRIMARY KEY AUTO_INCREMENT,
    delivery_date    TIMESTAMP    NOT NULL,
    carrier          VARCHAR(50)  NOT NULL,
    receiver         VARCHAR(100) NOT NULL,
    tracking_number  VARCHAR(50)  NOT NULL,
    shipping_address VARCHAR(150) NOT NULL,
    shipping_city    VARCHAR(50)  NOT NULL,
    shipping_state   VARCHAR(50)  NOT NULL,
    shipping_zip     VARCHAR(10)  NOT NULL,
    create_date      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    update_date      TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS `position`
(
    id         INT PRIMARY KEY AUTO_INCREMENT,
    title      VARCHAR(200)  NOT NULL,
    salary     DECIMAL(10, 2) NOT NULL,
    create_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    update_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS employee
(
    id            INT PRIMARY KEY AUTO_INCREMENT,
    name          VARCHAR(100) NOT NULL,
    position_id   INT          NOT NULL,
    email         VARCHAR(100) NOT NULL,
    phone_number  VARCHAR(20)  NOT NULL,
    address       VARCHAR(200) NOT NULL,
    date_of_birth DATE         NOT NULL,
    hire_date     DATE         NOT NULL,
    create_date    TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    update_date    TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (position_id) REFERENCES `position` (id)
);

CREATE TABLE IF NOT EXISTS work_schedule
(
    id          INT PRIMARY KEY AUTO_INCREMENT,
    employee_id INT  NOT NULL,
    start_date  DATE NOT NULL,
    end_date    DATE NOT NULL,
    start_time  TIME NOT NULL,
    end_time    TIME NOT NULL,
    create_date  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    update_date  TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (employee_id) REFERENCES employee (id)
);

CREATE TABLE IF NOT EXISTS orders
(
    id          INT PRIMARY KEY AUTO_INCREMENT,
    employee_id INT                                                 NOT NULL,
    shipping_id INT,
    customer_id INT                                                 NOT NULL,
    order_date  TIMESTAMP                                                    DEFAULT CURRENT_TIMESTAMP,
    status      ENUM ('Accepted', 'InProgress', 'Done', 'Canceled') NOT NULL DEFAULT 'Accepted',
    create_date TIMESTAMP                                                    DEFAULT CURRENT_TIMESTAMP,
    update_date TIMESTAMP                                                    DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers (id),
    FOREIGN KEY (employee_id) REFERENCES employee (id),
    FOREIGN KEY (shipping_id) REFERENCES shipping (id)
);

CREATE TABLE IF NOT EXISTS order_items
(
    order_id    INT NOT NULL,
    product_id  INT NOT NULL,
    quantity    INT NOT NULL,
    create_date DATETIME  DEFAULT CURRENT_TIMESTAMP,
    update_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
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
    create_date    DATETIME  DEFAULT CURRENT_TIMESTAMP,
    update_date    TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (order_id) REFERENCES orders (id)
);

COMMIT;
