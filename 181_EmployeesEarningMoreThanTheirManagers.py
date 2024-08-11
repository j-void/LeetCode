# Write your MySQL query statement below
-- select E.name as "Employee"
-- from Employee E
-- where E.salary > (select distinct salary from Employee where id = E.managerId)

select E.name as "Employee"
from Employee E
join Employee EM on E.managerId = EM.id
where Em.salary < E.salary
