/*
Well Paid Employees
Given a table of S&P Global employee salary data, write a SQL query to find all employees who earn more than their own manager.

S&P Global employees Example Input:
employee_id	name	        salary	department_id	manager_id
1	        Emma Thompson	3800	1	
2	        Daniel Rodrig   2230	1	            10
3	        Olivia Smith	8000	1	            8
4	        Noah Johnson	6800	2	            8
5	        Sophia Martinez	1750	1	            10
8	        William Davis	7000	2	            NULL
10	        James Anderson	4000	1	            NULL

Example Output:
employee_id	employee_name
    3	    Olivia Smith

This is the output because Olivia Smith earns $8,000, surpassing her manager, William Davis who earns 7,800.
*/
-- First, we perform a SELF-JOIN where we treat the first employee table (mgr) as the managers' table and the second employee table (emp) as the employees' table. Then we use a WHERE clause to filter the results, ensuring we only get employees whose salaries are higher than their manager's salary.

SELECT
  emp.employee_id AS employee_id,
  emp.name AS employee_name
FROM employee AS mgr
INNER JOIN employee AS emp
  ON mgr.employee_id = emp.manager_id
WHERE emp.salary > mgr.salary;