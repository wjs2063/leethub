# Write your MySQL query statement below
SELECT DISTINCT(ss.product_id),p.product_name
FROM Sales as ss left join Product p on ss.product_id = p.product_id
WHERE ss.product_id not in (SELECT s.product_id
FROM Sales s left join Product p on s.product_id = p.product_id
WHERE DATE_FORMAT("2019-01-01","%Y-%m-%d") > s.sale_date or s.sale_date > DATE_FORMAT("2019-03-31","%Y-%m-%d"))
