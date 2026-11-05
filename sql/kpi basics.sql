-- KPI 1:  nobre des commandes
SELECT COUNT(*) nombre_commandes FROM orders;

-- KPI 2: périods étudiées
SELECT MIN(date), MAX(date) périods_étudiées FROM orders;


-- KPI 3: nombre commandes par dates
SELECT date, COUNT(*) nobre_par_date
FROM orders
GROUP BY date 
ORDER BY nobre_par_date DESC;

-- KPI 4: nombre commandes par mois
SELECT MONTH(date) as cmd_mois, COUNT(*) nobre_par_mois
FROM   orders
GROUP BY cmd_mois
ORDER BY nobre_par_mois DESC;

-- KPI 5: nombre commandes par périod horaires
SELECT travail_périod, COUNT(*) nobres_par_périod_du_travail 
FROM (	SELECT *, CASE WHEN time BETWEEN '09:00:00' AND '18:00:00' THEN 'Temps de Travail' ELSE  'Hors de Travail' END travail_périod
		FROM   orders) as ff
GROUP BY travail_périod
ORDER BY nobres_par_périod_du_travail DESC;


-- KPI 6: par quantitées
SELECT quantity, COUNT(*) AS nombres_par_quantités
FROM order_details
GROUP BY quantity
ORDER BY nombres_par_quantités DESC