-- Crée la table unique_id avec une contrainte UNIQUE sur la colonne id
-- CREATE TABLE IF NOT EXISTS : crée la table seulement si elle n'existe pas déjà
-- id INT DEFAULT 1 UNIQUE : valeur par défaut 1, et chaque valeur doit être unique dans la table
-- UNIQUE empêche d'insérer deux lignes avec le même id
-- name VARCHAR(256) : colonne de texte sans contrainte particulière
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
