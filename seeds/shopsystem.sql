DROP TABLE if exists products cascade;
DROP sequence IF EXISTS products_id_seq;

DROP TABLE IF exists orders cascade;
DROP sequence if exists orders_id_seq;

DROP TABLE IF EXISTS orders_products;
DROP SEQUENCE IF EXISTS orders_products_id_seq;

CREATE sequence if not exists products_id_seq;
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    unit_price DECIMAL(5, 2),
    quantity int
);

CREATE SEQUENCE IF NOT EXISTS orders_id_seq;
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    customer_name VARCHAR(255),
    order_date DATE
);

CREATE SEQUENCE IF NOT EXISTS orders_products_id_seq;
CREATE TABLE orders_products(
    id SERIAL PRIMARY KEY,
    order_id int,
    product_id int,
    constraint fk_order foreign key(order_id) references orders(id) on delete cascade,
    constraint fk_product foreign key(product_id) references products(id) on delete cascade
);

INSERT INTO products (name,unit_price,quantity) VALUES ('Baked Beans',00.10,50);
INSERT INTO products (name,unit_price,quantity) VALUES ('Sweetcorn',00.25,40);
INSERT INTO products (name,unit_price,quantity) VALUES ('Kidney Beans',00.30,25);
INSERT INTO products (name,unit_price,quantity) VALUES ('Diamonds',999.99,1);

INSERT INTO orders (customer_name,order_date) VALUES ('John Smith','2023-05-01');
INSERT INTO orders (customer_name,order_date) VALUES ('Ned Stark','1356-01-06');

INSERT INTO orders_products (order_id,product_id) VALUES (1,1);
INSERT INTO orders_products (order_id,product_id) VALUES (1,2);
INSERT INTO orders_products (order_id,product_id) VALUES (2,4);
INSERT INTO orders_products (order_id,product_id) VALUES (2,3);
INSERT INTO orders_products (order_id,product_id) VALUES (2,3);


