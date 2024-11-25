-- List all genres sorted by their total rating
SELECT tv_genres.name, SUM(tv_show_rates.rate) AS rating
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
JOIN tv_show_rates ON tv_shows.id = tv_show_rates.show_id
GROUP BY tv_genres.id, tv_genres.name
ORDER BY rating DESC;
