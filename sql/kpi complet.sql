-- KPI 7: ca par nom de pizza
SELECT name, SUM(quantity * price) AS prix_achat
FROM jview 
GROUP BY name
ORDER BY prix_achat DESC;


-- KPI 8: ca par la taille de pizza
SELECT size, SUM(quantity * price) AS prix_achat
FROM jview 
GROUP BY size
ORDER BY prix_achat DESC;

-- KPI 9: ca par la catégorie de pizza
SELECT category, SUM(quantity * price) AS prix_achat
FROM jview 
GROUP BY category
ORDER BY prix_achat DESC;


-- KPI 10: ca par la catégorie de pizza
SELECT category, SUM(quantity * price) AS prix_achat
FROM jview 
GROUP BY category
ORDER BY prix_achat DESC;

-- KPI 11: ca par mois
SELECT month(date) mois, SUM(quantity * price) AS prix_achat
FROM jview 
GROUP BY month(date)
ORDER BY prix_achat DESC;


-- KPI 12:  les prix
SELECT min(price) prix_minimal, max(price) prix_maximal, avg(price) prix_moyenne 
FROM (
	SELECT price
	FROM pizza p 
	GROUP BY price
	ORDER BY price DESC
    ) as gropedprices