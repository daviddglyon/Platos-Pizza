-- KPI 6: par quantitées
SELECT quantity, COUNT(*) AS nombres_par_quantités
FROM order_details
GROUP BY quantity
ORDER BY nombres_par_quantités DESC