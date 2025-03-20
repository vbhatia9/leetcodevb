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