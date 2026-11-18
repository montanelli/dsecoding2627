-- database available at
-- (large version) https://contents.islab.di.unimi.it/datasets/instacart.sql.zip
-- (small version) https://contents.islab.di.unimi.it/datasets/instacart_small.sql.zip

CREATE TABLE departments(
  department_id INTEGER PRIMARY KEY,
  department VARCHAR(15)
);

CREATE TABLE aisles(
  aisle_id INTEGER PRIMARY KEY,
  aisle VARCHAR(50)
);

CREATE TABLE products(
  product_id INTEGER PRIMARY KEY,
  product_name VARCHAR(300),
  aisle_id INTEGER REFERENCES aisles(aisle_id) ,
  department_id INTEGER REFERENCES departments(department_id) on delete cascade 
);

CREATE TABLE orders(
  order_id INTEGER PRIMARY KEY,
  user_id INTEGER,
  eval_set VARCHAR(5),
  order_number INTEGER,
  order_dow INTEGER,
  order_hour_of_day INTEGER,
  days_since_prior_order REAL
);

CREATE TABLE order_products(
  order_id INTEGER REFERENCES orders(order_id),
  product_id INTEGER REFERENCES products(product_id),
  add_to_cart_order INTEGER,
  reordered INTEGER,
  PRIMARY KEY(order_id, product_id)
);

-- tick the statement that cannot generate an error
A. DELETE FROM aisles WHERE aisle_id = 5; -- can generate error
B. DELETE FROM departments WHERE department_id = 8; -- cannot generate errors (cascade)
C. UPDATE aisles SET aisle_id = 4 WHERE aisle_id = 5; -- can generate error
D. UPDATE departments SET department_id = 7 WHERE department_id = 8; -- can generate error
E. UPDATE departments SET department = 'data science' WHERE department_id = 8; -- cannot generate errors

-- tick the statement that generates an error
A. DELETE FROM order_products WHERE order_id = 5; -- no error
B. DELETE FROM products WHERE product_id = 8292; -- possible error
C. DELETE FROM orders WHERE order_id = 4848; -- possible error
D. DELETE FROM order_products WHERE product_id = 0494; -- no error

-- consider to use the cascade policy on order_products.order_id 
A. DELETE FROM order_products WHERE order_id = 5; -- no error
B. DELETE FROM products WHERE product_id = 8292; -- possible error
C. DELETE FROM orders WHERE order_id = 4848; -- no error ** 
D. DELETE FROM order_products WHERE product_id = 0494; -- no error


-- Retrieve the order_id, product_id, and the product_name for each order submitted on Monday (order_dow = 1)
select orders.order_id, products.product_id, product_name
from orders inner join order_products on orders.order_id = order_products.order_id inner join products on order_products.product_id = products.product_id 
where order_dow = 1;

-- Retrieve the order_id, product_id, and the name of products that are added as first in the cart of each order (add_to_cart_order = 1)


-- Retrieve the order_id, product_id, and the product_name for each order submitted between the hours 15 and 17 
select orders.order_id, products.product_id, product_name
from orders inner join order_products on orders.order_id = order_products.order_id inner join products on order_products.product_id = products.product_id 
where order_hour_of_day between 15 and 17
-- where order_hour_of_day >= 15 and order_hour_of_day <= 17;

-- Retrieve the id of orders where the first product added to the cart is the same as the one in the order_id = 2411567
-- explain analyze
select order_id 
from order_products 
where add_to_cart_order = 1 and product_id = (
select product_id
from order_products 
where order_id = 2411567 and add_to_cart_order = 1)

-- alternative solution 
-- explain provides an estimation of execution time of a statement 
-- explain analyze
select op1.order_id 
from order_products op1, order_products op2
where op1.add_to_cart_order = 1 and op1.product_id = op2.product_id 
    and op2.add_to_cart_order = 1 and op2.order_id = 2411567


-- Retrieve the name of products that are ordered on Monday (order_dow = 1) from the coffee aisle. Sort the result by the product name


-- Retrieve the id of products that are never ordered on Tuesday (order_dow = 2)
-- this solution is wrong:
select product_id
from orders o inner join order_products op on o.order_id = op.order_id 
where order_dow <> 2

order_id | product_id | dow 
001     002     2
002     003     3
001     003     2

select product_id
from products p 
where product_id not in (
select distinct product_id 
from orders o inner join order_products op on o.order_id = op.order_id 
where order_dow = 2)

-- there is also a solution with left join 


-- Retrieve the id of products from the coffee aisle that are never ordered on Tuesay (order_dow = 2)


-- Retrieve the id of users that submitted orders on BOTH Monday (order_dow = 1) and Tuesday (order_dow = 2). 


-- Retrieve the id of products that are ordered on Saturday and Sunday (order_dow = 6 and order_dow = 7)


-- Retrieve the average number of products for each order
-- HINT: create a view with product counts for each order as intermediate step  


-- For each department, retrieve the number of ordered products. Show the department_name in the result. Sort the result by the number of products in descending order
select d.department_id, d.department, count(p.product_id) as p_count, count(*)
from departments d  inner join products p on d.department_id = p.department_id inner join order_products op on p.product_id = op.product_id 
group by d.department_id, d.department
order by p_count desc 

-- Refine the previous query by returning only the departments with more than 10K of ordered products
select d.department_id, d.department, count(p.product_id) as p_count, count(*)
from departments d  inner join products p on d.department_id = p.department_id inner join order_products op on p.product_id = op.product_id 
group by d.department_id, d.department
having count(p.product_id) > 10000
order by p_count desc 


-- For each product in the coffee aisle, retrieve the number of orders submitted on Tuesday (order_dow = 2). Include in the result the products that are never ordered (if they exist)
SELECT products.product_id, product_name, count(orders.order_id) 
FROM aisles INNER JOIN products ON products.aisle_id = aisles.aisle_id LEFT JOIN order_products ON order_products.product_id = products.product_id
LEFT JOIN orders ON (order_products.order_id = orders.order_id AND order_dow = 2) 
WHERE aisles.aisle = 'coffee'
GROUP BY products.product_id, product_name;


