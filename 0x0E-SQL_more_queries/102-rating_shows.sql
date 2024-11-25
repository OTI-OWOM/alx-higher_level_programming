-- List all shows sorted by their total rating
SELECT tv_shows.title, SUM(tv_show_rates.rate) AS rating
FROM tv_shows
JOIN tv_show_rates ON tv_shows.id = tv_show_rates.show_id
GROUP BY tv_shows.id, tv_shows.title
ORDER BY rating DESC;
