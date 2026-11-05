-- kpi 15: combien par jour moyenne

SELECT ROUND(avg(nbr_par_date),0) cmd_moyenne_jour
FROM (
		SELECT COUNT(*) nbr_par_date 
		FROM orders
		GROUP BY  date
	) as par_date