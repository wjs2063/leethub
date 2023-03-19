# Write your MySQL query statement below

SELECT u.name,SUM(t.amount) AS "balance"
FROM Users u left join Transactions t on u.account = t.account
GROUP BY u.account
HAVING SUM(t.amount) > 10000