 /*
Employee table with three columns emp
 
ID, Salary, DeptID
 
10, 1000, 2
 
20, 5000, 3
 
30, 3000, 2
 
Department table with two columns: dept
 
ID, DeptName
 
1, Marketing
 
2, IT
 
3, Finance

Emp Address  emp_addrs

id address

10  India

20  UK

30  US
 
find  salary for each employee along with deptname and emp address*/

SELECT e.id AS EmployeeID, e.salary, d.DeptName, a.address 
FROM emp e
JOIN dept d ON e.DeptID = d.id
JOIN emp_addrs a ON e.id = a.id;
