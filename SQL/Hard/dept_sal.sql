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

SELECT department, employee, salary 
FROM (
    SELECT d.name AS department, e.name AS employee, e.salary,
           DENSE_RANK() OVER (PARTITION BY d.id ORDER BY e.salary DESC) AS rnk
    FROM Employee e
    JOIN Department d ON e.departmentId = d.id
) temp
WHERE rnk <= 3;
