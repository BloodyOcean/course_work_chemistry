use pharmacy_shop;

-- Insert test data into discounts table
INSERT INTO discounts (title, description, start_date, end_date, discount_percent)
VALUES ('Spring Sale', 'Discount for spring season', '2022-03-20', '2022-04-20', 10.00),
('Summer Sale', 'Discount for summer season', '2022-06-20', '2022-07-20', 15.00);

-- Insert test data into packaging table
INSERT INTO packaging (name, description)
VALUES ('Bottle', 'Packaging in bottle'),
('Box', 'Packaging in box');

-- Insert test data into suppliers table
INSERT INTO suppliers (name, contact_name, phone_number, email, address)
VALUES ('ABC Inc.', 'John Doe', '555-1234', 'johndoe@abcinc.com', '123 Main St, Anytown USA'),
('XYZ Corp.', 'Jane Smith', '555-5678', 'janesmith@xyzcorp.com', '456 Elm St, Anytown USA');

-- Insert test data into customers table
INSERT INTO customers (first_name, last_name, email, phone_number, address, city, state, zip_code)
VALUES ('John', 'Doe', 'johndoe@example.com', '555-1234', '123 Main St, Anytown USA', 'Anytown', 'CA', '12345'),
('Jane', 'Smith', 'janesmith@example.com', '555-5678', '456 Elm St, Anytown USA', 'Anytown', 'CA', '12345');

-- Insert test data into product_categories table
INSERT INTO product_categories (name)
VALUES ('Medicines'),
('Supplements');

-- Insert test data into manufacturers table
INSERT INTO manufacturers (name, description, contact_person, email)
VALUES ('ABC Manufacturing', 'Manufacturer of medicines and supplements', 'John Smith', 'johnsmith@abcmfg.com'),
('XYZ Pharma', 'Pharmaceutical company specializing in medicines', 'Jane Doe', 'janedoe@xyzpharma.com');

-- Insert test data into products table
INSERT INTO products (name, description, price, quantity, manufacturer_id, supplier_id, packaging_id, discount_id, category_id)
VALUES ('Acetaminophen', 'Pain reliever and fever reducer', 5.99, 100, 1, 1, 1, 1, 1),
('Vitamin C', 'Vitamin supplement', 7.99, 50, 2, 2, 2, 2, 2);

-- Insert test data into payments table
INSERT INTO shipping (delivery_date, carrier, receiver, tracking_number, shipping_address, shipping_city,
                          shipping_state, shipping_zip)
VALUES ('2023-05-15 10:00:00', 'FedEx', 'John Smith', '123456789', '123 Main St', 'Anytown', 'CA', '12345');

-- Insert test data into orders table
INSERT INTO orders (customer_id, order_date, status)
VALUES (1, 1, '2022-05-01', 'InProgress'),
(1, 2, '2022-05-02', 'InProgress');

-- Insert test data into order_items table
INSERT INTO order_items (order_id, product_id, quantity)
VALUES (1, 1, 2),
(2, 2, 1);

-- Insert test data into comments table
INSERT INTO comments (product_id, customer_id, comment_text, rating)
VALUES (1, 1, 'Great product, highly recommend!', 5),
(2, 2, 'Product arrived damaged, but was quickly replaced by customer service.', 3);

-- Insert test data into payments table
INSERT INTO payments (order_id, payment_date, payment_method, payment_amount, card_number, card_holder)
VALUES (1, '2022-05-05', 'Credit Card', 11.98, '5791245701345802', 'Ivan');
