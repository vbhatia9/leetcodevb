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