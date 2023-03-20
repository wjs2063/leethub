# Write your MySQL query statement below

SELECT p.product_id, "store1" as "store", p.store1 as "price"
FROM Products p WHERE p.store1 is not null 
UNION
SELECT p.product_id, "store2" as "store", p.store2 as "price"
FROM Products p WHERE p.store2 is not null
UNION 
SELECT p.product_id, "store3" as "store", p.store3 as "price"
FROM Products p WHERE p.store3 is not null
