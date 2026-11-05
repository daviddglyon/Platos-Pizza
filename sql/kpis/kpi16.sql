-- kpi 15: combien par jour moyenne

SELECT COUNT(*) nbr_par jour 
FROM orders
GROUP BY  date