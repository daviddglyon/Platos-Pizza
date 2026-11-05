-- kpi 13: pizza par les nobres des ingredients. on va appeler dept
SELECT name pizza, category, (LENGTH(ingredients)-LENGTH(REPLACE(ingredients, '-', ''))) AS nombre_ingreds
FROM pizza_types
ORDER BY nombre_ingreds DESC;
