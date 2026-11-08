-- KPI 14: ca total
SELECT ROUND(SUM(quantity * price),2) AS CA
FROM jview 