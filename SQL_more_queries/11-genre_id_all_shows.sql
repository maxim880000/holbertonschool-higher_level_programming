-- Liste toutes les séries avec leur genre_id, ou NULL si elles n'ont pas de genre
-- LEFT JOIN : retourne TOUTES les lignes de tv_shows (table gauche)
-- même si elles n'ont pas de correspondance dans tv_show_genres
-- Si une série n'a pas de genre, tv_show_genres.genre_id sera NULL
-- ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC : tri par titre puis par genre
SELECT tv_shows.title, tv_show_genres.genre_id
    FROM tv_shows
    LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
    ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
