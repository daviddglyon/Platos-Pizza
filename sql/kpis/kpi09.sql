-- KPI 9: ca par la catégorie de pizza
SELECT category, ROUND(SUM(quantity * price),2) AS prix_achat
FROM jview 
GROUP BY category
ORDER BY prix_achat DESC;