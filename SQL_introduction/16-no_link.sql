-- affiche les scores et noms non NULL triés par score décroissant
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;