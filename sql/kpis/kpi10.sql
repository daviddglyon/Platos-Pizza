-- KPI 10: ca par la catégorie de pizza
SELECT category, SUM(quantity * price) AS prix_achat
FROM jview 
GROUP BY category
ORDER BY prix_achat DESC;