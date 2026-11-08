CREATE VIEW nombre_cmd_date_view AS
SELECT date, COUNT(*) nombre_par_date
FROM orders
GROUP BY date 
ORDER BY date;

SELECT * FROM nombre_cmd_date_view LIMIT 10;