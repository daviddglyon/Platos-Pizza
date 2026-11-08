-- KPI 12:  les prix
SELECT 	ROUND(min(price),2) prix_minimal, 
		ROUND(max(price),2) prix_maximal, 
        ROUND(avg(price),2) prix_moyenne 
FROM (
	SELECT price
	FROM pizza p 
	GROUP BY price
	ORDER BY price DESC
    ) as gropedprices