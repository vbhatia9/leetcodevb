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

Example 1:

Input: 
Seat table:
+----+---------+
| id | student |
+----+---------+
| 1  | Abbot   |
| 2  | Doris   |
| 3  | Emerson |
| 4  | Green   |
| 5  | Jeames  |
+----+---------+
Output: 
+----+---------+
| id | student |
+----+---------+
| 1  | Doris   |
| 2  | Abbot   |
| 3  | Green   |
| 4  | Emerson |
| 5  | Jeames  |
+----+---------+
Explanation: 
Note that if the number of students is odd, there is no need to change the last one's seat.

*/
-- not sure 
-- # Write your MySQL query statement below
/* Given that the task specifies dealing with odd and even IDs, we can efficiently separate these scenarios using a CASE WHEN clause.

For the records where the ID is even, swap the names with the preceding record. This can be achieved using the SQL window function LAG(student) OVER (ORDER BY id) to retrieve the name from the line above.

For records with an odd ID, swap the names with the subsequent record. Use the window function LEAD(student) OVER (ORDER BY id) to fetch the name from the line below.

It's important to note that for the last record with an odd ID, there will be no subsequent name to fetch. In such cases, ensure the student's name remains unchanged by using the COALESCE function to default to the original value in the student column when the window function returns null.
 SELECT 
    id,
    CASE
        WHEN id % 2 = 0 THEN LAG(student) OVER(ORDER BY id)
        ELSE COALESCE(LEAD(student) OVER(ORDER BY id), student)
    END AS student
FROM Seat
 
 */


-- Solution1
-- SELECT id, 
--        CASE 
--            WHEN MOD(id, 2) = 0 THEN LAG(student, 1) OVER (ORDER BY id)
--            WHEN MOD(id, 2) = 1 THEN LEAD(student, 1) OVER (ORDER BY id)
--            ELSE student 
--        END AS student
-- FROM Seat
-- ORDER BY id;


-- Solution2    
/*
Approach
We check if the id is odd and if the next seat (id + 1) exists in the table.
If true, swap the id with id + 1.
If the id is even, swap it with id - 1.
If there is no adjacent seat (last row in case of an odd number of students), retain the original id.
The CASE statement handles these conditions efficiently.

The final result is ordered by id in ascending order.

Time complexity:
Since we scan all rows once and use a simple conditional check with a subquery (SELECT id FROM Seat), the complexity is O(n).

Space complexity:
We do not use any extra storage apart from the output, so the complexity is O(1).
*/
SELECT 
    CASE 
        WHEN id % 2 = 1 AND id + 1 <= (SELECT MAX(id) FROM Seat) THEN id + 1 -- if id is odd and not the last one
        WHEN id % 2 = 0 THEN id - 1 -- if id is even
        ELSE id -- if id is odd and the last one
        
     
    END AS id,student-- swap id
FROM Seat
ORDER BY id;