-- Liste toutes les séries du genre "Comedy"
-- Première jointure : tv_show_genres JOIN tv_genres pour relier les séries aux genres
-- Deuxième jointure : tv_shows JOIN tv_show_genres pour obtenir le titre de chaque série
-- WHERE tv_genres.name = 'Comedy' : filtre uniquement les séries liées au genre Comédie
-- ORDER BY tv_shows.title ASC : tri alphabétique des titres de séries
SELECT tv_shows.title
    FROM tv_shows
    JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
    JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
    WHERE tv_genres.name = 'Comedy'
    ORDER BY tv_shows.title ASC;
