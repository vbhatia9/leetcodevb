-- Write a SQL query to report the Nth highest salary from the Employee table.
-- If there is no Nth highest salary, the query should return null.
--AUTO

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    RETURN (
        SELECT DISTINCT Salary
        FROM Employee
        ORDER BY Salary DESC
        LIMIT 1 OFFSET N-1
    );
END;

--SOLUTION 2
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT

BEGIN
  SET N= N-1;
  RETURN (
      -- Write your MySQL query statement below.
    SELECT DISTINCT SALARY FROM EMPLOYEE ORDER BY SALARY DESC
    LIMIT 1 OFFSET N
  );
END