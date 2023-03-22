# Write your MySQL query statement below

SELECT e.employee_id as "employee_id"
FROM Employees e left join Salaries s on e.employee_id = s.employee_id
WHERE s.salary is null
UNION
SELECT s.employee_id as "employee_id"
FROM Salaries s left join Employees e on e.employee_id = s.employee_id
WHERE e.name is null
ORDER BY employee_id ASC