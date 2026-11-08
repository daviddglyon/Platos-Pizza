-- kpi 17: nombre max  ventes

SELECT date max_number_ventes, nombre_par_date
FROM  nombre_cmd_date_view
WHERE nombre_par_date = (SELECT MAX(nombre_par_date) FROM nombre_cmd_date_view) 