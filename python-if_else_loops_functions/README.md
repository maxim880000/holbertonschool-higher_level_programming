# Python - If/Else, Loops, Functions 🐍

## Description du Projet

Ce projet explore les structures de contrôle fondamentales de Python : les conditions, les boucles et les fonctions. Ces concepts constituent le cœur de la programmation impérative et permettent de créer des programmes dynamiques capables de prendre des décisions, de répéter des actions et de structurer le code de manière modulaire et réutilisable. À travers des exercices pratiques et progressifs, vous apprendrez à maîtriser les mécanismes de flux de contrôle, les boucles `for` et `while`, ainsi que la création et l'utilisation de fonctions.

## Objectifs d'Apprentissage

À la fin de ce projet, vous serez capable d'expliquer sans aide extérieure :

### Structures Conditionnelles
- **Comprendre les conditions** : Tests booléens, opérateurs de comparaison
- **Maîtriser if/elif/else** : Structure des blocs conditionnels
- **Opérateurs logiques** : `and`, `or`, `not` et leur combinaison
- **Conditions imbriquées** : Niveaux multiples de décision
- **Valeurs de vérité** : Truthiness et falsiness en Python

### Boucles
- **Boucle `for`** : Itération sur des séquences
- **Fonction `range()`** : Génération de séquences numériques
- **Boucle `while`** : Répétition conditionnelle
- **Contrôle de flux** : `break`, `continue`, `else` avec les boucles
- **Boucles imbriquées** : Itérations multidimensionnelles

### Fonctions
- **Définir des fonctions** : Syntaxe `def`, paramètres, corps de fonction
- **Paramètres et arguments** : Positionnels, par défaut, nommés
- **Instruction `return`** : Valeurs de retour
- **Portée des variables** : Locale vs globale
- **Docstrings** : Documentation des fonctions

### Concepts Avancés
- **Codes ASCII** : Manipulation de caractères avec `ord()` et `chr()`
- **Opérateurs modulo** : `%` pour les restes de division
- **Formatage de sortie** : Contrôle de l'affichage avec `end=` et `sep=`
- **Expressions booléennes** : Évaluation et court-circuit

## Table des Matières

1. [Concepts Clés Expliqués en Détail](#concepts-clés-expliqués-en-détail)
2. [Fichiers du Projet](#fichiers-du-projet)
3. [Commandes Importantes](#commandes-importantes)
4. [Concepts Avancés](#concepts-avancés)
5. [Bonnes Pratiques](#bonnes-pratiques-détaillées)
6. [Tests et Exécution](#tests-et-exécution)
7. [Ressources](#ressources)

---

## Concepts Clés Expliqués en Détail

### 1. Structures Conditionnelles (if/elif/else)

Les structures conditionnelles permettent d'exécuter du code différent selon que des conditions sont vraies ou fausses.

#### Syntaxe de Base

```python
if condition:
    # Bloc exécuté si condition est True
    instruction1
elif autre_condition:
    # Bloc exécuté si autre_condition est True
    instruction2
else:
    # Bloc exécuté si aucune condition n'est True
    instruction3
```

**Règles importantes** :
- Les **deux-points** (`:`) sont obligatoires après chaque condition
- L'**indentation** (4 espaces) définit les blocs de code
- `elif` = "else if" (contraction)
- `else` est optionnel

#### Opérateurs de Comparaison

| Opérateur | Signification | Exemple |
|-----------|---------------|---------|
| `==` | Égal à | `x == 5` |
| `!=` | Différent de | `x != 5` |
| `>` | Supérieur à | `x > 5` |
| `<` | Inférieur à | `x < 5` |
| `>=` | Supérieur ou égal | `x >= 5` |
| `<=` | Inférieur ou égal | `x <= 5` |

#### Opérateurs Logiques

| Opérateur | Description | Exemple |
|-----------|-------------|---------|
| `and` | ET logique (les deux doivent être vrais) | `x > 0 and x < 10` |
| `or` | OU logique (au moins un doit être vrai) | `x < 0 or x > 10` |
| `not` | NON logique (inverse la valeur) | `not x == 5` |

**Exemples détaillés** :
```python
# Condition simple
age = 18
if age >= 18:
    print("Majeur")

# if/else
if age >= 18:
    print("Majeur")
else:
    print("Mineur")

# if/elif/else
score = 85
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")

# Opérateurs logiques
x = 5
if x > 0 and x < 10:
    print("x est entre 0 et 10")

# Conditions imbriquées
if x > 0:
    if x < 10:
        print("x est positif et inférieur à 10")
    else:
        print("x est positif et supérieur ou égal à 10")
else:
    print("x est négatif ou zéro")
```

#### Valeurs de Vérité (Truthiness)

En Python, certaines valeurs sont considérées comme **fausses** :
- `False`
- `None`
- `0` (zéro)
- `0.0` (zéro flottant)
- `""` (chaîne vide)
- `[]` (liste vide)
- `{}` (dictionnaire vide)
- `()` (tuple vide)

Toutes les autres valeurs sont **vraies**.

```python
# Exemples
if "":  # False
    print("Ne sera pas affiché")

if "Hello":  # True
    print("Sera affiché")

if []:  # False
    print("Ne sera pas affiché")

if [1, 2, 3]:  # True
    print("Sera affiché")
```

### 2. La Boucle `for`

La boucle `for` permet d'itérer sur une séquence (liste, chaîne, range, etc.).

#### Syntaxe

```python
for variable in sequence:
    # Bloc répété pour chaque élément
    instruction
```

**Exemples** :
```python
# Itération sur une chaîne
for char in "Python":
    print(char)
# Output: P y t h o n (chacun sur une ligne)

# Itération sur une liste
for fruit in ["pomme", "banane", "orange"]:
    print(fruit)

# Itération sur un range
for i in range(5):  # 0, 1, 2, 3, 4
    print(i)

# Avec start et end
for i in range(2, 8):  # 2, 3, 4, 5, 6, 7
    print(i)

# Avec step
for i in range(0, 10, 2):  # 0, 2, 4, 6, 8
    print(i)
```

### 3. La Fonction `range()`

La fonction `range()` génère une séquence de nombres.

#### Syntaxe

```python
range(stop)           # De 0 à stop-1
range(start, stop)    # De start à stop-1
range(start, stop, step)  # De start à stop-1 avec un pas de step
```

**Exemples détaillés** :
```python
# range(stop)
list(range(5))
# Output: [0, 1, 2, 3, 4]

# range(start, stop)
list(range(2, 7))
# Output: [2, 3, 4, 5, 6]

# range(start, stop, step)
list(range(0, 10, 2))
# Output: [0, 2, 4, 6, 8]

# Compte à rebours (step négatif)
list(range(10, 0, -1))
# Output: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# Boucle avec range
for i in range(3):
    print(f"Itération {i}")
# Output:
# Itération 0
# Itération 1
# Itération 2
```

**⚠️ Points importants** :
- `range()` génère un objet itérable, pas une liste (efficacité mémoire)
- La valeur de fin (`stop`) est **EXCLUE**
- Par défaut, `start = 0` et `step = 1`

### 4. Les Fonctions

Les fonctions permettent d'organiser et de réutiliser du code.

#### Définition de Fonction

```python
def nom_fonction(parametre1, parametre2):
    """
    Docstring : description de la fonction
    """
    # Corps de la fonction
    resultat = parametre1 + parametre2
    return resultat
```

**Composants** :
1. **`def`** : Mot-clé pour définir une fonction
2. **Nom** : Identifiant de la fonction (snake_case)
3. **Paramètres** : Variables d'entrée (entre parenthèses)
4. **Docstring** : Documentation (optionnelle mais recommandée)
5. **Corps** : Instructions indentées
6. **`return`** : Valeur de sortie (optionnel)

#### Exemples de Fonctions

```python
# Fonction simple sans paramètre
def dire_bonjour():
    print("Bonjour!")

dire_bonjour()  # Appel de la fonction
# Output: Bonjour!

# Fonction avec paramètres
def addition(a, b):
    return a + b

resultat = addition(5, 3)
print(resultat)  # Output: 8

# Fonction avec valeur par défaut
def saluer(nom="Monde"):
    print(f"Bonjour, {nom}!")

saluer()           # Output: Bonjour, Monde!
saluer("Alice")    # Output: Bonjour, Alice!

# Fonction avec docstring
def multiplier(a, b):
    """
    Multiplie deux nombres.

    Args:
        a (int/float): Premier nombre
        b (int/float): Deuxième nombre

    Returns:
        int/float: Le produit de a et b
    """
    return a * b
```

#### L'Instruction `return`

```python
# Sans return (retourne None par défaut)
def afficher_message():
    print("Message")

resultat = afficher_message()
print(resultat)  # Output: None

# Avec return
def calculer_carre(x):
    return x ** 2

carre = calculer_carre(5)
print(carre)  # Output: 25

# Return multiple (retourne un tuple)
def min_max(liste):
    return min(liste), max(liste)

minimum, maximum = min_max([1, 5, 3, 9, 2])
print(f"Min: {minimum}, Max: {maximum}")  # Min: 1, Max: 9

# Return prématuré (sort de la fonction)
def verifier_positif(x):
    if x < 0:
        return False
    return True
```

### 5. Codes ASCII

ASCII (American Standard Code for Information Interchange) est un système d'encodage de caractères.

#### Fonctions `ord()` et `chr()`

- **`ord(caractere)`** : Retourne le code ASCII d'un caractère
- **`chr(code)`** : Retourne le caractère correspondant à un code ASCII

**Table ASCII (extraits)** :

| Caractère | Code ASCII | Type |
|-----------|------------|------|
| `0-9` | 48-57 | Chiffres |
| `A-Z` | 65-90 | Majuscules |
| `a-z` | 97-122 | Minuscules |
| espace | 32 | Espace |
| `\n` | 10 | Nouvelle ligne |

**Exemples** :
```python
# ord() - caractère vers code
print(ord('A'))   # 65
print(ord('a'))   # 97
print(ord('0'))   # 48
print(ord(' '))   # 32

# chr() - code vers caractère
print(chr(65))    # 'A'
print(chr(97))    # 'a'
print(chr(48))    # '0'

# Conversion majuscule <-> minuscule
majuscule = 'A'
minuscule = chr(ord(majuscule) + 32)
print(minuscule)  # 'a'

# Afficher l'alphabet
for i in range(97, 123):  # codes de 'a' à 'z'
    print(chr(i), end="")
# Output: abcdefghijklmnopqrstuvwxyz

# Vérifier si un caractère est une minuscule
def est_minuscule(c):
    return ord(c) >= 97 and ord(c) <= 122
```

**Relation majuscule/minuscule** :
- Différence constante de 32 entre majuscule et minuscule
- `ord('a') - ord('A') = 97 - 65 = 32`
- Pour convertir : `minuscule → majuscule : -32` | `majuscule → minuscule : +32`

### 6. L'Opérateur Modulo `%`

L'opérateur modulo `%` retourne le **reste** d'une division entière.

```python
# Syntaxe
reste = dividende % diviseur

# Exemples
print(10 % 3)   # 1 (10 ÷ 3 = 3 reste 1)
print(15 % 4)   # 3 (15 ÷ 4 = 3 reste 3)
print(20 % 5)   # 0 (division exacte)
print(7 % 2)    # 1 (impair)
print(8 % 2)    # 0 (pair)
```

**Applications pratiques** :

#### 1. Tester la parité
```python
nombre = 42
if nombre % 2 == 0:
    print("Pair")
else:
    print("Impair")
```

#### 2. Obtenir le dernier chiffre
```python
nombre = 12345
dernier_chiffre = nombre % 10  # 5
```

#### 3. Tester la divisibilité
```python
# Multiple de 3 ?
if nombre % 3 == 0:
    print("Multiple de 3")

# Multiple de 3 ET de 5 ?
if nombre % 3 == 0 and nombre % 5 == 0:
    print("Multiple de 15 (FizzBuzz!)")
```

#### 4. Cycle répétitif
```python
# Alterner entre 0, 1, 2
for i in range(10):
    print(i % 3)
# Output: 0 1 2 0 1 2 0 1 2 0
```

### 7. Contrôle de l'Affichage avec `print()`

#### Paramètre `end=`

Par défaut, `print()` ajoute un saut de ligne (`\n`) à la fin. Le paramètre `end=` permet de le modifier.

```python
# Par défaut (saut de ligne)
print("Hello")
print("World")
# Output:
# Hello
# World

# Sans saut de ligne
print("Hello", end=" ")
print("World")
# Output: Hello World

# Avec un séparateur personnalisé
for i in range(5):
    print(i, end=", ")
# Output: 0, 1, 2, 3, 4,

# Formatage de nombres
for i in range(3):
    print(f"Nombre {i}", end=" | ")
# Output: Nombre 0 | Nombre 1 | Nombre 2 |
```

#### Paramètre `sep=`

Définit le séparateur entre plusieurs arguments de `print()`.

```python
# Par défaut (espace)
print("a", "b", "c")
# Output: a b c

# Séparateur personnalisé
print("a", "b", "c", sep="-")
# Output: a-b-c

print("2024", "01", "15", sep="/")
# Output: 2024/01/15

# Combinaison sep et end
print("x", "y", "z", sep=", ", end=".\n")
# Output: x, y, z.
```

### 8. Le Module `random`

Le module `random` permet de générer des nombres pseudo-aléatoires.

```python
import random

# Entier aléatoire entre a et b (inclus)
nombre = random.randint(1, 10)
print(nombre)  # Ex: 7

# Nombre flottant entre 0.0 et 1.0
aleatoire = random.random()
print(aleatoire)  # Ex: 0.734892

# Choix aléatoire dans une liste
fruits = ["pomme", "banane", "orange"]
fruit = random.choice(fruits)
print(fruit)  # Ex: "banane"

# Mélanger une liste
cartes = [1, 2, 3, 4, 5]
random.shuffle(cartes)
print(cartes)  # Ex: [3, 1, 5, 2, 4]
```

**`random.randint(a, b)`** :
- Génère un entier aléatoire `n` tel que `a <= n <= b`
- **Inclus** des deux côtés (contrairement à `range()`)

---

## Fichiers du Projet

### 📄 0-positive_or_negative.py

**Objectif** : Déterminer si un nombre est positif, négatif ou zéro

```python
#!/usr/bin/python3
import random
# On importe le module random pour pouvoir générer des nombres aléatoires
number = random.randint(-10, 10)

if number > 0:
    print(number, "is positive")
elif number < 0:
    print(number, "is negative")
else:
    print(number, "is zero")
```

**Notions utilisées** :
1. **Module `random`** : Génération de nombres aléatoires
2. **`random.randint(a, b)`** : Entier aléatoire entre a et b (inclus)
3. **Structure if/elif/else** : Conditions multiples
4. **Opérateurs de comparaison** : `>`, `<`

**Explication détaillée** :

**Import du module** :
```python
import random
```
- `import` charge le module `random` en mémoire
- Donne accès aux fonctions du module : `random.randint()`, `random.choice()`, etc.

**Génération aléatoire** :
```python
number = random.randint(-10, 10)
```
- Génère un entier entre -10 et 10 **inclus**
- Chaque exécution produit potentiellement un nombre différent
- Valeurs possibles : -10, -9, ..., -1, 0, 1, ..., 9, 10

**Logique conditionnelle** :
```python
if number > 0:        # Si strictement positif
    print(number, "is positive")
elif number < 0:      # Sinon, si strictement négatif
    print(number, "is negative")
else:                 # Sinon (forcément zéro)
    print(number, "is zero")
```

**Flux d'exécution** :
1. Python évalue `number > 0`
   - Si `True` → affiche "is positive" et **termine**
   - Si `False` → passe à `elif`
2. Python évalue `number < 0`
   - Si `True` → affiche "is negative" et **termine**
   - Si `False` → passe à `else`
3. Exécute le bloc `else` (nombre = 0)

**Exemples de sortie** :
```bash
$ python3 0-positive_or_negative.py
5 is positive

$ python3 0-positive_or_negative.py
-3 is negative

$ python3 0-positive_or_negative.py
0 is zero
```

---

### 📄 1-last_digit.py

**Objectif** : Afficher le dernier chiffre d'un nombre et analyser ses propriétés

```python
#!/usr/bin/python3
# Import random générer des nombres aléatoires
import random

# Génère un nombre aléatoire compris entre -10000 et 10000
number = random.randint(-10000, 10000)

# On récupère le dernier chiffre du nombre
# abs(number) permet d'éviter les problèmes avec les nombres négatifs
last_digit = abs(number) % 10

# Si le nombre est négatif,dernier chiffre doit aussi être négatif
# ex-123 -> = -3
if number < 0:
    last_digit = -last_digit

# Affiche le nombre et son dernier chiffre
# end=" " permet de continuer l'affichage sur la même ligne
print(f"Last digit of {number} is {last_digit}", end=" ")

if last_digit > 5:
    print("and is greater than 5")

elif last_digit == 0:
    print("and is 0")

# - le dernier chiffre est inférieur à 6
# - et il n'est pas égal à 0
else:
    print("and is less than 6 and not 0")
```

**Notions utilisées** :
1. **Fonction `abs()`** : Valeur absolue d'un nombre
2. **Opérateur modulo `%`** : Obtenir le reste d'une division
3. **Paramètre `end=`** : Contrôler la fin de ligne de `print()`
4. **Conditions imbriquées** : Plusieurs niveaux de tests

**Explication détaillée** :

**Obtention du dernier chiffre** :

Pour un nombre **positif** :
```python
number = 12345
last_digit = number % 10  # 12345 % 10 = 5
```

Pour un nombre **négatif**, il faut utiliser la valeur absolue :
```python
number = -12345
last_digit = abs(number) % 10  # abs(-12345) = 12345, puis % 10 = 5
```

**Gestion du signe** :
```python
if number < 0:
    last_digit = -last_digit
```
- Si le nombre original est négatif, le dernier chiffre doit aussi être négatif
- Exemple : -123 → dernier chiffre = -3

**Affichage sur la même ligne** :
```python
print(f"Last digit of {number} is {last_digit}", end=" ")
```
- `end=" "` remplace le saut de ligne par un espace
- Permet de continuer l'affichage sur la même ligne avec le prochain `print()`

**Analyse du dernier chiffre** :
```python
if last_digit > 5:
    print("and is greater than 5")  # 6, 7, 8, 9
elif last_digit == 0:
    print("and is 0")               # 0
else:
    print("and is less than 6 and not 0")  # 1, 2, 3, 4, 5 ou -1, -2, ..., -9
```

**Exemples de sortie** :
```bash
$ python3 1-last_digit.py
Last digit of 4205 is 5 and is less than 6 and not 0

$ python3 1-last_digit.py
Last digit of -626 is -6 and is less than 6 and not 0

$ python3 1-last_digit.py
Last digit of 1680 is 0 and is 0

$ python3 1-last_digit.py
Last digit of 8 is 8 and is greater than 5
```

**Cas particuliers** :
- Nombre positif : dernier chiffre positif (0-9)
- Nombre négatif : dernier chiffre négatif (-9 à -1) sauf si 0
- Zéro : dernier chiffre = 0

---

### 📄 2-print_alphabet.py

**Objectif** : Afficher l'alphabet en minuscules sur une seule ligne

```python
#!/usr/bin/python3
# Boucle sur les codes ASCII de 97 à 122 (a,z)
for i in range(97, 123):
    # chr(i) convertit le code ASCII en caractère
    # print end="" affiche le caractère sans aller à la ligne
    print("{}".format(chr(i)), end="")
```

**Notions utilisées** :
1. **Boucle `for`** : Itération sur une séquence
2. **Fonction `range()`** : Génération de séquence numérique
3. **Fonction `chr()`** : Conversion code ASCII → caractère
4. **Méthode `.format()`** : Formatage de chaîne
5. **Paramètre `end=""`** : Pas de saut de ligne

**Explication détaillée** :

**Codes ASCII de l'alphabet minuscule** :
```
a → 97
b → 98
c → 99
...
z → 122
```

**La boucle** :
```python
for i in range(97, 123):
```
- `range(97, 123)` génère : 97, 98, 99, ..., 122 (123 est EXCLU)
- `i` prend successivement chaque valeur

**Conversion et affichage** :
```python
print("{}".format(chr(i)), end="")
```

Décorticage :
1. `chr(i)` convertit le code ASCII en caractère
   - `chr(97)` → `'a'`
   - `chr(98)` → `'b'`
   - etc.
2. `"{}".format(chr(i))` insère le caractère dans la chaîne
3. `end=""` supprime le saut de ligne par défaut
4. Résultat : tous les caractères sur la même ligne

**Déroulement** :
```
i = 97  → chr(97) = 'a'  → affiche 'a'
i = 98  → chr(98) = 'b'  → affiche 'b'
i = 99  → chr(99) = 'c'  → affiche 'c'
...
i = 122 → chr(122) = 'z' → affiche 'z'
```

**Sortie attendue** :
```
abcdefghijklmnopqrstuvwxyz
```

**Méthodes alternatives** :
```python
# Méthode 1 : Avec f-string
for i in range(97, 123):
    print(f"{chr(i)}", end="")

# Méthode 2 : Sans format
for i in range(97, 123):
    print(chr(i), end="")

# Méthode 3 : Itération directe sur string
import string
for c in string.ascii_lowercase:
    print(c, end="")

# Méthode 4 : Avec join (plus efficace)
print(''.join(chr(i) for i in range(97, 123)))
```

---

### 📄 3-print_alphabt.py

**Objectif** : Afficher l'alphabet en minuscules SAUF 'e' et 'q'

```python
#!/usr/bin/python3

# Boucle de i = 97 (a) à 122 (z)
for i in range(97, 123):
    # On ignore les lettres e (101) et q (113)
    if i != 101 and i != 113:
        # On affiche le caractère correspondant à i sans saut de ligne
        print("{}".format(chr(i)), end="")
```

**Notions utilisées** :
1. **Condition dans une boucle** : Filtrage des éléments
2. **Opérateur `!=`** : Différent de
3. **Opérateur logique `and`** : Les deux conditions doivent être vraies
4. **Codes ASCII** : `e` = 101, `q` = 113

**Explication détaillée** :

**Codes ASCII des lettres à exclure** :
```python
ord('e')  # 101
ord('q')  # 113
```

**Condition de filtrage** :
```python
if i != 101 and i != 113:
```
- `i != 101` : i n'est pas le code de 'e'
- `and` : **ET** logique
- `i != 113` : i n'est pas le code de 'q'
- Les deux doivent être vrais pour afficher

**Table de vérité** :

| i | i != 101 | i != 113 | Résultat | Action |
|---|----------|----------|----------|--------|
| 97 ('a') | True | True | True | Affiche |
| 101 ('e') | False | True | False | N'affiche pas |
| 113 ('q') | True | False | False | N'affiche pas |
| 122 ('z') | True | True | True | Affiche |

**Flux d'exécution** :
```
i = 97  ('a') → 97 != 101 and 97 != 113 → True → affiche 'a'
i = 98  ('b') → 98 != 101 and 98 != 113 → True → affiche 'b'
...
i = 101 ('e') → 101 != 101 → False → n'affiche PAS
...
i = 113 ('q') → 113 != 113 → False → n'affiche PAS
...
i = 122 ('z') → 122 != 101 and 122 != 113 → True → affiche 'z'
```

**Sortie attendue** :
```
abcdfghijklmnoprstuvwxyz
```
(notez l'absence de 'e' et 'q')

**Méthodes alternatives** :
```python
# Méthode 1 : Avec liste d'exclusion
exclus = [101, 113]
for i in range(97, 123):
    if i not in exclus:
        print(chr(i), end="")

# Méthode 2 : Comparaison de caractères directement
for i in range(97, 123):
    c = chr(i)
    if c != 'e' and c != 'q':
        print(c, end="")

# Méthode 3 : Avec continue
for i in range(97, 123):
    if i == 101 or i == 113:
        continue  # Saute cette itération
    print(chr(i), end="")
```

---

### 📄 4-print_hexa.py

**Objectif** : Afficher les nombres de 0 à 98 en décimal et hexadécimal

```python
#!/usr/bin/python3

for i in range(99):  # Boucle de 0 à 98 inclus
    print("{} = {}".format(i, hex(i)))  # Affiche décimal et hexadécimal
```

**Notions utilisées** :
1. **Fonction `hex()`** : Conversion décimal → hexadécimal
2. **Système hexadécimal** : Base 16 (0-9, a-f)
3. **Formatage** : Affichage de deux valeurs

**Explication détaillée** :

**Le système hexadécimal** :
- Base 16 : utilise 16 chiffres (0-9, A-F)
- Préfixe : `0x` en Python
- Utilisé en informatique (adresses mémoire, couleurs, etc.)

**Correspondances** :

| Décimal | Hexadécimal | Binaire |
|---------|-------------|---------|
| 0 | 0x0 | 0000 |
| 1 | 0x1 | 0001 |
| 9 | 0x9 | 1001 |
| 10 | 0xa | 1010 |
| 15 | 0xf | 1111 |
| 16 | 0x10 | 10000 |
| 255 | 0xff | 11111111 |

**La fonction `hex()`** :
```python
hex(0)    # '0x0'
hex(10)   # '0xa'
hex(15)   # '0xf'
hex(16)   # '0x10'
hex(255)  # '0xff'
```

**La boucle** :
```python
for i in range(99):
```
- Génère les nombres de 0 à 98 (99 est exclu)
- 99 itérations au total

**Affichage formaté** :
```python
print("{} = {}".format(i, hex(i)))
```
- Premier `{}` : valeur décimale de `i`
- Deuxième `{}` : valeur hexadécimale via `hex(i)`

**Sortie attendue** (extraits) :
```
0 = 0x0
1 = 0x1
2 = 0x2
...
9 = 0x9
10 = 0xa
11 = 0xb
12 = 0xc
13 = 0xd
14 = 0xe
15 = 0xf
16 = 0x10
...
98 = 0x62
```

**Calcul hexadécimal** :
```
98 en hexadécimal :
98 ÷ 16 = 6 reste 2
Donc 98₁₀ = 62₁₆ = 0x62
```

**Fonctions de conversion** :
```python
# Décimal → Hexadécimal
hex(42)      # '0x2a'

# Décimal → Binaire
bin(42)      # '0b101010'

# Décimal → Octal
oct(42)      # '0o52'

# Hexadécimal → Décimal
int('0x2a', 16)   # 42
int('2a', 16)     # 42 (sans préfixe)

# Binaire → Décimal
int('0b101010', 2)  # 42
int('101010', 2)    # 42 (sans préfixe)
```

---

### 📄 5-print_comb2.py

**Objectif** : Afficher les nombres de 00 à 99 avec formatage

```python
#!/usr/bin/python3

for i in range(100):  # Boucle de 0 à 99 inclus
    if i != 99:  # Tous les nombres sauf le dernier
        # {:02d} force 2 chiffres avec un zéro devant
        print("{:02d}, ".format(i), end="")
    else:
        print("{:02d}".format(i))  # Dernier nombre, suivi d'un saut de ligne
```

**Notions utilisées** :
1. **Spécificateur de format `:02d`** : Padding avec zéros
2. **Condition dans une boucle** : Traitement spécial du dernier élément
3. **Contrôle de l'affichage** : `end=""` pour concaténation

**Explication détaillée** :

**Le spécificateur `:02d`** :
```python
"{:02d}".format(5)   # "05"
"{:02d}".format(42)  # "42"
"{:02d}".format(100) # "100"
```

Décorticage de `:02d` :
- `:` : Début du spécificateur
- `0` : Caractère de remplissage (zéro)
- `2` : Largeur minimale (2 caractères)
- `d` : Type décimal (entier)

**Logique conditionnelle** :
```python
if i != 99:
    print("{:02d}, ".format(i), end="")
else:
    print("{:02d}".format(i))
```

**Pourquoi cette condition ?**
- Pour les nombres 0-98 : affiche "XX, " (avec virgule et espace)
- Pour le nombre 99 : affiche "99" (sans virgule, avec saut de ligne)
- Évite d'avoir une virgule à la fin : `"00, 01, ..., 98, 99"` ✅ au lieu de `"00, 01, ..., 98, 99, "` ❌

**Déroulement** :
```
i = 0  → i != 99 → True  → affiche "00, "
i = 1  → i != 99 → True  → affiche "01, "
i = 2  → i != 99 → True  → affiche "02, "
...
i = 98 → i != 99 → True  → affiche "98, "
i = 99 → i != 99 → False → affiche "99\n"
```

**Sortie attendue** :
```
00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, ..., 97, 98, 99
```

**Spécificateurs de format courants** :

| Format | Description | Exemple | Résultat |
|--------|-------------|---------|----------|
| `:d` | Entier décimal | `"{:d}".format(42)` | `"42"` |
| `:5d` | Largeur 5, aligné droite | `"{:5d}".format(42)` | `"   42"` |
| `:05d` | Largeur 5, padding zéros | `"{:05d}".format(42)` | `"00042"` |
| `:<5d` | Largeur 5, aligné gauche | `"{:<5d}".format(42)` | `"42   "` |
| `:^5d` | Largeur 5, centré | `"{:^5d}".format(42)` | `" 42  "` |
| `:+d` | Signe forcé | `"{:+d}".format(42)` | `"+42"` |
| `:,` | Séparateur de milliers | `"{:,}".format(1000)` | `"1,000"` |

**Méthodes alternatives** :
```python
# Méthode 1 : Avec f-string
for i in range(100):
    if i != 99:
        print(f"{i:02d}, ", end="")
    else:
        print(f"{i:02d}")

# Méthode 2 : Avec join (plus pythonic)
print(", ".join(f"{i:02d}" for i in range(100)))

# Méthode 3 : Sans condition (avec slicing pour enlever la dernière virgule)
result = ""
for i in range(100):
    result += f"{i:02d}, "
print(result[:-2])  # Enlève les 2 derniers caractères ", "
```

---

### 📄 6-print_comb3.py

**Objectif** : Afficher toutes les combinaisons de deux chiffres différents

```python
#!/usr/bin/python3

# On parcourt tous les chiffres possibles pour le premier chiffre (0 à 9)
for i in range(10):
    # Pour chaque premier chiffre i,
    # on parcourt tous les chiffres plus grands que i pour le deuxième chiffre
    for j in range(i + 1, 10):
        # Si ce n'est pas la dernière combinaison "89"
        # on affiche les deux chiffres suivis de ", "
        if i != 8 or j != 9:
            print("{}{}".format(i, j), end=", ")
        # Si c'est la dernière combinaison "89"
        # on affiche les deux chiffres suivis d'un saut de ligne
        else:
            print("{}{}".format(i, j))
```

**Notions utilisées** :
1. **Boucles imbriquées** : Boucle dans une boucle
2. **Combinaisons** : Paires sans répétition
3. **Condition complexe** : `or` logique pour le dernier élément
4. **Range dynamique** : `range(i + 1, 10)`

**Explication détaillée** :

**Concept de combinaisons** :
- On veut toutes les paires (i, j) où i < j
- Pas de répétition : (0, 1) ✅ mais pas (1, 0) ❌
- Pas de doublon : (5, 5) ❌
- Ordre croissant : premier chiffre < deuxième chiffre

**Boucles imbriquées** :
```python
for i in range(10):          # i = 0, 1, 2, ..., 9
    for j in range(i + 1, 10):  # j commence à i+1
```

**Déroulement visuel** :
```
i = 0:
  j = 1 → affiche "01"
  j = 2 → affiche "02"
  j = 3 → affiche "03"
  ...
  j = 9 → affiche "09"

i = 1:
  j = 2 → affiche "12"
  j = 3 → affiche "13"
  ...
  j = 9 → affiche "19"

i = 2:
  j = 3 → affiche "23"
  ...

...

i = 8:
  j = 9 → affiche "89" (dernier!)

i = 9:
  (pas de j car range(10, 10) est vide)
```

**Pourquoi `range(i + 1, 10)` ?**
- Assure que `j > i` (toujours)
- Évite les doublons : on ne génère jamais (5, 3) si on a déjà (3, 5)
- Évite les paires identiques : (5, 5) n'est jamais généré

**Condition pour le dernier élément** :
```python
if i != 8 or j != 9:
    print("{}{}".format(i, j), end=", ")
else:
    print("{}{}".format(i, j))
```

**Logique** :
- `i != 8 or j != 9` : Si ce n'est PAS la dernière combinaison
  - Vraie pour toutes les combinaisons sauf (8, 9)
  - Affiche avec ", " à la fin
- `else` : C'est la dernière combinaison (8, 9)
  - Affiche sans ", " et avec saut de ligne

**Table de vérité pour la dernière combinaison** :

| i | j | i != 8 | j != 9 | i != 8 or j != 9 | Action |
|---|---|--------|--------|------------------|--------|
| 0 | 1 | True | True | True | Affiche ", " |
| 1 | 2 | True | True | True | Affiche ", " |
| 8 | 8 | False | True | True | (n'existe pas) |
| 8 | 9 | False | False | False | Affiche "\n" |

**Sortie attendue** :
```
01, 02, 03, 04, 05, 06, 07, 08, 09, 12, 13, 14, 15, 16, 17, 18, 19, 23, 24, 25, 26, 27, 28, 29, 34, 35, 36, 37, 38, 39, 45, 46, 47, 48, 49, 56, 57, 58, 59, 67, 68, 69, 78, 79, 89
```

**Nombre total de combinaisons** :
- Formule : C(n, k) = n! / (k! * (n-k)!)
- Ici : C(10, 2) = 10! / (2! * 8!) = 45 combinaisons

**Méthodes alternatives** :
```python
# Méthode 1 : Avec list comprehension et join
combos = [f"{i}{j}" for i in range(10) for j in range(i+1, 10)]
print(", ".join(combos))

# Méthode 2 : Avec itertools
from itertools import combinations
combos = [''.join(map(str, c)) for c in combinations(range(10), 2)]
print(", ".join(combos))
```

---

### 📄 7-islower.py

**Objectif** : Vérifier si un caractère est en minuscule

```python
#!/usr/bin/python3

# Fonction qui vérifie si un caractère est en minuscule
def islower(c):
    # ord(c) retourne le code ASCII du caractère c
    # Les lettres minuscules vont de 'a' (97) à 'z' (122)
    if ord(c) >= 97 and ord(c) <= 122:
        return True  # Retourne True si c est compris entre 'a' et 'z'
    else:
        return False  # Retourne False sinon
```

**Notions utilisées** :
1. **Définition de fonction** : `def nom_fonction(parametre):`
2. **Paramètre** : Variable d'entrée de la fonction
3. **Instruction `return`** : Valeur de sortie
4. **Fonction `ord()`** : Caractère → code ASCII
5. **Valeurs booléennes** : `True` et `False`

**Explication détaillée** :

**Structure de la fonction** :
```python
def islower(c):
    # Corps de la fonction
    return resultat
```
- `def` : Mot-clé pour définir une fonction
- `islower` : Nom de la fonction (convention : `snake_case`)
- `c` : Paramètre (caractère à tester)
- `return` : Renvoie un résultat (True ou False)

**Logique de vérification** :
```python
if ord(c) >= 97 and ord(c) <= 122:
    return True
else:
    return False
```

**Codes ASCII des minuscules** :
```
'a' → 97
'b' → 98
...
'z' → 122
```

**Test** :
```python
ord('a')  # 97  → 97 >= 97 and 97 <= 122 → True
ord('m')  # 109 → 109 >= 97 and 109 <= 122 → True
ord('z')  # 122 → 122 >= 97 and 122 <= 122 → True
ord('A')  # 65  → 65 >= 97 → False
ord('5')  # 53  → 53 >= 97 → False
ord('@')  # 64  → 64 >= 97 → False
```

**Utilisation de la fonction** :
```python
# Appels
print(islower('a'))  # True
print(islower('Z'))  # False
print(islower('3'))  # False
print(islower('g'))  # True

# Dans une condition
char = input("Entrez un caractère: ")
if islower(char):
    print("C'est une minuscule")
else:
    print("Ce n'est pas une minuscule")
```

**Simplification possible** :
```python
def islower(c):
    # Retourne directement le résultat du test
    return ord(c) >= 97 and ord(c) <= 122

# Ou encore plus simple
def islower(c):
    return 97 <= ord(c) <= 122  # Comparaison chaînée (pythonic!)
```

**Comparaison avec la méthode native** :
```python
# Méthode native de Python
'a'.islower()  # True
'Z'.islower()  # False

# Notre fonction
islower('a')   # True
islower('Z')   # False
```

**Tests supplémentaires** :
```python
# Test exhaustif
for i in range(128):  # Premiers 128 caractères ASCII
    char = chr(i)
    if islower(char):
        print(f"{char} ({i}) est une minuscule")

# Sortie:
# a (97) est une minuscule
# b (98) est une minuscule
# ...
# z (122) est une minuscule
```

---

### 📄 8-uppercase.py

**Objectif** : Convertir une chaîne en majuscules et l'afficher

```python
#!/usr/bin/python3

# Fonction qui affiche une chaîne en majuscules suivie d'un saut de ligne
def uppercase(str):

    # Parcours chaque caractère de la chaîne
    for c in str:
        # Si le caractère est une lettre minuscule ('a' à 'z')
        if ord(c) >= 97 and ord(c) <= 122:
            # Convertit la minuscule en majuscule en utilisant ASCII
            c = chr(ord(c) - 32)
        # Affiche le caractère (majuscules ou non) sans passer à la ligne
        print("{}".format(c), end="")
    # Après toute la chaîne, affiche un saut de ligne
    print()
```

**Notions utilisées** :
1. **Itération sur une chaîne** : `for c in str`
2. **Conversion majuscule/minuscule** : Arithmétique ASCII
3. **Fonction `chr()`** : Code ASCII → caractère
4. **Paramètre `end=""`** : Affichage sans saut de ligne
5. **`print()` vide** : Saut de ligne final

**Explication détaillée** :

**Relation ASCII majuscule/minuscule** :
```
Minuscule   Majuscule   Différence
'a' (97) → 'A' (65)  →  -32
'b' (98) → 'B' (66)  →  -32
'z' (122) → 'Z' (90)  →  -32
```

**Constante de conversion** : `-32`

**Algorithme de conversion** :
```python
for c in str:  # Pour chaque caractère
    if ord(c) >= 97 and ord(c) <= 122:  # Si minuscule
        c = chr(ord(c) - 32)  # Convertir en majuscule
    print("{}".format(c), end="")  # Afficher
print()  # Saut de ligne final
```

**Étapes de conversion** :
```python
# Exemple avec 'a'
c = 'a'
ord(c)         # 97
ord(c) - 32    # 65
chr(65)        # 'A'

# Exemple avec 'z'
c = 'z'
ord(c)         # 122
ord(c) - 32    # 90
chr(90)        # 'Z'
```

**Cas particuliers** :
```python
# Déjà en majuscule
c = 'A'
ord(c)  # 65 (< 97) → condition False → reste 'A'

# Chiffre
c = '5'
ord(c)  # 53 (< 97) → condition False → reste '5'

# Symbole
c = '!'
ord(c)  # 33 (< 97) → condition False → reste '!'
```

**Déroulement complet** :

Entrée : `"Hello World!"`

```
c = 'H' → ord('H') = 72  → pas minuscule → affiche 'H'
c = 'e' → ord('e') = 101 → minuscule → 101-32=69 → chr(69)='E' → affiche 'E'
c = 'l' → ord('l') = 108 → minuscule → 108-32=76 → chr(76)='L' → affiche 'L'
c = 'l' → ord('l') = 108 → minuscule → 108-32=76 → chr(76)='L' → affiche 'L'
c = 'o' → ord('o') = 111 → minuscule → 111-32=79 → chr(79)='O' → affiche 'O'
c = ' ' → ord(' ') = 32  → pas minuscule → affiche ' '
c = 'W' → ord('W') = 87  → pas minuscule → affiche 'W'
c = 'o' → ord('o') = 111 → minuscule → 111-32=79 → chr(79)='O' → affiche 'O'
c = 'r' → ord('r') = 114 → minuscule → 114-32=82 → chr(82)='R' → affiche 'R'
c = 'l' → ord('l') = 108 → minuscule → 108-32=76 → chr(76)='L' → affiche 'L'
c = 'd' → ord('d') = 100 → minuscule → 100-32=68 → chr(68)='D' → affiche 'D'
c = '!' → ord('!') = 33  → pas minuscule → affiche '!'
print()  → saut de ligne
```

Sortie : `"HELLO WORLD!"`

**Utilisation** :
```python
uppercase("Hello World!")  # HELLO WORLD!
uppercase("Python 3.8")    # PYTHON 3.8
uppercase("abc123")        # ABC123
```

**Comparaison avec la méthode native** :
```python
# Méthode native
"Hello World!".upper()  # "HELLO WORLD!"

# Notre fonction
uppercase("Hello World!")  # Affiche: HELLO WORLD!
```

**Version simplifiée** :
```python
def uppercase(str):
    for c in str:
        if 97 <= ord(c) <= 122:  # Comparaison chaînée
            c = chr(ord(c) - 32)
        print(c, end="")
    print()
```

---

### 📄 9-print_last_digit.py

**Objectif** : Afficher et retourner le dernier chiffre d'un nombre

```python
#!/usr/bin/python3
# prints the last digit of a number.
def print_last_digit(number):

    # abs pour les nb negatifs
    last_digit = abs(number) % 10
    # afficher le dernier chiffre sans saut de ligne
    print("{}".format(last_digit), end="")

    return last_digit
```

**Notions utilisées** :
1. **Fonction avec retour** : `return valeur`
2. **Fonction `abs()`** : Valeur absolue
3. **Opérateur modulo `%`** : Reste de division
4. **Affichage ET retour** : Double action de la fonction

**Explication détaillée** :

**Obtention du dernier chiffre** :
```python
last_digit = abs(number) % 10
```

**Étapes** :
1. `abs(number)` : Valeur absolue (élimine le signe négatif)
2. `% 10` : Reste de la division par 10 (dernier chiffre)

**Exemples** :
```python
# Nombres positifs
abs(12345) % 10  # 12345 % 10 = 5
abs(987) % 10    # 987 % 10 = 7
abs(50) % 10     # 50 % 10 = 0

# Nombres négatifs
abs(-12345) % 10  # 12345 % 10 = 5
abs(-987) % 10    # 987 % 10 = 7
abs(-50) % 10     # 50 % 10 = 0
```

**Pourquoi `abs()` ?**
- Sans `abs()`, le modulo de nombres négatifs donnerait des résultats négatifs en Python
- Exemple : `-123 % 10 = 7` en Python (comportement spécifique)
- Avec `abs()`, on obtient toujours un chiffre positif

**Double action de la fonction** :
1. **Affiche** le dernier chiffre (avec `print`)
2. **Retourne** le dernier chiffre (avec `return`)

**Utilisation** :
```python
# Affichage seul
print_last_digit(12345)  # Affiche: 5

# Capture du retour
resultat = print_last_digit(12345)  # Affiche: 5
print(resultat)  # Affiche: 5 (sur une nouvelle ligne)

# Utilisation dans une expression
total = print_last_digit(123) + print_last_digit(456)
# Affiche: 36
# total = 3 + 6 = 9

# Enchaînement
print_last_digit(98)
print_last_digit(0)
print_last_digit(-1024)
# Affiche: 804 (sur la même ligne)
```

**Différence avec/sans return** :
```python
# Sans return
def print_last_digit_v1(number):
    last_digit = abs(number) % 10
    print(last_digit, end="")
    # Pas de return → retourne None par défaut

result = print_last_digit_v1(123)  # Affiche: 3
print(result)  # None

# Avec return
def print_last_digit_v2(number):
    last_digit = abs(number) % 10
    print(last_digit, end="")
    return last_digit

result = print_last_digit_v2(123)  # Affiche: 3
print(result)  # 3
```

**Tests** :
```python
print_last_digit(98)      # Affiche 8, retourne 8
print_last_digit(0)       # Affiche 0, retourne 0
print_last_digit(123456)  # Affiche 6, retourne 6
print_last_digit(-987)    # Affiche 7, retourne 7
```

---

### 📄 10-add.py

**Objectif** : Fonction d'addition simple

```python
#!/usr/bin/python3

# Fonction qui additionne deux entiers et retourne le résultat
def add(a, b):
    # Additionne a et b puis retourne le résultat
    return a + b
```

**Notions utilisées** :
1. **Fonction avec plusieurs paramètres** : `def func(param1, param2)`
2. **Opérateur `+`** : Addition
3. **Return direct** : Retour d'expression

**Explication détaillée** :

**Structure** :
```python
def add(a, b):
    return a + b
```
- Deux paramètres : `a` et `b`
- Calcul : `a + b`
- Retourne le résultat directement

**Utilisation** :
```python
# Appels basiques
resultat = add(1, 2)
print(resultat)  # 3

resultat = add(100, 250)
print(resultat)  # 350

# Dans une expression
total = add(5, 3) + add(2, 4)
print(total)  # (5+3) + (2+4) = 8 + 6 = 14

# Avec variables
x = 10
y = 20
somme = add(x, y)
print(somme)  # 30

# Nombres négatifs
print(add(-5, 3))   # -2
print(add(-5, -3))  # -8

# Flottants
print(add(3.14, 2.71))  # 5.85
```

**Version avec docstring** :
```python
def add(a, b):
    """
    Additionne deux nombres.

    Args:
        a (int/float): Premier nombre
        b (int/float): Deuxième nombre

    Returns:
        int/float: La somme de a et b

    Examples:
        >>> add(1, 2)
        3
        >>> add(10, -5)
        5
    """
    return a + b
```

**Fonctions similaires** :
```python
# Soustraction
def sub(a, b):
    return a - b

# Multiplication
def mul(a, b):
    return a * b

# Division
def div(a, b):
    return a / b

# Division entière
def div_int(a, b):
    return a // b

# Modulo
def mod(a, b):
    return a % b

# Puissance
def pow(a, b):
    return a ** b
```

---

### 📄 11-pow.py

**Objectif** : Fonction de puissance

```python
#!/usr/bin/python3

# Fonction qui calcule a élevé à la puissance b et retourne le résultat
def pow(a, b):
    # Calcule a puissance b en utilisant l'opérateur **
    return a ** b
```

**Notions utilisées** :
1. **Opérateur `**`** : Exponentiation (puissance)
2. **Fonction mathématique** : Calcul de puissance

**Explication détaillée** :

**L'opérateur `**`** :
```python
a ** b  # a élevé à la puissance b
```

**Exemples** :
```python
2 ** 3   # 2³ = 2 × 2 × 2 = 8
5 ** 2   # 5² = 5 × 5 = 25
10 ** 0  # 10⁰ = 1 (toute valeur à la puissance 0 vaut 1)
2 ** -1  # 2⁻¹ = 1/2 = 0.5
4 ** 0.5 # 4^0.5 = √4 = 2.0
```

**Utilisation de la fonction** :
```python
# Appels basiques
print(pow(2, 3))   # 8
print(pow(5, 2))   # 25
print(pow(10, 0))  # 1

# Exposants négatifs
print(pow(2, -1))  # 0.5
print(pow(10, -2)) # 0.01

# Racines (exposants fractionnaires)
print(pow(4, 0.5))   # 2.0 (racine carrée)
print(pow(27, 1/3))  # 3.0 (racine cubique)

# Grands nombres
print(pow(2, 10))   # 1024
print(pow(10, 6))   # 1000000
```

**Cas particuliers** :
```python
pow(0, 5)    # 0 (zéro à toute puissance positive = 0)
pow(1, 100)  # 1 (1 à toute puissance = 1)
pow(5, 0)    # 1 (tout à la puissance 0 = 1)
pow(-2, 3)   # -8 (exposant impair conserve le signe)
pow(-2, 2)   # 4 (exposant pair donne positif)
```

**Différence avec `pow()` built-in** :
```python
# Notre fonction
def pow(a, b):
    return a ** b

# Fonction built-in de Python (3 paramètres possibles)
pow(2, 3)      # 8
pow(2, 3, 5)   # (2**3) % 5 = 8 % 5 = 3 (modulo optionnel)
```

**Applications** :
```python
# Calcul d'aire
def aire_cercle(rayon):
    pi = 3.14159
    return pi * pow(rayon, 2)

# Croissance exponentielle
def croissance(valeur_initiale, taux, annees):
    return valeur_initiale * pow(1 + taux, annees)

# Nombre de combinaisons
def factorielle_approx(n):
    # Approximation de Stirling
    e = 2.71828
    return pow(n/e, n)
```

---

### 📄 12-fizzbuzz.py

**Objectif** : Implémenter le célèbre algorithme FizzBuzz

```python
#!/usr/bin/python3

# Fonction qui affiche les nombres de 1 à 100
def fizzbuzz():
    # Boucle sur les nombres de 1 à 100 inclus
    for i in range(1, 101):
        # Si le nombre est multiple de 3 et de 5, on affiche FizzBuzz
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        # Si le nombre est multiple de 3 seulement, on affiche Fizz
        elif i % 3 == 0:
            print("Fizz", end=" ")
        # Si le nombre est multiple de 5 seulement, on affiche Buzz
        elif i % 5 == 0:
            print("Buzz", end=" ")
        # Sinon, on affiche simplement le nombre
        else:
            print("{}".format(i), end=" ")
```

**Notions utilisées** :
1. **FizzBuzz** : Exercice classique de programmation
2. **Tests de divisibilité** : Utilisation de `% 3` et `% 5`
3. **Logique conditionnelle multiple** : if/elif/else
4. **Ordre des conditions** : Importance de tester d'abord le cas le plus spécifique

**Explication détaillée** :

**Les règles de FizzBuzz** :
1. Pour les multiples de **3** : afficher "Fizz"
2. Pour les multiples de **5** : afficher "Buzz"
3. Pour les multiples de **3 ET 5** (donc 15) : afficher "FizzBuzz"
4. Sinon : afficher le nombre

**⚠️ Ordre des conditions crucial !**

Il faut tester `3 AND 5` **AVANT** `3` ou `5` séparément :

```python
# ✅ CORRECT
if i % 3 == 0 and i % 5 == 0:  # Teste d'abord le cas double
    print("FizzBuzz")
elif i % 3 == 0:
    print("Fizz")
elif i % 5 == 0:
    print("Buzz")
else:
    print(i)

# ❌ INCORRECT
if i % 3 == 0:  # 15 serait capturé ici!
    print("Fizz")
elif i % 5 == 0:
    print("Buzz")
elif i % 3 == 0 and i % 5 == 0:  # Jamais atteint!
    print("FizzBuzz")
else:
    print(i)
```

**Pourquoi ?**
- Si `i = 15` :
  - Version correcte : teste `15 % 3 == 0 and 15 % 5 == 0` → True → affiche "FizzBuzz" ✅
  - Version incorrecte : teste `15 % 3 == 0` → True → affiche "Fizz" ❌ (ne teste jamais la condition AND)

**Déroulement (premiers nombres)** :

```
i = 1  → 1%3=1, 1%5=1     → else               → affiche "1"
i = 2  → 2%3=2, 2%5=2     → else               → affiche "2"
i = 3  → 3%3=0            → elif i%3==0        → affiche "Fizz"
i = 4  → 4%3=1, 4%5=4     → else               → affiche "4"
i = 5  → 5%5=0            → elif i%5==0        → affiche "Buzz"
i = 6  → 6%3=0            → elif i%3==0        → affiche "Fizz"
i = 7  → 7%3=1, 7%5=2     → else               → affiche "7"
i = 8  → 8%3=2, 8%5=3     → else               → affiche "8"
i = 9  → 9%3=0            → elif i%3==0        → affiche "Fizz"
i = 10 → 10%5=0           → elif i%5==0        → affiche "Buzz"
i = 11 → 11%3=2, 11%5=1   → else               → affiche "11"
i = 12 → 12%3=0           → elif i%3==0        → affiche "Fizz"
i = 13 → 13%3=1, 13%5=3   → else               → affiche "13"
i = 14 → 14%3=2, 14%5=4   → else               → affiche "14"
i = 15 → 15%3=0, 15%5=0   → if i%3==0 and ...  → affiche "FizzBuzz"
i = 16 → 16%3=1, 16%5=1   → else               → affiche "16"
...
```

**Sortie complète** :
```
1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz Fizz 22 23 Fizz Buzz 26 Fizz 28 29 FizzBuzz 31 32 Fizz 34 Buzz Fizz 37 38 Fizz Buzz 41 Fizz 43 44 FizzBuzz 46 47 Fizz 49 Buzz Fizz 52 53 Fizz Buzz 56 Fizz 58 59 FizzBuzz 61 62 Fizz 64 Buzz Fizz 67 68 Fizz Buzz 71 Fizz 73 74 FizzBuzz 76 77 Fizz 79 Buzz Fizz 82 83 Fizz Buzz 86 Fizz 88 89 FizzBuzz 91 92 Fizz 94 Buzz Fizz 97 98 Fizz Buzz
```

**Variantes** :
```python
# Variante 1 : Avec % 15
def fizzbuzz_v2():
    for i in range(1, 101):
        if i % 15 == 0:  # 15 = PPCM(3, 5)
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")

# Variante 2 : Construction de chaîne
def fizzbuzz_v3():
    for i in range(1, 101):
        output = ""
        if i % 3 == 0:
            output += "Fizz"
        if i % 5 == 0:
            output += "Buzz"
        print(output or i, end=" ")  # output si non vide, sinon i

# Variante 3 : One-liner (moins lisible)
def fizzbuzz_v4():
    for i in range(1, 101):
        print("Fizz"*(i%3==0) + "Buzz"*(i%5==0) or i, end=" ")
```

**Extensions du problème** :
```python
# FizzBuzzBazz (multiples de 3, 5, 7)
def fizzbuzzbazz():
    for i in range(1, 101):
        output = ""
        if i % 3 == 0:
            output += "Fizz"
        if i % 5 == 0:
            output += "Buzz"
        if i % 7 == 0:
            output += "Bazz"
        print(output or i, end=" ")
```

---

## Commandes Importantes

### Exécution de Scripts

```bash
# Exécution standard
python3 script.py

# Exécution avec arguments
python3 2-args.py arg1 arg2 arg3

# Rendre exécutable
chmod +x script.py
./script.py
```

### Tests de Fonctions

```bash
# Test interactif
python3
>>> from 7-islower import islower
>>> islower('a')
True
>>> islower('Z')
False
>>> exit()
```

### Débogage

```bash
# Mode verbose
python3 -v script.py

# Afficher les erreurs de syntaxe
python3 -m py_compile script.py

# Tracer l'exécution
python3 -m trace --trace script.py
```

---

## Concepts Avancés

### 1. Court-Circuit Logique

Les opérateurs `and` et `or` utilisent l'évaluation en court-circuit.

```python
# AND : s'arrête au premier False
x = 5
if x > 0 and x < 10:
    # Si x > 0 est False, x < 10 n'est PAS évalué
    print("Entre 0 et 10")

# OR : s'arrête au premier True
if x < 0 or x > 100:
    # Si x < 0 est True, x > 100 n'est PAS évalué
    print("Hors limites")

# Utilisation pour éviter les erreurs
denominator = 0
if denominator != 0 and 10 / denominator > 1:
    # Sans court-circuit, division par zéro!
    print("OK")
```

### 2. Opérateur Ternaire

Condition en une ligne.

```python
# Syntaxe
valeur_si_vrai if condition else valeur_si_faux

# Exemples
age = 20
statut = "majeur" if age >= 18 else "mineur"

nombre = -5
signe = "positif" if nombre > 0 else ("négatif" if nombre < 0 else "zéro")

# Équivalent à
if nombre > 0:
    signe = "positif"
elif nombre < 0:
    signe = "négatif"
else:
    signe = "zéro"
```

### 3. Compréhensions de Liste

```python
# Créer une liste de carrés
carres = [x**2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Avec condition
pairs = [x for x in range(20) if x % 2 == 0]
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# FizzBuzz en compréhension
fizzbuzz_list = [
    "FizzBuzz" if i % 15 == 0 else
    "Fizz" if i % 3 == 0 else
    "Buzz" if i % 5 == 0 else
    i
    for i in range(1, 101)
]
```

### 4. Fonctions Lambda

Fonctions anonymes courtes.

```python
# Syntaxe
lambda parametres: expression

# Exemples
carre = lambda x: x ** 2
print(carre(5))  # 25

addition = lambda a, b: a + b
print(addition(3, 4))  # 7

# Avec map
nombres = [1, 2, 3, 4, 5]
carres = list(map(lambda x: x**2, nombres))
# [1, 4, 9, 16, 25]

# Avec filter
pairs = list(filter(lambda x: x % 2 == 0, nombres))
# [2, 4]
```

### 5. Portée des Variables

```python
x = 10  # Variable globale

def fonction():
    x = 5  # Variable locale (masque la globale)
    print(x)  # 5

fonction()
print(x)  # 10 (globale inchangée)

# Modifier une variable globale
def fonction2():
    global x  # Déclare qu'on utilise la globale
    x = 20

fonction2()
print(x)  # 20 (globale modifiée)
```

---

## Bonnes Pratiques Détaillées

### 1. Nommage de Fonctions

```python
# ✅ BON
def calculate_total():
    pass

def is_valid_email():
    pass

def get_user_name():
    pass

# ❌ MAUVAIS
def CalculateTotal():  # PascalCase (réservé aux classes)
    pass

def IsValidEmail():
    pass
```

### 2. Docstrings

```python
# ✅ BON
def divide(a, b):
    """
    Divise a par b.

    Args:
        a (float): Dividende
        b (float): Diviseur

    Returns:
        float: Résultat de a / b

    Raises:
        ZeroDivisionError: Si b est zéro
    """
    if b == 0:
        raise ZeroDivisionError("Division par zéro")
    return a / b

# ❌ MAUVAIS (pas de docstring)
def divide(a, b):
    return a / b
```

### 3. Return vs Print

```python
# ✅ BON : Fonction retourne une valeur
def calculate_sum(a, b):
    return a + b

result = calculate_sum(5, 3)
print(result)

# ❌ MAUVAIS : Fonction imprime directement
def calculate_sum(a, b):
    print(a + b)  # Moins réutilisable

calculate_sum(5, 3)  # Pas de valeur de retour
```

### 4. Valeurs par Défaut

```python
# ✅ BON
def greet(name, greeting="Bonjour"):
    return f"{greeting}, {name}!"

print(greet("Alice"))              # Bonjour, Alice!
print(greet("Bob", "Salut"))       # Salut, Bob!

# ⚠️ ATTENTION : Objets mutables par défaut
# ❌ MAUVAIS
def add_item(item, liste=[]):  # Liste partagée entre appels!
    liste.append(item)
    return liste

print(add_item(1))  # [1]
print(add_item(2))  # [1, 2] (pas [2]!)

# ✅ BON
def add_item(item, liste=None):
    if liste is None:
        liste = []
    liste.append(item)
    return liste
```

---

## Tests et Exécution

### Tests des Fichiers

```bash
# 0-positive_or_negative.py
$ python3 0-positive_or_negative.py
5 is positive

# 1-last_digit.py
$ python3 1-last_digit.py
Last digit of 4205 is 5 and is less than 6 and not 0

# 2-print_alphabet.py
$ python3 2-print_alphabet.py
abcdefghijklmnopqrstuvwxyz

# 3-print_alphabt.py
$ python3 3-print_alphabt.py
abcdfghijklmnoprstuvwxyz

# 4-print_hexa.py
$ python3 4-print_hexa.py | head -20
0 = 0x0
1 = 0x1
...

# 5-print_comb2.py
$ python3 5-print_comb2.py
00, 01, 02, ..., 98, 99

# 6-print_comb3.py
$ python3 6-print_comb3.py
01, 02, 03, ..., 89

# 12-fizzbuzz.py
$ python3 -c "from 12-fizzbuzz import fizzbuzz; fizzbuzz()" | head -c 100
1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz Fizz 22 23 Fizz Buzz
```

---

## Ressources

### Documentation Officielle
- [Python Control Flow](https://docs.python.org/3/tutorial/controlflow.html)
- [Python Built-in Functions](https://docs.python.org/3/library/functions.html)
- [PEP 8 - Style Guide](https://pep8.org/)

### Tutoriels
- [Real Python - Conditionals](https://realpython.com/python-conditional-statements/)
- [Real Python - For Loops](https://realpython.com/python-for-loop/)
- [Real Python - Functions](https://realpython.com/defining-your-own-python-function/)

### Exercices
- [HackerRank Python](https://www.hackerrank.com/domains/python)
- [LeetCode](https://leetcode.com/)
- [Codewars](https://www.codewars.com/)

---

## Conclusion

Ce projet vous a permis de maîtriser :
- ✅ Structures conditionnelles (if/elif/else)
- ✅ Boucles (for avec range)
- ✅ Fonctions (définition, paramètres, return)
- ✅ Codes ASCII et manipulation de caractères
- ✅ Opérateurs arithmétiques et logiques
- ✅ Algorithmes classiques (FizzBuzz)

**Prochaines étapes** :
1. Listes et tuples
2. Dictionnaires et sets
3. Compréhensions avancées
4. Gestion d'erreurs (try/except)
5. Programmation orientée objet

---

**Auteur** : Projet Holberton School  
**Date** : 2026  
**Langage** : Python 3.8+
