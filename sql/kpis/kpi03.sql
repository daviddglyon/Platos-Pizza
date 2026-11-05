-- KPI 3: nombre commandes par dates
SELECT date, COUNT(*) nombre_par_date
FROM orders
GROUP BY date 
ORDER BY date;