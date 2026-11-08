-- kpi 17: nombre min des vintes

SELECT date min_number_ventes, nombre_par_date
FROM  nombre_cmd_date_view
WHERE nombre_par_date = (SELECT MIN(nombre_par_date) FROM nombre_cmd_date_view) 