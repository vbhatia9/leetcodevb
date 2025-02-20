"""
Identify S&P Global's Most Important Customers

You are given two tables - customers and sales.

customers contains details of their customers and sales contains details of all sales transactions performed.

Write a SQL query to list down all the 'whale' customers along with their total spending in the past 30 days.

customers Sample Input
customer_id	first_name	last_name	email
1	        John	        Doe	     john.doe@gmail.com
2	        Jane	        Smith	 jane.smith@gmail.com
3	        Jim	            Brown	 jim.brown@gmail.com
4	        Alice	        Johnson	 alice.johnson@gmail.com
5	        Bob	            Williams bob.williams@gmail.com
sales Sample Input
transaction_id	customer_id	transaction_date	amount
1001	            1	    06/01/2022 12:00:00	5000
1002	            1	    06/20/2022 15:00:00	6000
1003	            2	    06/08/2022 13:30:00	9000
1004	            3	    06/20/2022 10:00:00	4000
1005	            4	    06/15/2022 16:00:00	3000
1006	            4	    07/20/2022 19:00:00	7500
"""

SELECT c.customer_id, c.first_name, c.last_name, c.email, SUM(s.amount) AS total_spent
FROM customers AS c
JOIN sales AS s
ON c.customer_id = s.customer_id
WHERE s.transaction_date >= (CURRENT_DATE - INTERVAL '30 days')
GROUP BY c.customer_id
HAVING SUM(s.amount) > 10000;
