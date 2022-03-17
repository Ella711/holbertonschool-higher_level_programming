-- Script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name
SELECT name
FROM tv_genres tg
WHERE tg.name NOT IN (
    SELECT tg2.name
    FROM tv_genres tg2
        INNER JOIN tv_show_genres tsg
            ON tg2.id = tsg.genre_id
        INNER JOIN tv_shows ts
            ON tsg.show_id = ts.id
    WHERE ts.title = "Dexter")
ORDER BY tg.name ASC;
