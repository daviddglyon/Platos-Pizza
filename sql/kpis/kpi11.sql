-- KPI 11: ca par mois
SELECT month(date) mois, SUM(quantity * price) AS prix_achat
FROM jview 
GROUP BY month(date)
ORDER BY prix_achat DESC;