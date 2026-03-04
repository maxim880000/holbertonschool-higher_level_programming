-- Compte le nombre de séries par genre
-- INNER JOIN : joint tv_genres avec tv_show_genres pour avoir le nom du genre et le show_id
-- COUNT(*) : compte le nombre de lignes (= nombre de séries) pour chaque groupe
-- GROUP BY tv_genres.name : groupe les résultats par nom de genre
-- AS genre / AS number_of_shows : renomme les colonnes pour l'affichage
-- ORDER BY number_of_shows DESC : tri du genre le plus populaire au moins populaire
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
    FROM tv_genres
    JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
    GROUP BY tv_genres.name
    ORDER BY number_of_shows DESC;
