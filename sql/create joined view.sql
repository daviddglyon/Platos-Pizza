CREATE VIEW jview AS (
	SELECT 	od.order_details_id, od.pizza_id, od.quantity, 
			o.order_id, o.date, o.time, 
            p.size, p.price,
            pt.name, pt.category, pt.ingredients
	FROM orders o LEFT JOIN order_details od ON o.order_id = od.order_id
				  LEFT JOIN pizza p ON od.pizza_id = p.pizza_id
                  LEFT JOIN pizza_types pt ON p.pizza_type_id = pt.pizza_type_id
)