SELECT 
    MAX(E.salary) AS SecondHighestSalary
FROM 
    Employee AS E
WHERE 
    E.salary not in (SELECT MAX(salary) FROM Employee);
