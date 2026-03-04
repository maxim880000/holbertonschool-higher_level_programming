-- Crée la table id_not_null : id vaut 1 par défaut si non renseigné
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
