-- KPI 8: ca par la taille de pizza
SELECT size, ROUND(SUM(quantity * price),2) AS prix_achat
FROM jview 
GROUP BY size
ORDER BY prix_achat DESC;