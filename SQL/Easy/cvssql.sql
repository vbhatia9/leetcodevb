/*
claim_date    claim_id   state 
01/01/2023    33         AZ
01/01/2023    66         AZ
01/02/2023    67         FL
01/03/2023    77         TX
02/01/2023    22         FL
03/01/2023    33         CT
03/01/2023    66         CT
03/02/2023    67         AZ
03/03/2023    77         TX
03/03/2023    38         CT
03/03/2023    68         CT
 
#claim_date  format mm/dd/yyyy
 
#Output
 
claim_month Total_claims  Max_claim_day  Max_claim_state   
Jan         4             01/01/2023     AZ                
Feb         1             02/01/2023     FL                
Mar         6             03/03/2023     CT  

*/
/*The provided SQL query is designed to analyze and summarize claims data on a monthly basis, identifying the days with the highest number of claims for each
 month and the corresponding states. The query is structured using Common Table Expressions (CTEs) to break down the problem into manageable parts.

The first CTE, MonthlyClaims, aggregates the claims data by month, date, and state. It formats the claim_date to extract the month in abbreviated form (e.g., 'Jan', 'Feb') and 
counts the number of claims (claim_id) for each combination of month, date, and state. This results in a table where each row represents the total number of claims for a specific day
and state within a month.

The second CTE, MaxClaims, identifies the maximum number of claims for each month. It selects the month and the highest count of claims (Max_claims) from the MonthlyClaims table, 
grouping the results by month. This helps in determining the peak claim day for each month.

The third CTE, MaxClaimDays, finds the specific days and states that correspond to the maximum number of claims identified in the MaxClaims CTE. 
It joins the MonthlyClaims table with the MaxClaims table on the month and the total number of claims, ensuring that only the days with the highest claims for each month are selected.

Finally, the main query selects the month, the total number of claims for that month, the day with the maximum claims, and the state where this occurred. 
It joins the MonthlyClaims table with the MaxClaimDays table on the month, groups the results by month, maximum claim day, and state, and orders the output by the month 
in chronological order.

This query provides a comprehensive summary of the claims data, highlighting the peak claim days and states for each month, which can be useful for identifying trends and patterns
 in the claims data.*/

-- The first CTE, MonthlyClaims, aggregates the claims data by month, date, and state. It formats the claim_date to extract the month in abbreviated form (e.g., 'Jan', 'Feb') and 
-- counts the number of claims (claim_id) for each combination of month, date, and state. This results in a table where each row represents the total number of claims for a specific day
-- and state within a month.

WITH MonthlyClaims AS (
    SELECT 
        DATE_FORMAT(claim_date, '%b') AS claim_month,
        COUNT(claim_id) AS Total_claims,
        claim_date,
        state
    FROM claims
    GROUP BY claim_month, claim_date, state
),
MaxClaims AS (
    SELECT 
        claim_month,
        MAX(Total_claims) AS Max_claims
    FROM MonthlyClaims
    GROUP BY claim_month
),
MaxClaimDays AS (
    SELECT 
        mc.claim_month,
        mc.claim_date AS Max_claim_day,
        mc.state AS Max_claim_state
    FROM MonthlyClaims mc
    JOIN MaxClaims mxc ON mc.claim_month = mxc.claim_month AND mc.Total_claims = mxc.Max_claims
)
SELECT 
    mc.claim_month,
    SUM(mc.Total_claims) AS Total_claims,
    mcd.Max_claim_day,
    mcd.Max_claim_state
FROM MonthlyClaims mc
JOIN MaxClaimDays mcd ON mc.claim_month = mcd.claim_month
GROUP BY mc.claim_month, mcd.Max_claim_day, mcd.Max_claim_state
ORDER BY FIELD(mc.claim_month, 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec');
