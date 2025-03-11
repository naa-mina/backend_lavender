/*
1. write SQL to create Product table with columns id, product_name, category, price, and insert 5 records into it
2. Write SQL to create Sales table with columns id, product_id, quantity_sold, sale_date, total_price and insert 5 records into it
3. Write SQL to retrieve all data from the product 
4. Write SQL to retrieve product_name and price from product table
5. Write SQL to retrieve only 2 records from sales table
6. Write SQL to retrieve sales that have total_price more than 100
7. Write SQL to retrieve products that have the same category
8. Write SQL to get the total number of products
9. Write SQL to get sum of total sales
10. Write SQL to get avg of product price
*/



--query to create table
CREATE TABLE product (
    id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    category TEXT NOT NULL,
    price NUMERIC NOT NULL
    );
--query to add items to table
INSERT INTO product (id, product_name,category, price)
VALUES
    (1, 'Egg', 'diary', 5.99),
    (2, 'Milk','diary', 10.50),
    (3, 'Apple', 'fruit', 2.30),
    (4, 'Banana', 'fruit', 1.50),
    (5, 'Cheese', 'diary', 8.30)

CREATE TABLE sales (
    id INTEGER PRIMARY KEY,
    product_id INT, 
    CONSTRAINT fk_product_sales FOREIGN KEY (product_id) REFERENCES product(id),
    quantity_sold INT NOT NULL,
    sale_date DATE NOT NULL,
    total_price NUMERIC NOT NULL
    );

INSERT INTO sales (id, product_id, sale_date,quantity_sold,total_price)
VALUES
    (1, 1, '2025-03-06',20, 119.80),
    (2, 4, '2025-03-06',5, 6.00),
    (3, 2, '2025-03-07',1, 10.50),
    (4, 5, '2025-03-07',3, 24.90),
    (5, 3, '2025-03-07',4, 9.20)

--queries to view info in table

SELECT * FROM product
SELECT product_name, price FROM product

SELECT * FROM sales LIMIT 2

SELECT * FROM sales WHERE total_price > 100
SELECT * FROM product WHERE category = 'fruit'

SELECT COUNT(*) AS total_product FROM product

SELECT SUM(total_price) AS total_sales from sales

SELECT AVG(price) AS average_price FROM product