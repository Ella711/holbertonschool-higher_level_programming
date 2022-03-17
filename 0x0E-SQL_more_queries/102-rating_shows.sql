-- Script that lists all shows from hbtn_0d_tvshows_rate by their rating
-- Each record should display: tv_shows.title - rating sum
-- Results must be sorted in descending order by the rating
-- You can use only one SELECT statement
SELECT
       ts.title,
       SUM(tsr.rate) AS rating
FROM tv_shows ts
JOIN tv_show_ratings tsr
ON ts.id = tsr.show_id
GROUP BY ts.title
ORDER BY rating DESC;
