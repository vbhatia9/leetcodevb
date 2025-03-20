/* SQL/Hard/
185. Department Top Three Salaries
https://leetcode.com/problems/department-top-three-salaries/

Problem: Find the top 3 highest salaries in each department.


*/

-- wrong answer
-- WITH RankedSalaries AS (
--     SELECT 
--         DepartmentId,
--         EmployeeId,
--         Salary,
--         RANK() OVER (PARTITION BY DepartmentId ORDER BY Salary DESC) AS Rank -- Rank salaries within each department
--     FROM Employee
-- )
-- SELECT 
--     DepartmentId,
--     EmployeeId,
--     Salary
-- FROM RankedSalaries
-- WHERE Rank <= 3
-- ORDER BY DepartmentId, Rank;


/*
This SQL query is designed to retrieve the top three highest-paid employees from each department, along with their department name and salary. It achieves this by using a combination of a subquery, a DENSE_RANK() window function, and filtering.

In the subquery:

The Employee table (e) is joined with the Department table (d) using the departmentId foreign key to associate each employee with their respective department.
The DENSE_RANK() window function is used to rank employees within each department (PARTITION BY d.id) based on their salary in descending order (ORDER BY e.salary DESC). 
This ensures that the highest-paid employee in each department gets a rank of 1, the second-highest gets a rank of 2, and so on. If multiple employees have the same salary, they are assigned the same rank, but the next rank is not skipped (hence "dense" ranking).

The outer query filters the results of the subquery to include only those rows where the rank (rnk) is less than or equal to 3. 
This ensures that only the top three highest-paid employees from each department are included in the final result.

Summary
The query outputs a list of departments, employees, and their salaries, showing only the top three earners in each department.
 The use of DENSE_RANK() ensures that ties in salary are handled correctly, and no ranks are skipped. 
 This is particularly useful for scenarios where you want to identify the top performers in each group (in this case, departments) based on a specific metric (salary).


*/
SELECT department, employee, salary 
FROM (
    SELECT d.name AS department, e.name AS employee, e.salary,
           DENSE_RANK() OVER (PARTITION BY d.id ORDER BY e.salary DESC) AS rnk
    FROM Employee e
    JOIN Department d ON e.departmentId = d.id
) temp
WHERE rnk <= 3;
