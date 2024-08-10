# Write your MySQL query statement below
Select
    P.firstName,
    P.lastName,
    A.city,
    A.state
From 
    Person as P
Left Join
    Address as A
ON
    P.personId = A.personId;
