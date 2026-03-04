-- Crée la base de données hbtn_0d_2 et l'utilisateur user_0d_2 avec seulement le droit SELECT
-- CREATE DATABASE IF NOT EXISTS : crée la base seulement si elle n'existe pas encore
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- CREATE USER IF NOT EXISTS : crée l'utilisateur seulement s'il n'existe pas déjà
-- IDENTIFIED BY : définit le mot de passe de l'utilisateur
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- GRANT SELECT : accorde uniquement le droit de lecture (SELECT) à user_0d_2
-- ON hbtn_0d_2.* : sur toutes les tables de la base de données hbtn_0d_2 uniquement
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
