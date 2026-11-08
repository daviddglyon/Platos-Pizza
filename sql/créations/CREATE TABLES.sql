CREATE TABLE orders (
	order_id int primary key,
	date date,
	time time
);

CREATE TABLE pizza_types (
	pizza_type_id VARCHAR(15) primary key, 
    name nvarchar(45), 
    category varchar(10), 
    ingredients text
);

CREATE TABLE pizza (
	pizza_id VARCHAR(14) primary key, 
	pizza_type_id  VARCHAR(15),
    constraint fk_pizza_type foreign key (pizza_type_id) references pizza_types(pizza_type_id),
	size char(5), 
	price float
 );
 
CREATE TABLE order_details (
	order_details_id int primary key, 
	order_id int, 
    constraint fk_order_id foreign key (order_id) references orders(order_id),
	pizza_id VARCHAR(14), 
    constraint fk_pizza_id foreign key (pizza_id) references pizza(pizza_id),
	quantity float
 );
 