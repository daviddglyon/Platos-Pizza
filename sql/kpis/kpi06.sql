-- KPI 6: par quantitées
SELECT quantity, COUNT(*) AS nombres_linges_par_quantités_pizza
FROM order_details
GROUP BY quantity
ORDER BY nombres_linges_par_quantités_pizza DESC