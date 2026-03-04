-- Crée la base de données hbtn_0d_usa et la table states
-- CREATE DATABASE IF NOT EXISTS : crée la base de données si elle n'existe pas encore
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- USE : sélectionne la base de données dans laquelle on va créer la table
USE hbtn_0d_usa;

-- CREATE TABLE IF NOT EXISTS : crée la table states si elle n'existe pas déjà
-- id INT : colonne entière
-- NOT NULL : la colonne id ne peut jamais être NULL
-- AUTO_INCREMENT : la valeur de id s'incrémente automatiquement à chaque insertion
-- PRIMARY KEY : id est la clé primaire (identifiant unique de chaque ligne)
-- name VARCHAR(256) NOT NULL : le nom de l'état est obligatoire
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
