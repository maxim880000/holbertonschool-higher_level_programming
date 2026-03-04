-- Crée la table id_not_null avec une valeur par défaut pour la colonne id
-- CREATE TABLE IF NOT EXISTS : crée la table seulement si elle n'existe pas déjà
-- id INT DEFAULT 1 : si on n'insère pas de valeur pour id, il vaut automatiquement 1
-- name VARCHAR(256) : colonne de texte pouvant être NULL (aucune contrainte)
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
