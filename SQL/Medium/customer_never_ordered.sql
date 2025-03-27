--Problem: Find customers who have never placed an order.
-- Query to find customers who never placed an order
SELECT c.name AS Customer
FROM Customers c
LEFT JOIN Orders o
ON c.id = o.customerId
WHERE o.id IS NULL;