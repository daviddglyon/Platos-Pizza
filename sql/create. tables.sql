CREATE table orders (
order_id int,
date date,
time time
);

create table order_details (
	order_details_id int primary key, 
	order_id int, 
	pizza_id int, 
	quantity float
 );
 
 create table pizza (
	pizza_id int primary key, 
	pizza_type_id  int, 
	size float, 
	price float
 );
 
 create table pizza_types (
	pizza_type_id int, 
    name nvarchar(25), 
    category nvarchar(10), 
    ingredients text
)
