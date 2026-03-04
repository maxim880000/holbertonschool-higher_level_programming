-- Liste toutes les séries avec leurs genres associés, ou NULL si pas de genre
-- LEFT JOIN tv_show_genres : garde TOUTES les séries, même sans genre (genre sera NULL)
-- LEFT JOIN tv_genres : récupère le nom du genre si disponible
-- ORDER BY tv_shows.title ASC, tv_genres.name ASC : tri par titre de série puis par genre
SELECT tv_shows.title, tv_genres.name
    FROM tv_shows
    LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
    LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
    ORDER BY tv_shows.title ASC, tv_genres.name ASC;
