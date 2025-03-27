/*
176. Second Highest Salary
Table: Employee

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.
 

Write a solution to find the second highest distinct salary from the Employee table.
 If there is no second highest salary, return null (return None in Pandas).

The result format is in the following example.

 

Example 1:

Input: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
Output: 
+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+
Example 2:

Input: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
+----+--------+
Output: 
+---------------------+
| SecondHighestSalary |
+---------------------+
| null                |
+---------------------+
*/

SELECT (
    SELECT DISTINCT salary
     FROM Employee
     ORDER BY salary DESC
     LIMIT 1 OFFSET 1
     ) AS SecondHighestSalary;  -- OFFSET 1 skips the highest salary and retrieves the second highest salary
-- The provided SQL query is designed to retrieve the second highest distinct salary from the Employee table. This query is executed using a subquery within the SELECT statement to retrieve the salary value that is distinct and second highest. The subquery is ordered by salary in descending order and limited to retrieve the second highest salary using the OFFSET 1 clause. The result is returned in the specified format.      
``` 