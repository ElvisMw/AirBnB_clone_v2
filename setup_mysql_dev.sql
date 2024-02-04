-- Create or update the user 'hbnb_dev' with the password 'hbnb_dev_pwd'
CREATE OR REPLACE USER 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Create or update the database 'hbnb_dev_db'
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Grant all privileges on 'hbnb_dev_db' to 'hbnb_dev'
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grant SELECT privilege on 'performance_schema' to 'hbnb_dev'
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
