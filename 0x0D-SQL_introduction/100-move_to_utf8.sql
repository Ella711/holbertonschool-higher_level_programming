-- Script that converts hbtn_0c_0 database to UTF8 and collate utf8mb4 unicode ci
--  Convert the database, table and field: name
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE hbtn_0c_0;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- ALTER TABLE first_table MODIFY name VARCHAR(256) CHARACTER SET utf8mb4;
