/*
180. Consecutive Numbers

Table: Logs

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| num         | varchar |
+-------------+---------+
In SQL, id is the primary key for this table.
id is an autoincrement column starting from 1.
 

Find all numbers that appear at least three times consecutively.

Return the result table in any order.

The result format is in the following example.

Example 1:

Input: 
Logs table:
+----+-----+
| id | num |
+----+-----+
| 1  | 1   |
| 2  | 1   |
| 3  | 1   |
| 4  | 2   |
| 5  | 1   |
| 6  | 2   |
| 7  | 2   |
+----+-----+
Output: 
+-----------------+
| ConsecutiveNums |
+-----------------+
| 1               |
+-----------------+
Explanation: 1 is the only number that appears consecutively for at least three times.

*/

--Consecutive appearing means the Id of the Num are next to each others. Since this problem asks for numbers appearing at least three times consecutively, we can use 3 aliases for this table Logs, and then check whether 3 consecutive numbers are all the same.
/*
Id	Num	Id	Num	Id	Num
1	1	2	1	3	1
Note: The first two columns are from l1, then the next two are from l2, and the last two are from l3.

Then we can select any Num column from the above table to get the target data. However, we need to add a keyword DISTINCT because it will display a duplicated number if one number appears more than 3 times consecutively.
*/
--Sol 1 auto
SELECT DISTINCT l1.num AS ConsecutiveNums   -- Select the distinct number from the first alias
FROM Logs l1
JOIN Logs l2 ON l1.id = l2.id - 1           -- Join the first alias with the second alias
JOIN Logs l3 ON l2.id = l3.id - 1           -- Join the second alias with the third alias
WHERE l1.num = l2.num AND l2.num = l3.num;  -- Check whether the numbers are the same   -- Check whether the numbers are the same
 

--Sol 2
--Write your MySQL query statement below
/*
The query achieves this by using window functions and a subquery.

The outer query:

This part of the query selects distinct numbers and labels them as ConsecutiveNums. The DISTINCT keyword ensures that each number is listed only once in the result set.

The subquery:

This subquery selects the num column from the Logs table and uses the LEAD window function to look ahead in the dataset. The LEAD(num, 1) OVER () function retrieves the value of num in the next row and labels it as next_num. Similarly, LEAD(num, 2) OVER () retrieves the value of num two rows ahead and labels it as next_next_num.

The WHERE clause:WHERE num = next_num AND num = next_next_num;

This clause filters the results to include only those rows where the current num is equal to both next_num and next_next_num. This condition ensures that the number appears consecutively at least three times.

In summary, the query identifies and lists numbers from the Logs table that appear consecutively in at least three rows. The use of the LEAD function allows the query to look ahead in the dataset and compare values across multiple rows, making it possible to detect consecutive occurrences of the same number.

*/
SELECT DISTINCT num  as ConsecutiveNums         -- Select the distinct number as ConsecutiveNums
FROM (
    SELECT num, 
           LEAD(num, 1) OVER () AS next_num, 
           LEAD(num, 2) OVER () AS next_next_num
    FROM Logs
) AS temp
WHERE num = next_num AND num = next_next_num;
