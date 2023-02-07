# Write your MySQL query statement below

select user_id, CONCAT(
    UPPER(SUBSTR(name,1,1)),
    LOWER(SUBSTR(name,2,length(name)))
    ) as name
from Users ORDER BY user_id