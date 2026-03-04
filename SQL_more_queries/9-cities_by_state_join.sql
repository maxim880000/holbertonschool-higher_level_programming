-- Toutes les villes avec le nom de leur état via JOIN
SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC;
