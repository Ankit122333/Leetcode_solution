# Write your MySQL query statement below
SELECT CLASS AS CLASS
FROM COURSES
GROUP BY CLASS
HAVING
COUNT(DISTINCT STUDENT)>=5;