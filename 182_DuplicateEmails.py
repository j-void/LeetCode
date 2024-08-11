# Write your MySQL query statement below
select P.email as "Email"
from Person P   
group by P.email
having count(P.email) > 1
