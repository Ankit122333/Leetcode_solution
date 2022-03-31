# Write your MySQL query statement below
SELECT stock_name, 
ROUND(SUM(
            CASE WHEN operation = 'Buy' THEN (-1.0*price)
            WHEN operation ='Sell' THEN price
            END)
            ,0)  AS capital_gain_loss
FROM Stocks 
GROUP BY 1;