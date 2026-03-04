-- Liste toutes les séries qui ont au moins un genre associé
-- INNER JOIN : retourne uniquement les lignes qui ont une correspondance dans les deux tables
-- tv_shows JOIN tv_show_genres : on joint sur tv_shows.id = tv_show_genres.show_id
-- Seules les séries avec au moins un genre apparaissent (INNER JOIN exclut les séries sans genre)
-- ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC : tri alphabétique puis par genre
SELECT tv_shows.title, tv_show_genres.genre_id
    FROM tv_shows
    JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
    ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
