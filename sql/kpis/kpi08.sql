-- KPI 8: ca par la taille de pizza
SELECT size, SUM(quantity * price) AS prix_achat
FROM jview 
GROUP BY size
ORDER BY prix_achat DESC;