-- KPI 11: ca par mois
SELECT MONTHNAME(date) as mois, ROUND(SUM(quantity * price),2) AS prix_achat
FROM jview 
GROUP BY YEAR(date), MONTH(date), mois
ORDER BY YEAR(date), MONTH(date);

