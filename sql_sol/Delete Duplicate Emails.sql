# Write your MySQL query statement below
DELETE a
FROM PERSON a, PERSON b
WHERE a.EMAIL = b.EMAIL 
AND
a.ID > b.ID;