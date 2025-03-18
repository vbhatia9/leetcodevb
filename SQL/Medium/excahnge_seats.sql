/*626. Exchange Seats
Table: Seat

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| student     | varchar |
+-------------+---------+
id is the primary key (unique value) column for this table.
Each row of this table indicates the name and the ID of a student.
The ID sequence always starts from 1 and increments continuously.
 

Write a solution to swap the seat id of every two consecutive students. If the number of students is odd, 
the id of the last student is not swapped.

Return the result table ordered by id in ascending order.

*/
-- not sure 
SELECT id, 
       CASE 
           WHEN MOD(id, 2) = 0 THEN LAG(student, 1) OVER (ORDER BY id)
           WHEN MOD(id, 2) = 1 THEN LEAD(student, 1) OVER (ORDER BY id)
           ELSE student 
       END AS student
FROM Seat
ORDER BY id;
