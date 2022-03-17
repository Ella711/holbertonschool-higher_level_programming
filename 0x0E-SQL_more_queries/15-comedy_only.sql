-- Script that lists all Comedy shows in the database hbtn_0d_tvshows
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title
SELECT title
FROM tv_shows ts
JOIN tv_show_genres tsg
ON ts.id = tsg.show_id
JOIN tv_genres tg
ON tg.id = tsg.genre_id
WHERE tg.name = "Comedy"
ORDER BY ts.title ASC;
