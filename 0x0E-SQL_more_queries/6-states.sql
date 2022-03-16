-- Script that creates the database hbtn_0d_usa and the table states
-- Description: id int unique, auto generated, can't be null, primary key
-- name varchar(256) can't be null
-- If db or table already exist, script should not fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(
    id INT AUTO_INCREMENT NOT NULL UNIQUE,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
