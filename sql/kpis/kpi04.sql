-- KPI 4: nombre commandes par mois
SELECT 
    MONTHNAME(date) AS cmd_mois, 
    COUNT(*) AS nombre_par_mois
FROM orders
GROUP BY YEAR(date), MONTH(date), cmd_mois
ORDER BY YEAR(date), MONTH(date);