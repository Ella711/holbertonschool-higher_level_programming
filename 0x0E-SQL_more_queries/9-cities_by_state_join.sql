-- Script that lists all cities contained in the database hbtn_0d_usa
-- Each record should display: cities.id - cities.name - states.name
-- Results must be sorted by asc order by cities.id
-- Can only use one SELECT statement
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON states.id = cities.state_id
ORDER BY cities.id ASC;
