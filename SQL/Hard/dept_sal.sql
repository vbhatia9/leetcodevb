/* SQL/Hard/
 Department Top Three Salaries (Hard)

Problem: Find the top 3 highest salaries in each department.

*/


WITH RankedSalaries AS (
    SELECT 
        DepartmentId,
        EmployeeId,
        Salary,
        RANK() OVER (PARTITION BY DepartmentId ORDER BY Salary DESC) AS Rank
    FROM Employee
)
SELECT 
    DepartmentId,
    EmployeeId,
    Salary
FROM RankedSalaries
WHERE Rank <= 3
ORDER BY DepartmentId, Rank;