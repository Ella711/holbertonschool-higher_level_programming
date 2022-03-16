-- Script that creates the database hbtn_0d_2 and the user user_0d_2
-- User should only have SELECT privileges in the new db
-- pass will be set to user_0d_2_pwd
-- if database or user already exists, script should not fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT USAGE ON *.* TO 'user_0d_2'@'localhost';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
