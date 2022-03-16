-- Script that creates the table id_not_null on your MySQL server
-- Description: id int with default value of 1
-- name varchar(256)
CREATE TABLE IF NOT EXISTS id_not_null(
    id INT DEFAULT 1,
    name VARCHAR(256)
);
