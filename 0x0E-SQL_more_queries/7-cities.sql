-- Script that creates the database hbtn_0d_usa and the table cities
-- Description: id INT unique, auto generate, can't be null, primary key
-- state_id, int, not null, foreign key that references id of states table
-- name VARCHAR256, can't be null
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(
    id INT AUTO_INCREMENT UNIQUE NOT NULL,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (state_id) REFERENCES hbtn_0d_usa.states(id)
);
