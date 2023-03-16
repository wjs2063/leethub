# Write your MySQL query statement below
SELECT a.player_id ,MIN(a.event_date) as "first_login"
FROM Activity a
GROUP BY a.player_id
HAVING "first_login" = MIN("first_login")


#키포인트는 HAVING 절은 SELECT 절 이후를 필터링하는것이다 ->
#WHERE 절느낌과 사뭇다름 둘다 필터링 역할을 하긴하지만 WHERE 는 select 이전에 필터링
#HAVING 은 select 이후를 필터링
#이전에 했던게 왜안되냐?
#player_id 의 기록이 여러개있는데 아무집계함수없이 GROUP BY 를 하게되면 전혀엉뚱한결과가
#나오게되고 -> 중복 다무시한채 아무결과가 나오게됨 -> 그말 즉 -> MIN 값을 제대로 찾지못하는현상





