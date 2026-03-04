-- Liste tous les genres de la série "Dexter"
-- Première jointure : tv_show_genres JOIN tv_shows pour relier les genres à la série Dexter
-- Deuxième jointure : tv_genres JOIN tv_show_genres pour obtenir le nom du genre
-- WHERE tv_shows.title = 'Dexter' : filtre uniquement les entrées de la série Dexter
-- ORDER BY tv_genres.name ASC : tri alphabétique des genres
SELECT tv_genres.name
    FROM tv_genres
    JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
    JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
    WHERE tv_shows.title = 'Dexter'
    ORDER BY tv_genres.name ASC;
