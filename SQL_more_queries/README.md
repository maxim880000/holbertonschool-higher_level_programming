# SQL - More Queries

## Description

Ce projet explore les fonctionnalités avancées de MySQL : gestion des utilisateurs et des privilèges, contraintes sur les tables (PRIMARY KEY, FOREIGN KEY, NOT NULL, UNIQUE), et les requêtes multi-tables avec JOIN, LEFT JOIN, et les sous-requêtes.

---

## Ressources utiles

- [How To Create a New User and Grant Permissions in MySQL](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql)
- [MySQL GRANT Statement](https://dev.mysql.com/doc/refman/8.0/en/grant.html)
- [MySQL Constraints](https://dev.mysql.com/doc/refman/8.0/en/constraints.html)
- [SQL JOIN types](https://dev.mysql.com/doc/refman/8.0/en/join.html)
- [MySQL 8.0 SQL Statement Syntax](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)

---

## Objectifs d'apprentissage

- Créer un nouvel utilisateur MySQL
- Gérer les privilèges d'un utilisateur sur une base de données ou une table
- Comprendre ce qu'est une **PRIMARY KEY** (clé primaire)
- Comprendre ce qu'est une **FOREIGN KEY** (clé étrangère)
- Utiliser les contraintes **NOT NULL** et **UNIQUE**
- Récupérer des données depuis plusieurs tables en une seule requête
- Utiliser les **sous-requêtes**
- Utiliser **JOIN** et **UNION**

---

## Prérequis

- Ubuntu 20.04 LTS
- MySQL 8.0 (version 8.0.25)
- Tous les fichiers se terminent par une nouvelle ligne
- Tous les mots-clés SQL sont en MAJUSCULES
- Chaque fichier commence par un commentaire décrivant la tâche

---

## Connexion à MySQL

```bash
# Connexion en root
sudo mysql

# Connexion avec identifiants
mysql -hlocalhost -uroot -p

# Exécuter un fichier SQL
cat fichier.sql | mysql -hlocalhost -uroot -p
```

---

## Structure des bases de données utilisées

### Base `hbtn_0d_usa`
```
states
├── id    (INT, PRIMARY KEY, AUTO_INCREMENT, NOT NULL)
└── name  (VARCHAR(256), NOT NULL)

cities
├── id        (INT, PRIMARY KEY, AUTO_INCREMENT, NOT NULL)
├── state_id  (INT, NOT NULL, FOREIGN KEY → states.id)
└── name      (VARCHAR(256), NOT NULL)
```

### Base `hbtn_0d_tvshows`
```
tv_shows
├── id     (INT, PRIMARY KEY)
└── title  (VARCHAR(256))

tv_genres
├── id    (INT, PRIMARY KEY)
└── name  (VARCHAR(256))

tv_show_genres
├── show_id   (INT, FOREIGN KEY → tv_shows.id)
└── genre_id  (INT, FOREIGN KEY → tv_genres.id)
```

---

## Tableau récapitulatif de toutes les commandes SQL utilisées

| # | Fichier | Commandes SQL utilisées | Description |
|---|---------|------------------------|-------------|
| 0 | `0-privileges.sql` | `SHOW GRANTS FOR` | Affiche les privilèges d'un utilisateur sur le serveur |
| 1 | `1-create_user.sql` | `CREATE USER IF NOT EXISTS`, `GRANT ALL PRIVILEGES ON *.* TO ... WITH GRANT OPTION` | Crée un utilisateur avec tous les droits |
| 2 | `2-create_read_user.sql` | `CREATE DATABASE IF NOT EXISTS`, `CREATE USER IF NOT EXISTS`, `GRANT SELECT ON db.*` | Crée une DB et un utilisateur en lecture seule |
| 3 | `3-force_name.sql` | `CREATE TABLE IF NOT EXISTS`, `NOT NULL` | Crée une table avec une colonne obligatoire |
| 4 | `4-never_empty.sql` | `CREATE TABLE IF NOT EXISTS`, `DEFAULT 1` | Crée une table avec une valeur par défaut |
| 5 | `5-unique_id.sql` | `CREATE TABLE IF NOT EXISTS`, `DEFAULT 1`, `UNIQUE` | Crée une table avec une contrainte d'unicité |
| 6 | `6-states.sql` | `CREATE DATABASE IF NOT EXISTS`, `USE`, `CREATE TABLE IF NOT EXISTS`, `AUTO_INCREMENT`, `PRIMARY KEY`, `NOT NULL` | Crée une DB et une table avec clé primaire auto-incrémentée |
| 7 | `7-cities.sql` | `CREATE DATABASE IF NOT EXISTS`, `USE`, `CREATE TABLE IF NOT EXISTS`, `AUTO_INCREMENT`, `PRIMARY KEY`, `FOREIGN KEY ... REFERENCES` | Crée une table avec clé étrangère |
| 8 | `8-cities_of_california_subquery.sql` | `SELECT`, `WHERE ... = (SELECT ...)` | Sous-requête : récupère l'id de la Californie puis filtre les villes |
| 9 | `9-cities_by_state_join.sql` | `SELECT`, `JOIN ... ON`, `ORDER BY` | JOIN : combine cities et states pour afficher le nom de l'état |
| 10 | `10-genre_id_by_show.sql` | `SELECT`, `JOIN ... ON`, `ORDER BY` | INNER JOIN : séries ayant au moins un genre |
| 11 | `11-genre_id_all_shows.sql` | `SELECT`, `LEFT JOIN ... ON`, `ORDER BY` | LEFT JOIN : toutes les séries, NULL si pas de genre |
| 12 | `12-no_genre.sql` | `SELECT`, `LEFT JOIN ... ON`, `WHERE ... IS NULL`, `ORDER BY` | LEFT JOIN + IS NULL : séries sans genre uniquement |
| 13 | `13-count_shows_by_genre.sql` | `SELECT`, `JOIN ... ON`, `COUNT(*)`, `GROUP BY`, `ORDER BY DESC` | JOIN + GROUP BY + COUNT : nombre de séries par genre |
| 14 | `14-my_genres.sql` | `SELECT`, `JOIN ... ON` (double jointure), `WHERE`, `ORDER BY` | Double JOIN : genres de la série Dexter |
| 15 | `15-comedy_only.sql` | `SELECT`, `JOIN ... ON` (double jointure), `WHERE`, `ORDER BY` | Double JOIN : séries du genre Comedy |
| 16 | `16-shows_by_genre.sql` | `SELECT`, `LEFT JOIN ... ON` (double), `ORDER BY` | Double LEFT JOIN : séries avec genres ou NULL |

---

## Détail des commandes SQL importantes

### Gestion des utilisateurs

```sql
-- Afficher les privilèges d'un utilisateur
SHOW GRANTS FOR 'user'@'localhost';

-- Créer un utilisateur (sans erreur si existe déjà)
CREATE USER IF NOT EXISTS 'user'@'localhost' IDENTIFIED BY 'password';

-- Accorder tous les privilèges
GRANT ALL PRIVILEGES ON *.* TO 'user'@'localhost' WITH GRANT OPTION;

-- Accorder uniquement SELECT sur une base
GRANT SELECT ON database_name.* TO 'user'@'localhost';
```

### Contraintes de table

```sql
-- Colonne obligatoire (ne peut pas être NULL)
name VARCHAR(256) NOT NULL

-- Valeur par défaut
id INT DEFAULT 1

-- Valeur unique (pas de doublon)
id INT UNIQUE

-- Clé primaire auto-incrémentée
id INT NOT NULL AUTO_INCREMENT,
PRIMARY KEY (id)

-- Clé étrangère (référence une autre table)
state_id INT NOT NULL,
FOREIGN KEY (state_id) REFERENCES states(id)
```

### Types de JOIN

```sql
-- INNER JOIN : seulement les lignes avec correspondance dans les deux tables
SELECT * FROM table1
JOIN table2 ON table1.id = table2.fk_id;

-- LEFT JOIN : toutes les lignes de la table gauche + correspondances (NULL si aucune)
SELECT * FROM table1
LEFT JOIN table2 ON table1.id = table2.fk_id;

-- Filtrer les lignes sans correspondance (après LEFT JOIN)
WHERE table2.id IS NULL
```

### Sous-requêtes

```sql
-- Utiliser le résultat d'une requête dans une autre (sans JOIN)
SELECT id, name FROM cities
WHERE state_id = (
    SELECT id FROM states WHERE name = 'California'
);
```

### Agrégation et groupement

```sql
-- Compter le nombre de lignes par groupe
SELECT genre_name, COUNT(*) AS number_of_shows
FROM table
GROUP BY genre_name
ORDER BY number_of_shows DESC;
```

---

## Importer un dump SQL

```bash
# Créer la base de données
echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p

# Importer le dump
curl "https://url_du_dump.sql" -s | mysql -uroot -p hbtn_0d_tvshows
```

---

## Auteur

- **Holberton School** - Projet SQL More Queries
