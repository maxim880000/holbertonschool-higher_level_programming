-- Liste toutes les villes de Californie en utilisant une sous-requête (sans JOIN)
-- On cherche d'abord l'id de la Californie dans la table states (sous-requête)
-- puis on récupère toutes les villes dont le state_id correspond à cet id
-- ORDER BY cities.id ASC : tri des résultats par id de ville croissant
SELECT id, name
    FROM cities
    WHERE state_id = (
        SELECT id
        FROM states
        WHERE name = 'California'
    )
    ORDER BY id ASC;
