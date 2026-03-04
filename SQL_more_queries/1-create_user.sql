-- Crée user_0d_1 avec tous les privilèges sur le serveur
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- GRANT ALL + WITH GRANT OPTION : peut aussi donner des droits à d'autres
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
