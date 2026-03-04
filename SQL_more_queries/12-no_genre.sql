-- Liste toutes les séries qui n'ont aucun genre associé
-- LEFT JOIN : joint toutes les séries avec leurs genres éventuels
-- WHERE tv_show_genres.genre_id IS NULL : filtre uniquement les séries sans genre
-- (quand il n'y a pas de correspondance dans tv_show_genres, genre_id est NULL)
-- ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC : tri par titre
SELECT tv_shows.title, tv_show_genres.genre_id
    FROM tv_shows
    LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
    WHERE tv_show_genres.genre_id IS NULL
    ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
