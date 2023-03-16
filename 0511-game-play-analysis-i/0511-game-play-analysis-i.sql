# Write your MySQL query statement below
SELECT a.player_id,MIN(a.event_date) as "first_login"
FROM Activity a 
GROUP BY a.player_id
