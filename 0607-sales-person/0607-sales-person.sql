# Write your MySQL query statement below
SELECT s.name
FROM SalesPerson s
WHERE s.name not in (
SELECT s.name
FROM Orders o 
left join Company c on o.com_id = c.com_id 
left join SalesPerson s on o.sales_id = s.sales_id
WHERE c.name = "RED")
