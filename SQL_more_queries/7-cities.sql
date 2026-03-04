-- Crée la base de données hbtn_0d_usa et la table cities avec une clé étrangère
-- CREATE DATABASE IF NOT EXISTS : crée la base si elle n'existe pas encore
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- USE : sélectionne la base de données hbtn_0d_usa
USE hbtn_0d_usa;

-- CREATE TABLE IF NOT EXISTS : crée la table cities si elle n'existe pas déjà
-- id INT AUTO_INCREMENT PRIMARY KEY : identifiant unique auto-incrémenté, clé primaire
-- state_id INT NOT NULL : référence obligatoire à l'état auquel appartient la ville
-- FOREIGN KEY (state_id) REFERENCES states(id) : contrainte de clé étrangère
--   -> state_id doit toujours correspondre à un id existant dans la table states
--   -> empêche d'insérer une ville pour un état qui n'existe pas
-- name VARCHAR(256) NOT NULL : le nom de la ville est obligatoire
CREATE TABLE IF NOT EXISTS cities (
    id INT NOT NULL AUTO_INCREMENT,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (state_id) REFERENCES states(id)
);
