/* 1407. Top Travellers
Table: Users

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| name          | varchar |
+---------------+---------+
id is the primary key for this table.
name is the name of the user.
 

Table: Rides

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| user_id       | int     |
| distance      | int     |
+---------------+---------+
id is the primary key for this table.
user_id is the id of the user who traveled the distance "distance".
 

Write an SQL query to report the distance traveled by each user.

Return the result table ordered by travelled_distance in descending order, if two or more users traveled the same distance, order them by their name in ascending order.

The query result format is in the following example.

 

Example 1:

Input: 
Users table:
+------+-----------+
| id   | name      |
+------+-----------+
| 1    | Alice     |
| 2    | Bob       |
| 3    | Alex      |
| 4    | Donald    |
| 7    | Lee       |
| 13   | Jonathan  |
| 19   | Elvis     |
+------+-----------+
Rides table:
+------+----------+----------+
| id   | user_id  | distance |
+------+----------+----------+
| 1    | 1        | 120      |
| 2    | 2        | 317      |
| 3    | 3        | 222      |
| 4    | 7        | 100      |
| 5    | 13       | 312      |
| 6    | 19       | 50       |
| 7    | 7        | 120      |
| 8    | 19       | 400      |
| 9    | 7        | 230      |
+------+----------+----------+
Output: 
+----------+--------------------+
| name     | travelled_distance |
+----------+--------------------+
| Elvis    | 450                |
| Lee      | 450                |
| Bob      | 317                |
| Jonathan | 312                |
| Alex     | 222                |
| Alice    | 120                |
| Donald   | 0                  |
+----------+--------------------+
Explanation: 
Elvis and Lee traveled 450 miles, Elvis is the top traveler as his name is alphabetically smaller than Lee.
Bob, Jonathan, Alex, and Alice have only one ride and we just order them by the total distances of the ride.
Donald did not have any rides, the distance traveled by him is 0. */
/*
The active selection is a SQL query that calculates and retrieves the total distance traveled by each user, ensuring that all users are included in the result even if they have no associated rides. The query is structured using a Common Table Expression (CTE) named UserDistance to simplify the main query.

Within the UserDistance CTE, the query selects the user_id and calculates the total distance traveled by each user using the SUM function on the distance column from the Rides table. The COALESCE(SUM(distance), 0) function ensures that if a user has no rides, the total distance (travelled_distance) is set to 0 instead of NULL. The results are grouped by user_id to aggregate the distances for each user.

The main query then selects the name of the user from the Users table, represented by the alias u, and the total distance traveled by each user from the UserDistance CTE, represented by the alias ud. The LEFT JOIN ensures that all users from the Users table are included in the result, even if they have no corresponding entries in the Rides table. The COALESCE(ud.travelled_distance, 0) function is used again to handle any NULL values that might result from the join, ensuring that users with no rides have a travelled_distance of 0.

Finally, the ORDER BY clause sorts the results first by travelled_distance in descending order, so users who have traveled the most distance appear first. If multiple users have traveled the same distance, they are further sorted by name in ascending order to maintain a consistent and readable order. This query provides a comprehensive view of the total distance traveled by each user, ordered by their travel activity and name.


WITH UserDistance AS (
    SELECT user_id, COALESCE(SUM(distance), 0) AS travelled_distance
    FROM Rides
    GROUP BY user_id
)
SELECT u.name, COALESCE(ud.travelled_distance, 0) AS travelled_distance
FROM Users u
LEFT JOIN UserDistance ud ON u.id = ud.user_id
ORDER BY travelled_distance DESC, u.name ASC;
*/

/*
The COALESCE(SUM(r.distance), 0) expression ensures that if a user has no rides, the total distance (travelled_distance) is set to 0 instead of NULL. The SUM(r.distance) function calculates the total distance for each user by summing the distance column from the Rides table, represented by the alias r.

The query uses a LEFT JOIN to combine the Users table with the Rides table on the condition that the id from the Users table matches the user_id from the Rides table. This ensures that all users are included in the result, even if they have no rides.

*/

SELECT u.name, 
    COALESCE(SUM(r.distance), 0) AS travelled_distance
FROM Users u
LEFT JOIN Rides r ON u.id = r.user_id
GROUP BY u.id, u.name
ORDER BY travelled_distance DESC, u.name ASC;