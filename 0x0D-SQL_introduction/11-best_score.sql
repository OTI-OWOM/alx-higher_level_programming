-- List records with score >= 10, ordered by score from highest to lowest
SELECT score, name 
FROM second_table 
WHERE score >= 10 
ORDER BY score DESC;
