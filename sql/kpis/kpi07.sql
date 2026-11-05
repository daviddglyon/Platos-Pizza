-- KPI 7: ca par nom de pizza
SELECT name pizza, ROUND(SUM(quantity * price),2) AS prix_achat
FROM jview 
GROUP BY name
ORDER BY prix_achat DESC;