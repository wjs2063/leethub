# Write your MySQL query statement below

SELECT d.actor_id,d.director_id

FROM ActorDirector d
GROUP BY d.actor_id,d.director_id
HAVING COUNT(*) >= 3
