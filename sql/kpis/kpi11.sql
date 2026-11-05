-- KPI 11: ca par mois
SELECT month(date) as mois, SUM(quantity * price) AS prix_achat
FROM jview 
GROUP BY month(date)
ORDER BY mois;