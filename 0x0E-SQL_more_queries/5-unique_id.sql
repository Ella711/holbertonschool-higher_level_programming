-- Script that creates the table unique_id on your MySQL server.
-- Description id INT default of 1 and must be unique and name varchar(256)
-- If table exists, script should not fail.
CREATE TABLE IF NOT EXISTS unique_id(
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
