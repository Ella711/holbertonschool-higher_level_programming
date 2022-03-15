# 0x0D. SQL - Introduction
## Details
      By Guillaume          Weight: 1                Ongoing project - started 03-14-2022, must end by 03-16-2022 (in 1 day)          - you're done with 0% of tasks.              Checker will be released at 03-15-2022 12:00 AM              An auto review will be launched at the deadline      ## Concepts
For this project, students are expected to look at this concept:
* [Databases](https://intranet.hbtn.io/concepts/556) 

 ![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/rtcwz.jpg) 

## Resources
Read or watch :
* [What is Database & SQL?](https://intranet.hbtn.io/rltoken/khEqMKp1PHvKpfO18d4fLQ) 

* [A Basic MySQL Tutorial](https://intranet.hbtn.io/rltoken/kK_v6WRoj8aoZ1TbrYNuBQ) 

* [Basic SQL statements: DDL and DML](https://intranet.hbtn.io/rltoken/ibCYnC9CDgZg5NQQvccBWw) 
 (no need to read the chapter “Privileges”)
* [Basic queries: SQL and RA](https://intranet.hbtn.io/rltoken/yelYhpf7l0FcRIPCVfnMLw) 

* [SQL technique: functions](https://intranet.hbtn.io/rltoken/3aQcovOE-clrD8yIfxFE9Q) 

* [SQL technique: subqueries](https://intranet.hbtn.io/rltoken/lTXnq6pdk59x2h_Y-q0-Hg) 

* [What makes the big difference between a backtick and an apostrophe?](https://intranet.hbtn.io/rltoken/R--kAkehyaawZFY4m1inxQ) 

* [MySQL Cheat Sheet](https://intranet.hbtn.io/rltoken/aGZu7ulJpbbKcDhcz49yrg) 

* [MySQL 8.0 SQL Statement Syntax](https://intranet.hbtn.io/rltoken/4n4nXLDHNPyViz2H0DTGUA) 

## Learning Objectives
At the end of this project, you are expected to be able to  [explain to anyone](https://intranet.hbtn.io/rltoken/L7Bww_1KJOUrbES5YSLXbA) 
 ,  without the help of Google :
### General
* What’s a database
* What’s a relational database
* What does SQL stand for
* What’s MySQL
* How to create a database in MySQL
* What does  ` DDL `  and  ` DML `  stand for
* How to  ` CREATE `  or  ` ALTER `  a table
* How to  ` SELECT `  data from a table
* How to  ` INSERT ` ,  ` UPDATE `  or  ` DELETE `  data
* What are  ` subqueries ` 
* How to use MySQL functions
## Requirements
### General
* Allowed editors:  ` vi ` ,  ` vim ` ,  ` emacs ` 
* All your files will be executed on Ubuntu 20.04 LTS using  ` MySQL 8.0 `  (version 8.0.25)
* All your files should end with a new line
* All your SQL queries should have a comment just before (i.e. syntax above)
* All your files should start by a comment describing the task
* All SQL keywords should be in uppercase ( ` SELECT ` ,  ` WHERE ` …)
* A  ` README.md `  file, at the root of the folder of the project, is mandatory
* The length of your files will be tested using  ` wc ` 
## More Info
### Comments for your SQL file:
```bash
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$

```
### Install MySQL 8.0 on Ubuntu 20.04 LTS
```bash
$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$

```
Connect to your MySQL server:
```bash
$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
mysql> quit
Bye
$

```
### Use “container-on-demand” to run MySQL
In the container, credentials are  ` root/root ` 
* Ask for container  ` Ubuntu 20.04 ` 
* Connect via SSH
* OR connect via the Web terminal
* In the container, you should start MySQL before playing with it:
```bash
$ service mysql start                                                   
 * Starting MySQL database server mysqld 
$
$ cat 0-list_databases.sql | mysql -uroot -p                               
Database                                                                                   
information_schema                                                                         
mysql                                                                                      
performance_schema                                                                         
sys                      
$

```
In the container, credentials are  ` root/root ` 
## Quiz questions
Show
#### 
        
        Question #0
    
 Quiz question Body What does SQL stand for?
 Quiz question Answers * Sequences of Query Logic

* Structured Query Language

* Solid Query Language

* Structured Question Language

 Quiz question Tips #### 
        
        Question #1
    
 Quiz question Body What is a relational database? (please select all correct answers)
 Quiz question Answers * a database

* a collection of data

* married databases

* data are organized by tables, records and columns

* data are organized by tables and indexes

* a table containing multiple object representation 

* a table containing only one object representation

 Quiz question Tips #### 
        
        Question #2
    
 Quiz question Body What does DDL stand for?
 Quiz question Answers * Data Definition Language

* Database Definition Language

* Data Document Language

* Document Data Language

 Quiz question Tips #### 
        
        Question #3
    
 Quiz question Body What does DML stand for?
 Quiz question Answers * Database Manipulation Language

* Document Manipulation Language

* Data Manipulation Language

* Document Model Language

 Quiz question Tips #### 
        
        Question #4
    
 Quiz question Body How do you list all   ` users `   in this table?
```bash
+-------+-------------------------------------------------------------------------------------------------------------------------------+
| Table | Create Table                                                                                                                  |
+-------+-------------------------------------------------------------------------------------------------------------------------------+
| users | CREATE TABLE `users` (
  `id` int(11) DEFAULT NULL,
  `name` varchar(256) DEFAULT NULL,
  `age` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 |
+-------+-------------------------------------------------------------------------------------------------------------------------------+

```
 Quiz question Answers * DELETE * FROM users;

* SELECT * FROM users;

* SELECT ALL users;

 Quiz question Tips #### 
        
        Question #5
    
 Quiz question Body How to you add a new record in the table   ` users `  ?
```bash
+-------+-------------------------------------------------------------------------------------------------------------------------------+
| Table | Create Table                                                                                                                  |
+-------+-------------------------------------------------------------------------------------------------------------------------------+
| users | CREATE TABLE `users` (
  `id` int(11) DEFAULT NULL,
  `name` varchar(256) DEFAULT NULL,
  `age` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 |
+-------+-------------------------------------------------------------------------------------------------------------------------------+

```
 Quiz question Answers * INSERT users (id, name, age) VALUES (2, “Betty”, 30);

* INSERT INTO users (id, name) VALUES (2, “Betty”, 30);

* INSERT INTO users (id, name, age) VALUES (2, “Betty”, 30);

* INSERT INTO users (id, name, age) VALUES (2, “Betty”);

 Quiz question Tips #### 
        
        Question #6
    
 Quiz question Body How do you delete the   ` users `   record with   ` id = 89 `   in this table?
```bash
+-------+-------------------------------------------------------------------------------------------------------------------------------+
| Table | Create Table                                                                                                                  |
+-------+-------------------------------------------------------------------------------------------------------------------------------+
| users | CREATE TABLE `users` (
  `id` int(11) DEFAULT NULL,
  `name` varchar(256) DEFAULT NULL,
  `age` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 |
+-------+-------------------------------------------------------------------------------------------------------------------------------+

```
 Quiz question Answers * DELETE users WHERE id = 89;

* DELETE FROM users WHERE id = 89;

* DELETE FROM users;

* DELETE FROM users WHERE id IS EQUAL TO 89;

 Quiz question Tips #### 
        
        Question #7
    
 Quiz question Body How do you change the name of the   ` users `   record with   ` id = 89 `   to   ` Holberton `  ?
```bash
+-------+-------------------------------------------------------------------------------------------------------------------------------+
| Table | Create Table                                                                                                                  |
+-------+-------------------------------------------------------------------------------------------------------------------------------+
| users | CREATE TABLE `users` (
  `id` int(11) DEFAULT NULL,
  `name` varchar(256) DEFAULT NULL,
  `age` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 |
+-------+-------------------------------------------------------------------------------------------------------------------------------+

```
 Quiz question Answers * UPDATE users SET name = “Holberton” WHERE id = 89;

* CHANGE users SET name = “Holberton” WHERE id = 89;

* UPDATE users SET name = “Holberton”;

 Quiz question Tips #### 
        
        Question #8
    
 Quiz question Body How do you list all   ` users `   records with   ` age > 21 `   in this table?
```bash
+-------+-------------------------------------------------------------------------------------------------------------------------------+
| Table | Create Table                                                                                                                  |
+-------+-------------------------------------------------------------------------------------------------------------------------------+
| users | CREATE TABLE `users` (
  `id` int(11) DEFAULT NULL,
  `name` varchar(256) DEFAULT NULL,
  `age` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 |
+-------+-------------------------------------------------------------------------------------------------------------------------------+

```
 Quiz question Answers * SELECT * FROM users WHERE age < 21;

* SELECT * FROM users WHERE age IS UP TO 21;

* SELECT * FROM users WHERE age > 21;

* SELECT * FROM users WHERE age BETWEEN 21 AND 89;

 Quiz question Tips ## Tasks
### 0. List databases
          mandatory         Progress vs Score  Task Body Write a script that lists all databases of your MySQL server.
```bash
guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password: 
Database                                                                                     
hbtn_0c_0                                                                                    
information_schema                                                                           
mysql                                                                                        
performance_schema                                                                           
sys        
guillaume@ubuntu:~/$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x0D-SQL_introduction ` 
* File:  ` 0-list_databases.sql ` 
 Self-paced manual review  Panel footer - Controls 
### 1. Create a database
          mandatory         Progress vs Score  Task Body Write a script that creates the database   ` hbtn_0c_0 `   in your MySQL server.
* If the database  ` hbtn_0c_0 `  already exists, your script should not fail
* You are not allowed to use the  ` SELECT `  or  ` SHOW `  statements
```bash
guillaume@ubuntu:~/$ cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password: 
Database
information_schema
hbtn_0c_0
mysql
performance_schema
guillaume@ubuntu:~/$ cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x0D-SQL_introduction ` 
* File:  ` 1-create_database_if_missing.sql ` 
 Self-paced manual review  Panel footer - Controls 
### 2. Delete a database
          mandatory         Progress vs Score  Task Body Write a script that deletes the database   ` hbtn_0c_0 `   in your MySQL server.
* If the database  ` hbtn_0c_0 `  doesn’t exist, your script should not fail
* You are not allowed to use the  ` SELECT `  or  ` SHOW `  statements
```bash
guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password: 
Database                                                                                     
hbtn_0c_0                                                                                    
information_schema                                                                           
mysql                                                                                        
performance_schema                                                                           
sys        
guillaume@ubuntu:~/$ cat 2-remove_database.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password: 
Database                                                                                                                                                                  
information_schema                                                                           
mysql                                                                                        
performance_schema                                                                           
sys        
guillaume@ubuntu:~/$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x0D-SQL_introduction ` 
* File:  ` 2-remove_database.sql ` 
 Self-paced manual review  Panel footer - Controls 
### 3. List tables
          mandatory         Progress vs Score  Task Body Write a script that lists all the tables of a database in your MySQL server.
* The database name will be passed as argument of  ` mysql `  command (in the following example:  ` mysql `  is the name of the database)
```bash
guillaume@ubuntu:~/$ cat 3-list_tables.sql | mysql -hlocalhost -uroot -p mysql
Enter password: 
Tables_in_mysql                                                                              
columns_priv                                                                                 
component                                                                                    
db                                                                                           
default_roles                                                                                
engine_cost                                                                                  
func                                                                                         
general_log                                                                                  
global_grants                                                                                
gtid_executed                                                                                
help_category                                                                                
help_keyword                                                                                 
help_relation                                                                                
help_topic                                                                                   
innodb_index_stats                                                                           
innodb_table_stats                                                                           
password_history                                                                             
plugin                                                                                       
procs_priv                                                                                   
proxies_priv                                                                                 
replication_asynchronous_connection_failover                                                 
replication_asynchronous_connection_failover_managed                                         
role_edges                                                                                   
server_cost                                                                                  
servers                                                                                      
slave_master_info                                                                            
slave_relay_log_info                                                                         
slave_worker_info                                                                            
slow_log                                                                                     
tables_priv                                                                                  
time_zone                                                                                    
time_zone_leap_second                                                                        
time_zone_name                                                                               
time_zone_transition                                                                         
time_zone_transition_type                                                                    
user
guillaume@ubuntu:~/$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x0D-SQL_introduction ` 
* File:  ` 3-list_tables.sql ` 
 Self-paced manual review  Panel footer - Controls 
### 4. First table
          mandatory         Progress vs Score  Task Body Write a script that creates a table called   ` first_table `   in the current database in your MySQL server.
*  ` first_table `  description:*  ` id `  INT
*  ` name `  VARCHAR(256)

* The database name will be passed as an argument of the  ` mysql `  command
* If the table  ` first_table `  already exists, your script should not fail
* You are not allowed to use the  ` SELECT `  or  ` SHOW `  statements
```bash
guillaume@ubuntu:~/$ cat 4-first_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ cat 3-list_tables.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
Tables_in_hbtn_0c_0
first_table
guillaume@ubuntu:~/$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x0D-SQL_introduction ` 
* File:  ` 4-first_table.sql ` 
 Self-paced manual review  Panel footer - Controls 
### 5. Full description
          mandatory         Progress vs Score  Task Body Write a script that prints the full description of the table   ` first_table `   from the database   ` hbtn_0c_0 `   in your MySQL server.
* The database name will be passed as an argument of the  ` mysql `  command
* You are not allowed to use the  ` DESCRIBE `  or  ` EXPLAIN `  statements
```bash
guillaume@ubuntu:~/$ cat 5-full_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
Table   Create Table                                                                         
first_table     CREATE TABLE `first_table` (\n  `id` int DEFAULT NULL,\n  `name` varchar(256) DEFAULT NULL\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci        
guillaume@ubuntu:~/$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x0D-SQL_introduction ` 
* File:  ` 5-full_table.sql ` 
 Self-paced manual review  Panel footer - Controls 
### 6. List all in table
          mandatory         Progress vs Score  Task Body Write a script that lists all rows of the table   ` first_table `   from the database   ` hbtn_0c_0 `   in your MySQL server.
* All fields should be printed
* The database name will be passed as an argument of the  ` mysql `  command
```bash
guillaume@ubuntu:~/$ cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x0D-SQL_introduction ` 
* File:  ` 6-list_values.sql ` 
 Self-paced manual review  Panel footer - Controls 
### 7. First add
          mandatory         Progress vs Score  Task Body Write a script that inserts a new row in the table   ` first_table `   (database   ` hbtn_0c_0 `  ) in your MySQL server.
* New row:*  ` id `  =  ` 89 ` 
*  ` name `  =  ` Best School ` 

* The database name will be passed as an argument of the  ` mysql `  command
```bash
guillaume@ubuntu:~/$ cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
id  name
89  Best School
guillaume@ubuntu:~/$ cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
id  name
89  Best School
89  Best School
89  Best School
guillaume@ubuntu:~/$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x0D-SQL_introduction ` 
* File:  ` 7-insert_value.sql ` 
 Self-paced manual review  Panel footer - Controls 
### 8. Count 89
          mandatory         Progress vs Score  Task Body Write a script that displays the number of records with   ` id = 89 `   in the table   ` first_table `   of the database   ` hbtn_0c_0 `   in your MySQL server.
* The database name will be passed as an argument of the  ` mysql `  command
```bash
guillaume@ubuntu:~/$ cat 8-count_89.sql | mysql -hlocalhost -uroot -p hbtn_0c_0 | tail -1
Enter password: 
3
guillaume@ubuntu:~/$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x0D-SQL_introduction ` 
* File:  ` 8-count_89.sql ` 
 Self-paced manual review  Panel footer - Controls 
### 9. Full creation
          mandatory         Progress vs Score  Task Body Write a script that creates a table   ` second_table `   in the database   ` hbtn_0c_0 `   in your MySQL server and add multiples rows.
*  ` second_table `  description:*  ` id `  INT
*  ` name `  VARCHAR(256)
*  ` score `  INT

* The database name will be passed as an argument to the  ` mysql `  command
* If the table  ` second_table `  already exists, your script should not fail
* You are not allowed to use the  ` SELECT `  and  ` SHOW `  statements
* Your script should create these records:*  ` id `  = 1,  ` name `  = “John”,  ` score `  = 10
*  ` id `  = 2,  ` name `  = “Alex”,  ` score `  = 3
*  ` id `  = 3,  ` name `  = “Bob”,  ` score `  = 14
*  ` id `  = 4,  ` name `  = “George”,  ` score `  = 8

```bash
guillaume@ubuntu:~/$ cat 9-full_creation.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x0D-SQL_introduction ` 
* File:  ` 9-full_creation.sql ` 
 Self-paced manual review  Panel footer - Controls 
### 10. List by best
          mandatory         Progress vs Score  Task Body Write a script that lists all records of the table   ` second_table `   of the database   ` hbtn_0c_0 `   in your MySQL server.
* Results should display both the score and the name (in this order)
* Records should be ordered by score (top first) 
* The database name will be passed as an argument of the  ` mysql `  command
```bash
guillaume@ubuntu:~/$ cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   name
14  Bob
10  John
8   George
3   Alex
guillaume@ubuntu:~/$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x0D-SQL_introduction ` 
* File:  ` 10-top_score.sql ` 
 Self-paced manual review  Panel footer - Controls 
### 11. Select the best
          mandatory         Progress vs Score  Task Body Write a script that lists all records with a   ` score >= 10 `   in the table   ` second_table `   of the database   ` hbtn_0c_0 `   in your MySQL server.
* Results should display both the score and the name (in this order)
* Records should be ordered by score (top first)
* The database name will be passed as an argument of the  ` mysql `  command
```bash
guillaume@ubuntu:~/$ cat 11-best_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   name
14  Bob
10  John
guillaume@ubuntu:~/$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x0D-SQL_introduction ` 
* File:  ` 11-best_score.sql ` 
 Self-paced manual review  Panel footer - Controls 
### 12. Cheating is bad
          mandatory         Progress vs Score  Task Body Write a script that updates the score of Bob to   ` 10 `   in the table   ` second_table `  .
* You are not allowed to use Bob’s id value, only the  ` name `  field
* The database name will be passed as an argument of the  ` mysql `  command
```bash
guillaume@ubuntu:~/$ cat 12-no_cheating.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   name
10  John
10  Bob
8   George
3   Alex
guillaume@ubuntu:~/$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x0D-SQL_introduction ` 
* File:  ` 12-no_cheating.sql ` 
 Self-paced manual review  Panel footer - Controls 
### 13. Score too low
          mandatory         Progress vs Score  Task Body Write a script that removes all records with a   ` score <= 5 `   in the table   ` second_table `   of the database   ` hbtn_0c_0 `   in your MySQL server.
* The database name will be passed as an argument of the  ` mysql `  command
```bash
guillaume@ubuntu:~/$ cat 13-change_class.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   name
10  John
10  Bob
8   George
guillaume@ubuntu:~/$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x0D-SQL_introduction ` 
* File:  ` 13-change_class.sql ` 
 Self-paced manual review  Panel footer - Controls 
### 14. Average
          mandatory         Progress vs Score  Task Body Write a script that computes the score average of all records in the table   ` second_table `   of the database   ` hbtn_0c_0 `   in your MySQL server.
* The result column name should be  ` average ` 
* The database name will be passed as an argument of the  ` mysql `  command
```bash
guillaume@ubuntu:~/$ cat 14-average.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
average
9.3333
guillaume@ubuntu:~/$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x0D-SQL_introduction ` 
* File:  ` 14-average.sql ` 
 Self-paced manual review  Panel footer - Controls 
### 15. Number by score
          mandatory         Progress vs Score  Task Body Write a script that lists the number of records with the same score in the table   ` second_table `   of the database   ` hbtn_0c_0 `   in your MySQL server.
* The result should display:* the  ` score ` 
* the number of records for this  ` score `  with the label  ` number ` 

* The list should be sorted by the number of records (descending)
* The database name will be passed as an argument to the  ` mysql `  command
```bash
guillaume@ubuntu:~/$ cat 15-groups.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   number
10  2
8   1
guillaume@ubuntu:~/$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x0D-SQL_introduction ` 
* File:  ` 15-groups.sql ` 
 Self-paced manual review  Panel footer - Controls 
### 16. Say my name
          mandatory         Progress vs Score  Task Body Write a script that lists all records of the table   ` second_table `   of the database   ` hbtn_0c_0 `   in your MySQL server.
* Don’t list rows without a  ` name `  value
* Results should display the score and the name (in this order)
* Records should be listed by descending score 
* The database name will be passed as an argument to the  ` mysql `  command
In this example, new data have been added to the table   ` second_table `  .
```bash
guillaume@ubuntu:~/$ cat 16-no_link.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   name
18  Aria
12  Aria
10  John
10  Bob
guillaume@ubuntu:~/$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x0D-SQL_introduction ` 
* File:  ` 16-no_link.sql ` 
 Self-paced manual review  Panel footer - Controls 
[Done with the mandatory tasks? Unlock 4 advanced tasks now!](https://intranet.hbtn.io/projects/272/unlock_optionals) 

×#### Recommended Sandbox
[Running only]() 
### 1 image(0/5 Sandboxes spawned)
### Ubuntu 20.04
Basic Ubuntu 20.04, with vim, emacs, curl, wget and all needed for Holberton Foundations
[Run]() 
