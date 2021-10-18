


CREATE TABLE IF NOT EXISTS flowerapi_products (
  product_id serial primary key,
  product_name varchar(250) NOT NULL,
  product_stock INT,
  product_price FLOAT,
  product_popularity INT,
  product_category varchar(250) NOT NULL
  
);

CREATE TABLE IF NOT EXISTS flowerapi_orders (
  order_id serial primary key,
  order_time timestamp DEFAULT(CURRENT_TIMESTAMP),
  order_product varchar(250) NOT NULL,
  order_quantity INT,
  order_subtotal FLOAT,
  order_total FLOAT
  
);






