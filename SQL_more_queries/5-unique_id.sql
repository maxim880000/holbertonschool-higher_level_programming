-- Crée la table unique_id : id est UNIQUE (pas de doublons), défaut 1
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
