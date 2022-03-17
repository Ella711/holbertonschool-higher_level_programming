-- script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name
-- You can use only one SELECT statement
SELECT tg.name
FROM tv_genres tg
JOIN tv_show_genres tsg
ON tg.id = tsg.genre_id
JOIN tv_shows ts
ON tsg.show_id = ts.id
WHERE ts.id = 8
ORDER BY tg.name ASC;