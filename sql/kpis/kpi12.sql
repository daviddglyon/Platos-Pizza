-- KPI 12:  les prix
SELECT min(price) prix_minimal, max(price) prix_maximal, avg(price) prix_moyenne 
FROM (
	SELECT price
	FROM pizza p 
	GROUP BY price
	ORDER BY price DESC
    ) as gropedprices