# Write your MySQL query statement below
SELECT u.name,SUM(ifnull(r.distance,0)) AS "travelled_distance"
FROM Rides r right join Users u on r.user_id = u.id
GROUP BY r.user_id
ORDER BY SUM(r.distance) DESC ,u.name ASC