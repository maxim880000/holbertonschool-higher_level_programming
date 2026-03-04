-- Liste toutes les villes avec le nom de leur état grâce à une jointure (JOIN)
-- JOIN (INNER JOIN) : combine les lignes de cities et states où cities.state_id = states.id
-- On affiche : l'id de la ville, le nom de la ville, le nom de l'état
-- ORDER BY cities.id ASC : tri par id de ville en ordre croissant
SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC;
