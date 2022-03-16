-- Script that creates the table force_name
-- id int and name varchar(256) can't be null
-- if name already exists, script should not fail
CREATE TABLE IF NOT EXISTS force_name(
    id INT,
    name VARCHAR(256) NOT NULL
);
