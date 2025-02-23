/*
4: Analyzing Financial Data with Window Functions
A recorded dataset includes daily stock market performance for a few select companies. Let's consider company 'X', 'Y', and 'Z'. You must write a PostgreSQL query that calculates the seven-day rolling average of closing prices for each company, but excludes the current day's closing price in this calculation.

The dataset is housed in the table stock_prices formatted as follows:

stock_prices Example Input:
date	company	closing_price
2022-01-01	X	1000
2022-01-02	X	1050
2022-01-03	X	1020
2022-01-04	X	1040
2022-01-05	X	1060
2022-01-06	X	1030
2022-01-07	X	1045
2022-01-08	X	1070

This data wants to be transformed into the following table:

Example Output:
date	company	closing_price	rolling_avg_price
2022-01-01	X	1000	NULL
2022-01-02	X	1050	NULL
2022-01-03	X	1020	NULL
2022-01-04	X	1040	NULL
2022-01-05	X	1060	NULL
2022-01-06	X	1030	NULL
2022-01-07	X	1045	1000
2022-01-08	X	1070	1025
*/
-- Write your MySQL query statement below
/*
The active selection is a SQL query that calculates a rolling average of stock closing prices over a specified window of time. The query is structured using a Common Table Expression (CTE) named rolling_avg to simplify the main query.

Within the rolling_avg CTE, the query selects the date, company, and closing_price columns from the stock_prices table. It also calculates a rolling average of the closing_price using the AVG window function. The OVER clause specifies that the calculation should be partitioned by company and ordered by date. The ROWS BETWEEN 7 PRECEDING AND 1 PRECEDING clause defines the window as the seven rows preceding the current row, excluding the current row itself. This means the rolling average is computed over the previous seven days' closing prices for each company.

The main query then selects the date, company, and closing_price from the rolling_avg CTE. It uses a CASE statement to handle NULL values in the closing_price column. If closing_price is NULL, the rolling_avg_price is also set to NULL. Otherwise, the rolling_avg_price is rounded to two decimal places using the ROUND function. Finally, the results are ordered by company and date to provide a clear, chronological view of the rolling average prices for each company.

*/

--Sol 1 Autopilot
WITH rolling_avg AS (
  SELECT
    date,
    company,
    closing_price,
    AVG(closing_price) OVER (PARTITION BY company ORDER BY date ROWS BETWEEN 7 PRECEDING AND 1 PRECEDING) AS rolling_avg_price
  FROM stock_prices
)
SELECT
  date,
  company,
  closing_price,
  CASE
    WHEN closing_price IS NULL THEN NULL
    ELSE ROUND(rolling_avg_price, 2)
  END AS rolling_avg_price
FROM rolling_avg
ORDER BY company, date;

--Sol 2 web
SELECT 
    date,
    company,
    closing_price,
    avg(closing_price) OVER (
        PARTITION BY company
        ORDER BY date
        ROWS BETWEEN 6 PRECEDING AND 1 PRECEDING
    ) as rolling_avg_price
FROM 
    stock_prices
ORDER BY 
    date ASC;