# ��️ SQL Introduction — Guide Complet & Ultra-Détaillé

> **Projet :** holbertonschool-higher_level_programming / SQL_introduction  
> **Technologie :** MySQL (MariaDB compatible)  
> **Niveau :** Débutant → Intermédiaire  

---

## 📚 Table des Matières

1. [Qu'est-ce qu'une Base de Données SQL ?](#1--quest-ce-quune-base-de-données-sql-)
2. [Concepts Fondamentaux](#2--concepts-fondamentaux)
3. [Architecture d'une Base de Données Relationnelle](#3--architecture-dune-base-de-données-relationnelle)
4. [Les Types de Données MySQL](#4--les-types-de-données-mysql)
5. [Analyse de chaque fichier SQL du projet](#5--analyse-de-chaque-fichier-sql-du-projet)
6. [Les Catégories de Commandes SQL (DDL, DML, DQL, DCL)](#6--les-catégories-de-commandes-sql-ddl-dml-dql-dcl)
7. [Tableau Géant de Référence — Toutes les Commandes SQL](#7--tableau-géant-de-référence--toutes-les-commandes-sql)

---

## 1 — Qu'est-ce qu'une Base de Données SQL ?

### 🔎 Définition

Une **base de données** est un système organisé permettant de **stocker, gérer et récupérer des données** de manière structurée et efficace. Elle peut contenir des millions, voire des milliards de lignes de données accessibles en millisecondes.

**SQL** (**S**tructured **Q**uery **L**anguage) est le **langage standard** utilisé pour interagir avec les bases de données relationnelles. Il permet de :
- 📥 **Insérer** des données
- 🔍 **Interroger** des données (faire des recherches)
- ✏️ **Modifier** des données
- 🗑️ **Supprimer** des données
- 🏗️ **Créer** la structure (tables, bases, index...)

### 🏛️ Bases de Données Relationnelles

Le modèle **relationnel** (inventé par Edgar F. Codd en 1970) organise les données sous forme de **tables** (aussi appelées *relations*). Chaque table est composée de :
- **Colonnes** (ou *champs*) → définissent la structure (ex : `id`, `name`, `score`)
- **Lignes** (ou *enregistrements* / *tuples*) → contiennent les données réelles

Les tables peuvent être **liées entre elles** via des clés (clé primaire / clé étrangère), ce qui évite la duplication d'information (**normalisation**).

### 💡 Pourquoi SQL ?

| Avantage | Description |
|---|---|
| **Standardisé** | SQL est un standard ISO/ANSI utilisé par tous les SGBD majeurs |
| **Puissant** | Permet des requêtes complexes sur des millions de lignes en quelques ms |
| **Fiable** | Transactions ACID garantissant l'intégrité des données |
| **Universel** | MySQL, PostgreSQL, SQLite, Oracle, SQL Server utilisent tous SQL |

### 🏢 Systèmes de Gestion de Bases de Données (SGBD)

| SGBD | Éditeur | Usage typique |
|---|---|---|
| **MySQL** | Oracle | Web, applications générales |
| **PostgreSQL** | Open Source | Applications complexes, JSON, extensions |
| **SQLite** | Open Source | Applications mobiles, fichiers locaux |
| **MariaDB** | Open Source (fork MySQL) | Serveurs web (LAMP) |
| **Oracle Database** | Oracle | Entreprises, banques |
| **Microsoft SQL Server** | Microsoft | Environnements Windows/.NET |

> 🎯 **Ce projet utilise MySQL.** Toutes les commandes présentées sont compatibles MySQL/MariaDB.

---

## 2 — Concepts Fondamentaux

### 🗂️ Base de Données (Database)

Une base de données est un **conteneur logique** qui regroupe un ensemble de tables liées.

```
MySQL Server
│
├── hbtn_0c_0
│   ├── first_table
│   ├── second_table
│   └── ...
│
└── autre_base
    └── ...
```

### 📋 Table

Une table est une structure **bidimensionnelle** (lignes × colonnes) qui stocke les données :

```
Table: second_table
┌────┬────────┬───────┐
│ id │  name  │ score │
├────┼────────┼───────┤
│  1 │ John   │   10  │
│  2 │ Alex   │    3  │
│  3 │ Bob    │   14  │
│  4 │ George │    8  │
└────┴────────┴───────┘
```

### 🔑 Clé Primaire (Primary Key)

Un champ qui **identifie de manière unique** chaque ligne. Elle ne peut pas être NULL ni dupliquée.

### 🔗 Clé Étrangère (Foreign Key)

Un champ d'une table qui **référence la clé primaire** d'une autre table, créant un lien entre elles.

### ⚙️ Transactions ACID

- **A**tomicité : une transaction réussit entièrement ou échoue entièrement
- **C**ohérence : la base reste dans un état valide avant et après la transaction
- **I**solation : les transactions concurrentes n'interfèrent pas entre elles
- **D**urabilité : une transaction validée est définitivement enregistrée

---

## 3 — Architecture d'une Base de Données Relationnelle

```
┌─────────────────────────────────────────────────────┐
│                   CLIENT (vous)                     │
│  mysql -u root -p hbtn_0c_0 < fichier.sql           │
└─────────────────────┬───────────────────────────────┘
                      │  Requête SQL
                      ▼
┌─────────────────────────────────────────────────────┐
│               SERVEUR MySQL                         │
│  ┌──────────────────────────────────────────────┐   │
│  │     Parseur SQL (analyse la syntaxe)         │   │
│  └──────────────────┬───────────────────────────┘   │
│  ┌──────────────────▼───────────────────────────┐   │
│  │       Optimiseur de requêtes                 │   │
│  └──────────────────┬───────────────────────────┘   │
│  ┌──────────────────▼───────────────────────────┐   │
│  │   Moteur de stockage InnoDB                  │   │
│  └──────────────────┬───────────────────────────┘   │
└─────────────────────┼───────────────────────────────┘
                      ▼
              📁 Fichiers sur disque
```

---

## 4 — Les Types de Données MySQL

| Type | Description | Exemple |
|---|---|---|
| `INT` | Entier signé (−2 147 483 648 à 2 147 483 647) | `42`, `-7`, `1000` |
| `VARCHAR(n)` | Chaîne de caractères variable, max `n` caractères | `'Hello'`, `'Bob'` |
| `FLOAT` | Nombre décimal à virgule flottante | `3.14`, `-0.5` |
| `DOUBLE` | Décimal double précision | `3.14159265358979` |
| `DECIMAL(p,s)` | Décimal exact, `p` chiffres total, `s` après virgule | `19.99` |
| `BOOLEAN` / `TINYINT(1)` | Vrai/Faux (0 ou 1) | `TRUE`, `FALSE` |
| `DATE` | Date (AAAA-MM-JJ) | `'2026-03-04'` |
| `DATETIME` | Date + heure (AAAA-MM-JJ HH:MM:SS) | `'2026-03-04 14:30:00'` |
| `TEXT` | Texte long (jusqu'à 65 535 caractères) | Paragraphes, descriptions |
| `NULL` | Absence de valeur | — |

---

## 5 — Analyse de chaque fichier SQL du projet

---

### `0-list_databases.sql`

```sql
-- List all databases
SHOW DATABASES;
```

#### 🔍 Explication détaillée

| Élément | Rôle |
|---|---|
| `-- List all databases` | **Commentaire SQL** — ligne commençant par `--`, ignorée par MySQL, sert de documentation |
| `SHOW DATABASES;` | **Commande MySQL** qui liste toutes les bases de données existantes sur le serveur |
| `;` | **Point-virgule** — termine chaque instruction SQL (obligatoire) |

#### ▶️ Comment l'utiliser

```bash
mysql -u root -p < 0-list_databases.sql
# ou en interactif :
mysql -u root -p
mysql> SHOW DATABASES;
```

#### 📤 Résultat typique

```
+--------------------+
| Database           |
+--------------------+
| information_schema |
| hbtn_0c_0          |
| mysql              |
| performance_schema |
+--------------------+
```

> 💡 `information_schema`, `mysql`, `performance_schema` sont des bases **système** créées automatiquement par MySQL. Ne pas les modifier.

---

### `1-create_database_if_missing.sql`

```sql
-- CREATES db (hbtn_0c_0) in MySQL server
CREATE DATABASE IF NOT EXISTS hbtn_0c_0;
```

#### 🔍 Explication détaillée

| Élément | Rôle |
|---|---|
| `CREATE DATABASE` | Crée une nouvelle base de données |
| `IF NOT EXISTS` | **Clause de sécurité** — si la base existe déjà, MySQL ne génère pas d'erreur |
| `hbtn_0c_0` | Nom de la base de données à créer |

#### Comparaison avec / sans IF NOT EXISTS

```sql
-- Sans IF NOT EXISTS → ERREUR si la base existe déjà
CREATE DATABASE hbtn_0c_0;
-- ERROR: Can't create database 'hbtn_0c_0'; database exists

-- Avec IF NOT EXISTS → Aucune erreur, ignoré silencieusement
CREATE DATABASE IF NOT EXISTS hbtn_0c_0;
```

> 💡 **Bonne pratique** : toujours utiliser `IF NOT EXISTS` pour rendre les scripts **idempotents** (exécutables plusieurs fois sans erreur).

---

### `2-remove_database.sql`

```sql
-- supprime la base de données hbtn_0c_0 si elle existe
DROP DATABASE IF EXISTS hbtn_0c_0;
```

#### 🔍 Explication détaillée

| Élément | Rôle |
|---|---|
| `DROP DATABASE` | **Supprime définitivement** une base de données entière avec toutes ses tables et données |
| `IF EXISTS` | Si la base n'existe pas, ne génère pas d'erreur |
| `hbtn_0c_0` | Nom de la base à supprimer |

#### ⚠️ DANGER — Commande irréversible

```
DROP DATABASE hbtn_0c_0;
→ Supprime : first_table, second_table, et TOUTES leurs données
→ Impossible de récupérer sans sauvegarde (backup)
```

> 🛡️ **Bonne pratique** : Toujours faire un `mysqldump` avant de dropper une base en production.

---

### `3-list_tables.sql`

```sql
-- lists all the tables of a database in your MySQL server
SHOW TABLES;
```

#### 🔍 Explication détaillée

| Élément | Rôle |
|---|---|
| `SHOW TABLES` | Liste toutes les tables de la **base de données actuellement sélectionnée** |

#### ▶️ Comment l'utiliser

```bash
# On spécifie la base en argument de connexion
mysql -u root -p hbtn_0c_0 < 3-list_tables.sql
```

#### 📤 Résultat typique

```
+---------------------+
| Tables_in_hbtn_0c_0 |
+---------------------+
| first_table         |
| second_table        |
+---------------------+
```

> 💡 Si aucune base n'est sélectionnée, MySQL retourne l'erreur `No database selected`.

---

### `4-first_table.sql`

```sql
-- creates a table called first_table in the current database
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
```

#### 🔍 Explication détaillée

| Élément | Rôle |
|---|---|
| `CREATE TABLE` | Crée une nouvelle table dans la base de données courante |
| `IF NOT EXISTS` | Ne génère pas d'erreur si la table existe déjà |
| `first_table` | Nom de la table à créer |
| `(...)` | **Définition des colonnes** — entre parenthèses |
| `id INT` | Colonne `id` de type entier |
| `name VARCHAR(256)` | Colonne `name`, chaîne de caractères max 256 chars |
| `,` | Séparateur entre les définitions de colonnes |

#### 📊 Structure créée

```
Table: first_table
┌──────────────┬───────────────┐
│ Colonne      │ Type          │
├──────────────┼───────────────┤
│ id           │ INT           │
│ name         │ VARCHAR(256)  │
└──────────────┴───────────────┘
```

#### 💡 Version améliorée avec contraintes

```sql
CREATE TABLE IF NOT EXISTS first_table (
    id   INT          NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
```
- `NOT NULL` → la valeur ne peut pas être vide
- `AUTO_INCREMENT` → l'id s'incrémente automatiquement à chaque insertion
- `PRIMARY KEY` → identifiant unique pour chaque ligne

---

### `5-full_table.sql`

```sql
-- affiche la structure complète de la table first_table
SHOW CREATE TABLE first_table;
```

#### 🔍 Explication détaillée

| Élément | Rôle |
|---|---|
| `SHOW CREATE TABLE` | Affiche la requête SQL complète qui a créé la table (moteur, encodage, etc.) |
| `first_table` | Nom de la table à inspecter |

#### 📤 Résultat typique

```
| first_table | CREATE TABLE `first_table` (
    `id` int DEFAULT NULL,
    `name` varchar(256) DEFAULT NULL
  ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 |
```

> 💡 `utf8mb4` = support des emojis et caractères spéciaux. `InnoDB` = moteur avec support transactions et clés étrangères.

**Alternative utile :**
```sql
DESCRIBE first_table;  -- ou : DESC first_table;
```
Affiche un tableau résumé : nom de colonne, type, NULL autorisé, clé, valeur par défaut.

---

### `6-list_values.sql`

```sql
-- lists all rows of the table first_table
SELECT * FROM first_table
```

#### 🔍 Explication détaillée

| Élément | Rôle |
|---|---|
| `SELECT` | **Commande de lecture** — récupère des données depuis une ou plusieurs tables |
| `*` | **Joker** — signifie "toutes les colonnes" |
| `FROM` | Indique la **source des données** |
| `first_table` | Nom de la table à lire |

#### Variantes de SELECT

```sql
SELECT id, name FROM first_table;              -- Colonnes spécifiques
SELECT id AS identifiant, name AS prenom FROM first_table;  -- Avec alias
SELECT * FROM first_table WHERE id = 89;       -- Avec filtre
SELECT * FROM first_table ORDER BY name ASC;   -- Avec tri
SELECT * FROM first_table LIMIT 5;             -- Limité à 5 résultats
```

> 💡 **Bonne pratique** : Éviter `SELECT *` en production — nommer explicitement les colonnes est plus efficace.

---

### `7-insert_value.sql`

```sql
-- inserts a new row in the table first_table
INSERT INTO first_table (id, name) VALUES (89, 'Best School');
```

#### 🔍 Explication détaillée

| Élément | Rôle |
|---|---|
| `INSERT INTO` | **Commande d'insertion** — ajoute une ou plusieurs lignes dans une table |
| `first_table` | Nom de la table cible |
| `(id, name)` | **Liste des colonnes** à remplir |
| `VALUES` | Introduit les valeurs à insérer |
| `(89, 'Best School')` | Valeurs correspondant aux colonnes : `id=89`, `name='Best School'` |

#### Syntaxes alternatives

```sql
-- Sans préciser les colonnes (risqué)
INSERT INTO first_table VALUES (89, 'Best School');

-- Insertion multiple (plus efficace)
INSERT INTO first_table (id, name) VALUES
    (1, 'Alice'),
    (2, 'Bob'),
    (3, 'Charlie');

-- Syntaxe SET (MySQL uniquement)
INSERT INTO first_table SET id = 89, name = 'Best School';
```

> 💡 Toujours préciser la liste des colonnes pour éviter les erreurs si la structure change.

---

### `8-count_89.sql`

```sql
-- compte le nombre d'enregistrements avec id = 89 dans first_table
SELECT COUNT(*) FROM first_table WHERE id = 89;
```

#### 🔍 Explication détaillée

| Élément | Rôle |
|---|---|
| `COUNT(*)` | **Fonction d'agrégation** — compte le nombre de lignes correspondant aux critères |
| `FROM first_table` | Source des données |
| `WHERE id = 89` | **Clause de filtrage** — ne compte que les lignes où `id` vaut 89 |

#### Les fonctions d'agrégation

```sql
COUNT(*)       -- Nombre total de lignes (inclut NULL)
COUNT(colonne) -- Nombre de lignes non-NULL dans la colonne
SUM(colonne)   -- Somme des valeurs
AVG(colonne)   -- Moyenne des valeurs
MAX(colonne)   -- Valeur maximale
MIN(colonne)   -- Valeur minimale
```

#### La clause WHERE — Tous les opérateurs

```sql
WHERE id = 89             -- Égalité
WHERE id != 89            -- Différent
WHERE score > 10          -- Supérieur strict
WHERE score >= 10         -- Supérieur ou égal
WHERE score BETWEEN 5 AND 15   -- Entre deux valeurs (inclus)
WHERE name = 'Bob'        -- Chaîne de caractères
WHERE name LIKE 'B%'      -- Commence par 'B'
WHERE name IS NULL        -- Valeur nulle
WHERE name IS NOT NULL    -- Valeur non nulle
WHERE id IN (1, 2, 3)     -- Dans une liste
```

---

### `9-full_creation.sql`

```sql
-- creates a table second_table in the database hbtn_0c_0
CREATE TABLE IF NOT EXISTS second_table (
    id    INT,
    name  VARCHAR(256),
    score INT
);

INSERT INTO second_table (id, name, score) VALUES
(1, "John",   10),
(2, "Alex",    3),
(3, "Bob",    14),
(4, "George",  8);
```

#### 🔍 Explication détaillée

Ce fichier combine **création** + **insertion de données initiales** (seed data) :

**Structure de second_table :**

| Colonne | Type | Description |
|---|---|---|
| `id` | `INT` | Identifiant numérique |
| `name` | `VARCHAR(256)` | Nom (max 256 chars) |
| `score` | `INT` | Score numérique |

**Données insérées :**

```
second_table après exécution :
┌────┬────────┬───────┐
│ id │  name  │ score │
├────┼────────┼───────┤
│  1 │ John   │    10 │
│  2 │ Alex   │     3 │
│  3 │ Bob    │    14 │
│  4 │ George │     8 │
└────┴────────┴───────┘
```

> 💡 Ici les guillemets doubles `"John"` sont utilisés — MySQL les accepte pour les chaînes mais la norme SQL préconise des guillemets simples `'John'`.

---

### `10-top_score.sql`

```sql
-- liste tous les enregistrements triés par score décroissant
SELECT score, name FROM second_table ORDER BY score DESC;
```

#### 🔍 Explication détaillée

| Élément | Rôle |
|---|---|
| `SELECT score, name` | Sélectionne **uniquement** les colonnes `score` et `name` (pas `id`) |
| `FROM second_table` | Source des données |
| `ORDER BY score` | **Trie les résultats** selon la colonne `score` |
| `DESC` | Tri **décroissant** — du plus grand au plus petit |

#### Toutes les variantes de tri

```sql
ORDER BY score DESC           -- 14, 10, 8, 3
ORDER BY score ASC            -- 3, 8, 10, 14 (défaut)
ORDER BY name ASC             -- Alphabétique A→Z
ORDER BY name DESC            -- Alphabétique Z→A
ORDER BY score DESC, name ASC -- Tri multicritères
```

#### 📤 Résultat

```
+-------+--------+
| score | name   |
+-------+--------+
|    14 | Bob    |
|    10 | John   |
|     8 | George |
|     3 | Alex   |
+-------+--------+
```

---

### `11-best_score.sql`

```sql
-- liste les enregistrements avec score >= 10
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
```

#### 🔍 Explication détaillée

| Élément | Rôle |
|---|---|
| `WHERE score >= 10` | **Filtre** : ne garde que les lignes où le score est >= 10 |
| `ORDER BY score DESC` | Trie par score décroissant |

#### Ordre d'évaluation SQL

MySQL traite les clauses dans cet ordre interne :
1. `FROM` → source
2. `WHERE` → filtrage
3. `SELECT` → colonnes
4. `ORDER BY` → tri
5. `LIMIT` → limitation

#### 📤 Résultat

```
+-------+------+
| score | name |
+-------+------+
|    14 | Bob  |
|    10 | John |
+-------+------+
```

---

### `12-no_cheating.sql`

```sql
-- met à jour le score de Bob à 10
UPDATE second_table
SET score = 10
WHERE name = 'Bob';
```

#### 🔍 Explication détaillée

| Élément | Rôle |
|---|---|
| `UPDATE` | **Commande de modification** — met à jour des lignes existantes |
| `second_table` | Nom de la table à modifier |
| `SET score = 10` | **Affectation** — change la valeur de `score` à 10 |
| `WHERE name = 'Bob'` | **Condition** — ne modifie que les lignes où `name = 'Bob'` |

#### ⚠️ Toujours utiliser WHERE avec UPDATE

```sql
-- ✅ CORRECT : modifie seulement Bob
UPDATE second_table SET score = 10 WHERE name = 'Bob';

-- 🚨 DANGEREUX : modifie TOUTES les lignes !
UPDATE second_table SET score = 10;
```

#### Modifier plusieurs colonnes à la fois

```sql
UPDATE second_table
SET score = 10, name = 'Robert'
WHERE id = 3;
```

---

### `13-change_class.sql`

```sql
-- supprime les enregistrements avec score <= 5
DELETE FROM second_table
WHERE score <= 5;
```

#### 🔍 Explication détaillée

| Élément | Rôle |
|---|---|
| `DELETE FROM` | **Suppression de lignes** dans une table |
| `second_table` | Table cible |
| `WHERE score <= 5` | Ne supprime que les lignes dont `score` est <= 5 |

#### Comparaison DELETE / TRUNCATE / DROP

| Commande | Effet | Peut filtrer ? | Réversible ? |
|---|---|---|---|
| `DELETE FROM table WHERE ...` | Supprime les lignes filtrées | ✅ Oui | ✅ (avec transaction) |
| `DELETE FROM table` | Supprime TOUTES les lignes | ❌ Non | ✅ (avec transaction) |
| `TRUNCATE TABLE table` | Vide la table entièrement (plus rapide) | ❌ Non | ❌ Non |
| `DROP TABLE table` | Supprime la table ET ses données | ❌ Non | ❌ Non |

#### Après exécution

```
Alex (score=3) → supprimé ✅
John (score=10) → conservé
Bob  (score=14) → conservé
George (score=8) → conservé
```

---

### `14-average.sql`

```sql
-- calcule la moyenne des scores de second_table
SELECT AVG(score) AS average
FROM second_table;
```

#### 🔍 Explication détaillée

| Élément | Rôle |
|---|---|
| `AVG(score)` | **Fonction d'agrégation** — calcule la **moyenne** de toutes les valeurs de `score` |
| `AS average` | **Alias** — renomme la colonne résultat en `average` |

#### Calcul

```
AVG(score) = (10 + 3 + 14 + 8) / 4 = 35 / 4 = 8.75
```

#### 📤 Résultat

```
+---------+
| average |
+---------+
|  8.7500 |
+---------+
```

#### Utilisation des alias AS

```sql
SELECT AVG(score) AS average           -- Colonne renommée
SELECT COUNT(*) AS total_students      -- Nom parlant
SELECT score AS note, name AS eleve    -- Plusieurs alias
```

---

### `15-groups.sql`

```sql
-- affiche le nombre d'enregistrements par score
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
```

#### 🔍 Explication détaillée

| Élément | Rôle |
|---|---|
| `COUNT(*) AS number` | Compte les lignes de chaque groupe |
| `GROUP BY score` | **Regroupe** les lignes ayant le même score |
| `ORDER BY number DESC` | Trie par nombre décroissant |

#### GROUP BY — Concept fondamental

`GROUP BY` est l'une des clauses les plus puissantes de SQL. Elle regroupe les lignes par valeur identique, puis applique des fonctions d'agrégation sur chaque groupe.

```
Avant GROUP BY :          Après GROUP BY score :
┌────┬────────┬───────┐   ┌───────┬────────┐
│ id │  name  │ score │   │ score │ number │
├────┼────────┼───────┤   ├───────┼────────┤
│  1 │ John   │    10 │   │    10 │      1 │
│  2 │ Alex   │     3 │   │     3 │      1 │
│  3 │ Bob    │    14 │   │    14 │      1 │
│  4 │ George │     8 │   │     8 │      1 │
└────┴────────┴───────┘   └───────┴────────┘
```

#### HAVING — Filtrer les groupes

```sql
-- Affiche seulement les scores ayant plus de 1 enregistrement
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
HAVING COUNT(*) > 1
ORDER BY number DESC;
```

> 🔑 `WHERE` filtre les lignes **avant** le groupement, `HAVING` filtre les groupes **après**.

---

### `16-no_link.sql`

```sql
-- affiche les scores et noms non NULL, triés par score décroissant
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
```

#### 🔍 Explication détaillée

| Élément | Rôle |
|---|---|
| `WHERE name IS NOT NULL` | **Filtre les valeurs NULL** — exclut les lignes dont `name` est NULL |
| `ORDER BY score DESC` | Tri décroissant par score |

#### NULL en SQL — Concept critique

`NULL` représente l'**absence de valeur** (ni 0, ni chaîne vide).

```sql
-- ✅ Correct : tester NULL avec IS NULL / IS NOT NULL
WHERE name IS NULL       -- lignes sans nom
WHERE name IS NOT NULL   -- lignes avec un nom

-- ❌ FAUX : = NULL ne fonctionne JAMAIS en SQL !
WHERE name = NULL        -- Ne retourne rien (même si NULL existe)
WHERE name != NULL       -- Idem
```

> 💡 En SQL, `NULL = NULL` retourne **UNKNOWN** (pas TRUE). C'est pourquoi `IS NULL` est obligatoire.

---

### `delete_second_table.sql`

```sql
-- supprime la table second_table si elle existe
DROP TABLE IF EXISTS second_table;
```

#### 🔍 Explication détaillée

| Élément | Rôle |
|---|---|
| `DROP TABLE` | **Supprime définitivement** une table et toutes ses données |
| `IF EXISTS` | Évite une erreur si la table n'existe pas |
| `second_table` | Nom de la table à supprimer |

#### DROP TABLE vs DROP DATABASE

```sql
DROP TABLE second_table;
-- → Supprime uniquement second_table
-- → La base hbtn_0c_0 et les autres tables restent intactes

DROP DATABASE hbtn_0c_0;
-- → Supprime la base ENTIÈRE avec TOUTES ses tables
```

---

## 6 — Les Catégories de Commandes SQL

SQL est organisé en plusieurs sous-langages selon le type d'opération :

### 🏗️ DDL — Data Definition Language

Définit et modifie la **structure** de la base de données.

| Commande | Rôle |
|---|---|
| `CREATE DATABASE` | Crée une base de données |
| `CREATE TABLE` | Crée une table |
| `ALTER TABLE` | Modifie la structure d'une table |
| `DROP DATABASE` | Supprime une base de données |
| `DROP TABLE` | Supprime une table |
| `TRUNCATE TABLE` | Vide entièrement une table |

### ✏️ DML — Data Manipulation Language

Manipule les **données** à l'intérieur des tables.

| Commande | Rôle |
|---|---|
| `INSERT INTO` | Insère de nouvelles lignes |
| `UPDATE` | Modifie des lignes existantes |
| `DELETE FROM` | Supprime des lignes |

### 🔍 DQL — Data Query Language

Interroge et lit les données.

| Commande | Rôle |
|---|---|
| `SELECT` | Lit et récupère des données |

### 🔐 DCL — Data Control Language

Gère les **droits et permissions** des utilisateurs.

| Commande | Rôle |
|---|---|
| `GRANT` | Accorde des permissions |
| `REVOKE` | Retire des permissions |

### 💾 TCL — Transaction Control Language

Gère les **transactions**.

| Commande | Rôle |
|---|---|
| `COMMIT` | Valide et enregistre une transaction |
| `ROLLBACK` | Annule une transaction |
| `SAVEPOINT` | Crée un point de sauvegarde intermédiaire |

---

## 7 — Tableau Géant de Référence — Toutes les Commandes SQL

---

### 🗄️ Gestion des Bases de Données

| Commande | Description | Exemple |
|---|---|---|
| `SHOW DATABASES` | Liste toutes les bases du serveur | `SHOW DATABASES;` |
| `CREATE DATABASE nom` | Crée une nouvelle base | `CREATE DATABASE ma_base;` |
| `CREATE DATABASE IF NOT EXISTS nom` | Crée seulement si elle n'existe pas | `CREATE DATABASE IF NOT EXISTS hbtn_0c_0;` |
| `DROP DATABASE nom` | Supprime la base entièrement (irréversible !) | `DROP DATABASE ma_base;` |
| `DROP DATABASE IF EXISTS nom` | Supprime seulement si elle existe | `DROP DATABASE IF EXISTS hbtn_0c_0;` |
| `USE nom` | Sélectionne une base de données | `USE hbtn_0c_0;` |
| `SELECT DATABASE()` | Affiche la base actuellement sélectionnée | `SELECT DATABASE();` |

---

### 📋 Gestion des Tables

| Commande | Description | Exemple |
|---|---|---|
| `SHOW TABLES` | Liste toutes les tables de la base courante | `SHOW TABLES;` |
| `CREATE TABLE nom (...)` | Crée une table avec ses colonnes | `CREATE TABLE users (id INT, name VARCHAR(100));` |
| `CREATE TABLE IF NOT EXISTS nom (...)` | Crée seulement si elle n'existe pas | `CREATE TABLE IF NOT EXISTS first_table (id INT, name VARCHAR(256));` |
| `DROP TABLE nom` | Supprime la table et ses données (irréversible !) | `DROP TABLE first_table;` |
| `DROP TABLE IF EXISTS nom` | Supprime seulement si elle existe | `DROP TABLE IF EXISTS second_table;` |
| `TRUNCATE TABLE nom` | Vide toutes les lignes (rapide, irréversible) | `TRUNCATE TABLE first_table;` |
| `ALTER TABLE nom ADD col type` | Ajoute une colonne | `ALTER TABLE users ADD email VARCHAR(200);` |
| `ALTER TABLE nom DROP COLUMN col` | Supprime une colonne | `ALTER TABLE users DROP COLUMN email;` |
| `ALTER TABLE nom MODIFY COLUMN col type` | Modifie le type d'une colonne | `ALTER TABLE users MODIFY COLUMN name VARCHAR(500);` |
| `ALTER TABLE nom RENAME TO nouveau` | Renomme une table | `ALTER TABLE users RENAME TO members;` |
| `SHOW CREATE TABLE nom` | Affiche le CREATE TABLE complet | `SHOW CREATE TABLE first_table;` |
| `DESCRIBE nom` / `DESC nom` | Affiche la structure d'une table | `DESCRIBE second_table;` |

---

### 📥 Insertion de Données (INSERT)

| Commande | Description | Exemple |
|---|---|---|
| `INSERT INTO table (cols) VALUES (vals)` | Insère une ligne avec colonnes précisées | `INSERT INTO first_table (id, name) VALUES (1, 'Alice');` |
| `INSERT INTO table VALUES (vals)` | Insère sans préciser les colonnes | `INSERT INTO first_table VALUES (1, 'Alice');` |
| `INSERT INTO table (cols) VALUES (...),(...)` | Insère plusieurs lignes en une commande | `INSERT INTO second_table (id, name, score) VALUES (1, 'John', 10), (2, 'Alex', 3);` |
| `INSERT INTO table SET col = val` | Syntaxe SET (MySQL uniquement) | `INSERT INTO first_table SET id = 1, name = 'Alice';` |
| `INSERT IGNORE INTO table (cols) VALUES (vals)` | Insère en ignorant les erreurs de doublons | `INSERT IGNORE INTO users (id, email) VALUES (1, 'a@b.com');` |
| `INSERT INTO table ... ON DUPLICATE KEY UPDATE col = val` | Insère ou met à jour si clé dupliquée (UPSERT) | `INSERT INTO users (id, name) VALUES (1, 'Bob') ON DUPLICATE KEY UPDATE name = 'Bob';` |

---

### 🔍 Lecture de Données (SELECT) et ses Clauses

| Commande / Clause | Description | Exemple |
|---|---|---|
| `SELECT * FROM table` | Toutes les colonnes, toutes les lignes | `SELECT * FROM first_table;` |
| `SELECT col1, col2 FROM table` | Colonnes spécifiques | `SELECT score, name FROM second_table;` |
| `SELECT col AS alias` | Renomme une colonne dans le résultat | `SELECT score AS note FROM second_table;` |
| `SELECT DISTINCT col FROM table` | Valeurs uniques, sans doublons | `SELECT DISTINCT score FROM second_table;` |
| `WHERE col = val` | Filtre par égalité | `WHERE name = 'Bob'` |
| `WHERE col != val` | Filtre : différent de | `WHERE score != 0` |
| `WHERE col > val` | Supérieur strict | `WHERE score > 10` |
| `WHERE col >= val` | Supérieur ou égal | `WHERE score >= 10` |
| `WHERE col < val` | Inférieur strict | `WHERE score < 5` |
| `WHERE col <= val` | Inférieur ou égal | `WHERE score <= 5` |
| `WHERE col BETWEEN a AND b` | Entre deux valeurs (inclus) | `WHERE score BETWEEN 5 AND 15` |
| `WHERE col IN (a, b, c)` | Dans une liste de valeurs | `WHERE id IN (1, 2, 3)` |
| `WHERE col NOT IN (a, b, c)` | Pas dans une liste | `WHERE id NOT IN (1, 2)` |
| `WHERE col LIKE 'pattern'` | Motif : `%` = tout, `_` = 1 caractère | `WHERE name LIKE 'B%'` |
| `WHERE col IS NULL` | La valeur est NULL | `WHERE name IS NULL` |
| `WHERE col IS NOT NULL` | La valeur n'est pas NULL | `WHERE name IS NOT NULL` |
| `WHERE cond1 AND cond2` | Les deux conditions vraies | `WHERE score > 5 AND name IS NOT NULL` |
| `WHERE cond1 OR cond2` | Au moins une condition vraie | `WHERE score > 10 OR name = 'Bob'` |
| `WHERE NOT cond` | Inverse la condition | `WHERE NOT score = 0` |
| `ORDER BY col ASC` | Tri croissant (défaut) | `ORDER BY score ASC` |
| `ORDER BY col DESC` | Tri décroissant | `ORDER BY score DESC` |
| `ORDER BY col1 DESC, col2 ASC` | Tri multicritères | `ORDER BY score DESC, name ASC` |
| `LIMIT n` | Limite le nombre de résultats | `LIMIT 10` |
| `LIMIT n OFFSET m` | n résultats en sautant les m premiers | `LIMIT 10 OFFSET 20` |
| `GROUP BY col` | Regroupe les lignes par valeur | `GROUP BY score` |
| `HAVING condition` | Filtre les groupes (après GROUP BY) | `HAVING COUNT(*) > 1` |

---

### 📊 Fonctions d'Agrégation

| Fonction | Description | Exemple |
|---|---|---|
| `COUNT(*)` | Compte toutes les lignes (inclut NULL) | `SELECT COUNT(*) FROM second_table;` |
| `COUNT(col)` | Compte les lignes non-NULL | `SELECT COUNT(name) FROM second_table;` |
| `SUM(col)` | Somme des valeurs | `SELECT SUM(score) FROM second_table;` |
| `AVG(col)` | Moyenne des valeurs | `SELECT AVG(score) AS average FROM second_table;` |
| `MAX(col)` | Valeur maximale | `SELECT MAX(score) FROM second_table;` |
| `MIN(col)` | Valeur minimale | `SELECT MIN(score) FROM second_table;` |
| `GROUP_CONCAT(col)` | Concatène les valeurs d'un groupe | `SELECT GROUP_CONCAT(name) FROM second_table GROUP BY score;` |

---

### ✏️ Modification de Données (UPDATE)

| Commande | Description | Exemple |
|---|---|---|
| `UPDATE table SET col = val WHERE cond` | Modifie les lignes filtrées | `UPDATE second_table SET score = 10 WHERE name = 'Bob';` |
| `UPDATE table SET col1=v1, col2=v2 WHERE cond` | Modifie plusieurs colonnes | `UPDATE second_table SET score = 10, name = 'Robert' WHERE id = 3;` |
| `UPDATE table SET col = col + n WHERE cond` | Incrémentation relative | `UPDATE second_table SET score = score + 5 WHERE name = 'Alex';` |
| `UPDATE table SET col = val` | ⚠️ Modifie TOUTES les lignes (sans WHERE) | `UPDATE second_table SET score = 0;` |

---

### 🗑️ Suppression de Données (DELETE)

| Commande | Description | Exemple |
|---|---|---|
| `DELETE FROM table WHERE cond` | Supprime les lignes filtrées | `DELETE FROM second_table WHERE score <= 5;` |
| `DELETE FROM table` | ⚠️ Supprime TOUTES les lignes | `DELETE FROM second_table;` |
| `TRUNCATE TABLE table` | Vide toute la table (rapide, réinitialise AUTO_INCREMENT) | `TRUNCATE TABLE second_table;` |

---

### 🔑 Contraintes (Constraints)

| Contrainte | Description | Exemple |
|---|---|---|
| `NOT NULL` | La colonne ne peut pas être NULL | `name VARCHAR(256) NOT NULL` |
| `UNIQUE` | Chaque valeur doit être unique | `email VARCHAR(200) UNIQUE` |
| `PRIMARY KEY` | Identifiant unique (NOT NULL + UNIQUE) | `id INT PRIMARY KEY` |
| `AUTO_INCREMENT` | Valeur auto-incrémentée à chaque insertion | `id INT AUTO_INCREMENT` |
| `DEFAULT val` | Valeur par défaut si rien n'est fourni | `score INT DEFAULT 0` |
| `FOREIGN KEY` | Référence la clé primaire d'une autre table | `FOREIGN KEY (user_id) REFERENCES users(id)` |
| `CHECK` | Valide une condition sur la valeur | `score INT CHECK (score >= 0)` |

---

### 🔗 Jointures (JOINs)

| Commande | Description | Exemple |
|---|---|---|
| `INNER JOIN` | Lignes avec correspondance dans les deux tables | `SELECT * FROM orders INNER JOIN users ON orders.user_id = users.id;` |
| `LEFT JOIN` | Toutes les lignes de gauche + correspondances de droite (NULL si aucune) | `SELECT * FROM users LEFT JOIN orders ON users.id = orders.user_id;` |
| `RIGHT JOIN` | Toutes les lignes de droite + correspondances de gauche | `SELECT * FROM orders RIGHT JOIN users ON orders.user_id = users.id;` |
| `CROSS JOIN` | Produit cartésien (toutes les combinaisons) | `SELECT * FROM table1 CROSS JOIN table2;` |

---

### 🛠️ Fonctions MySQL Utiles

| Fonction | Description | Exemple |
|---|---|---|
| `UPPER(str)` | Convertit en majuscules | `SELECT UPPER(name) FROM second_table;` |
| `LOWER(str)` | Convertit en minuscules | `SELECT LOWER(name) FROM second_table;` |
| `LENGTH(str)` | Longueur d'une chaîne | `SELECT LENGTH(name) FROM second_table;` |
| `CONCAT(a, b, ...)` | Concatène des chaînes | `SELECT CONCAT(name, ' - ', score) FROM second_table;` |
| `SUBSTRING(str, pos, len)` | Extrait une sous-chaîne | `SELECT SUBSTRING(name, 1, 3) FROM second_table;` |
| `TRIM(str)` | Supprime les espaces en début/fin | `SELECT TRIM(name) FROM second_table;` |
| `ROUND(num, d)` | Arrondit à `d` décimales | `SELECT ROUND(AVG(score), 2) FROM second_table;` |
| `NOW()` | Date et heure actuelles | `SELECT NOW();` |
| `CURDATE()` | Date actuelle | `SELECT CURDATE();` |
| `IFNULL(col, val)` | Retourne `val` si `col` est NULL | `SELECT IFNULL(name, 'Inconnu') FROM second_table;` |
| `COALESCE(a, b, c)` | Premier argument non NULL | `SELECT COALESCE(name, email, 'N/A') FROM users;` |

---

### 💬 Commentaires SQL

| Syntaxe | Description | Exemple |
|---|---|---|
| `-- commentaire` | Commentaire sur une ligne (standard SQL) | `-- Cette requête liste toutes les bases` |
| `# commentaire` | Commentaire une ligne (MySQL uniquement) | `# Requête de test` |
| `/* commentaire */` | Commentaire multiligne | `/* Ceci est un commentaire sur plusieurs lignes */` |

---

### 📋 Commandes MySQL en Ligne de Commande

| Commande Shell | Description |
|---|---|
| `mysql -u user -p` | Se connecter à MySQL (demande le mot de passe) |
| `mysql -u user -p base_de_donnees` | Se connecter directement à une base |
| `mysql -u user -p base < fichier.sql` | Exécuter un fichier SQL |
| `mysqldump -u user -p base > sauvegarde.sql` | Exporter (sauvegarder) une base |
| `mysql -u user -p base < sauvegarde.sql` | Importer une base depuis un fichier |
| `mysqladmin -u root -p create ma_base` | Créer une base depuis le terminal |
| `mysql -u user -p -e "SHOW DATABASES;"` | Exécuter une requête directement depuis le shell |

---

*README généré le 4 mars 2026 — Projet Holberton School Higher Level Programming*
