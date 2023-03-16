# Write your MySQL query statement below

SELECT a.activity_date "day", COUNT(DISTINCT(a.user_id)) as "active_users"
FROM Activity a
WHERE a.activity_date <= DATE_FORMAT("2019-07-27","%Y-%m-%d") and DATEDIFF("2019-07-27",a.activity_date) + 1 <= 30
GROUP BY a.activity_date