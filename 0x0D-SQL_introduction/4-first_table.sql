-- Script that creates a table called first_table in the current database
-- Database name will be passed as an argument.
-- If the table first_table already exists, your script should not fail
CREATE TABLE IF NOT EXISTS first_table(
    id INT,
    name VARCHAR(256)
);
