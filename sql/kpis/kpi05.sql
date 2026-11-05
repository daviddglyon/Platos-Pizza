-- KPI 5: nombre commandes par périod horaires
SELECT travail_périod, COUNT(*) nobres_par_périod_du_travail 
FROM (	SELECT *, CASE WHEN time BETWEEN '09:00:00' AND '18:00:00' THEN 'Temps de Travail' ELSE  'Hors de Travail' END travail_périod
		FROM   orders) as ff
GROUP BY travail_périod
ORDER BY nobres_par_périod_du_travail DESC;