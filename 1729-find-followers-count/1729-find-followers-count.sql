# Write your MySQL query statement below
SELECT f.user_id,COUNT(DISTINCT(f.follower_id)) as "followers_count"
FROM Followers as f
GROUP BY f.user_id