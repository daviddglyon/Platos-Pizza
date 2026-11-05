-- select ingredients, 
--     SUBSTRING_INDEX(ingredients, '-', 1)                           AS ingr_1,
--     SUBSTRING_INDEX(SUBSTRING_INDEX(ingredients, '-', 2), '-', -1) AS ingr_2
-- from pizza_types;

-- kpi 13: pizza par les nobres des ingredients. on va appeler dept
SELECT name, category, (LENGTH(ingredients)-LENGTH(REPLACE(ingredients, '-', ''))) AS nombre_ingredients 
FROM pizza_types
ORDER BY nombre_ingredients DESC;
