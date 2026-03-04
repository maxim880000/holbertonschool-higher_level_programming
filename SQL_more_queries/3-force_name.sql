-- Crée la table force_name avec une contrainte NOT NULL sur la colonne name
-- CREATE TABLE IF NOT EXISTS : crée la table seulement si elle n'existe pas déjà
-- id INT : colonne entière sans contrainte particulière
-- name VARCHAR(256) NOT NULL : la colonne name ne peut jamais être NULL (obligatoire)
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
