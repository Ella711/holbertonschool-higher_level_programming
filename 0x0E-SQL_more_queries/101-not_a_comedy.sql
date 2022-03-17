-- Script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title
-- You can use a maximum of two SELECT statement
SELECT title
FROM tv_shows ts
WHERE ts.title NOT IN (
    SELECT ts2.title
    FROM tv_shows ts2
        INNER JOIN tv_show_genres tsg
            ON ts2.id = tsg.show_id
        INNER JOIN tv_genres tg
            ON tg.id = tsg.genre_id
    WHERE tg.name = "Comedy"
    )
ORDER BY ts.title ASC;
