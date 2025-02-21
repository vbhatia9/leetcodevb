/* 570. Managers with at Least 5 Direct Reports
Table: Employee

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| department  | varchar |
| managerId   | int     |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the name of an employee, their department, and the id of their manager.
If managerId is null, then the employee does not have a manager.
No employee will be the manager of themself.
 

Write a solution to find managers with at least five direct reports.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Employee table:
+-----+-------+------------+-----------+
| id  | name  | department | managerId |
+-----+-------+------------+-----------+
| 101 | John  | A          | null      |
| 102 | Dan   | A          | 101       |
| 103 | James | A          | 101       |
| 104 | Amy   | A          | 101       |
| 105 | Anne  | A          | 101       |
| 106 | Ron   | B          | 101       |
+-----+-------+------------+-----------+
Output: 
+------+
| name |
+------+
| John |
+------+
Explanation: John is the only manager who has at least 5 direct reports.


*/
SELECT name
FROM Employee
WHERE id IN (
    SELECT managerId
    FROM Employee
    GROUP BY managerId
    HAVING COUNT(*) >= 5
);

/*
The provided SQL query is designed to retrieve the names of employees who are managers overseeing at least five other employees. This query is executed in two main parts: an inner query and an outer query.

The inner query is:
This part of the query selects the managerId from the Employee table and groups the results by managerId. The GROUP BY clause is used to aggregate the data based on the managerId. The HAVING clause then filters these groups to include only those managers who have five or more employees reporting to them. The COUNT(*) function counts the number of employees in each group.


SELECT managerId
FROM Employee
GROUP BY managerId
HAVING COUNT(*) >= 5

The outer query is:
SELECT name
FROM Employee
WHERE id IN (
    ...
);

This part of the query selects the name of employees from the Employee table where the id of the employee matches any managerId returned by the inner query. The WHERE id IN (...) clause ensures that only the names of those employees who are managers with at least five direct reports are selected.

In summary, this SQL query effectively identifies and lists the names of managers who have a significant number of direct reports, specifically five or more.

*/