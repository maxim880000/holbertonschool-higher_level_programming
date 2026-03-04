-- Crée la DB hbtn_0d_2 et user_0d_2 avec seulement le droit SELECT
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Crée l'utilisateur
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Donne uniquement le droit de lecture sur hbtn_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
