-- SHOW VARIABLES LIKE "secure_file_priv";
SET GLOBAL local_infile = 1;

LOAD DATA local INFILE 'C:\\Users\\Utilisateur\\Documents\\Pizza sql streamlit\\Platos Pizza\\data\\pizza_types_cleaned.csv'
INTO TABLE pizza_types
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA local INFILE 'C:\\Users\\Utilisateur\\Documents\\Pizza sql streamlit\\Platos Pizza\\data\\pizzas.csv'
INTO TABLE pizza
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA local INFILE 'C:\\Users\\Utilisateur\\Documents\\Pizza sql streamlit\\Platos Pizza\\data\\orders.csv'
INTO TABLE orders
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA local INFILE 'C:\\Users\\Utilisateur\\Documents\\Pizza sql streamlit\\Platos Pizza\\data\\order_details.csv'
INTO TABLE order_details
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;



