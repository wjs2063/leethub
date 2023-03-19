# Write your MySQL query statement below

SELECT v.customer_id,COUNT(*) AS "count_no_trans"
FROM Visits v left join Transactions t on v.visit_id = t.visit_id
WHERE amount is null 
GROUP BY v.customer_id