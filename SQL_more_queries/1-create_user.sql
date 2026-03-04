-- Crée l'utilisateur user_0d_1 avec tous les privilèges sur le serveur MySQL
-- CREATE USER IF NOT EXISTS : crée l'utilisateur seulement s'il n'existe pas déjà (évite l'erreur)
-- IDENTIFIED BY : définit le mot de passe de l'utilisateur
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- GRANT ALL PRIVILEGES : accorde tous les droits (lecture, écriture, création, suppression...)
-- ON *.* : sur toutes les bases de données et toutes les tables
-- WITH GRANT OPTION : permet à user_0d_1 de donner des droits à d'autres utilisateurs
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
