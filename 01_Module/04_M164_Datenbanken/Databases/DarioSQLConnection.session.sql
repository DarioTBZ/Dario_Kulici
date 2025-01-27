use pizza_express;

SELECT firstname, lastname, address FROM customer;

SELECT DISTINCT firstname FROM customer;

SELECT * FROM order_entry ORDER BY ordered_at DESC;

SELECT price FROM product as sqrt;