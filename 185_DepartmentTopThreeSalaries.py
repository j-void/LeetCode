SELECT D.name AS Department, E.name AS Employee, E.salary AS Salary
FROM Employee E
JOIN Department D ON E.departmentId = D.id
WHERE (
    SELECT COUNT(DISTINCT salary)
    FROM Employee E2
    WHERE E2.departmentId = E.departmentId and E2.salary >= E.salary
) <= 3
ORDER BY D.name, E.salary DESC;
