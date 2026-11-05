-- KPI 4: nombre commandes par mois
SELECT MONTH(date) as cmd_mois, COUNT(*) nobre_par_mois
FROM   orders
GROUP BY cmd_mois
ORDER BY cmd_mois ;