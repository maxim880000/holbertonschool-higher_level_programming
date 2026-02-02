# 🐍 Python - Hello, World# Python - Hello, World 🐍



![Python](https://img.shields.io/badge/Python-3.8.5-blue?style=for-the-badge&logo=python)## Description du Projet

![Ubuntu](https://img.shields.io/badge/Ubuntu-20.04_LTS-orange?style=for-the-badge&logo=ubuntu)

Ce projet constitue une introduction fondamentale à la programmation Python, couvrant les concepts de base essentiels pour tout développeur Python. Il explore les mécanismes d'affichage, le formatage de chaînes de caractères, la manipulation de variables, et les techniques de slicing. Ce module est conçu pour établir une base solide en Python en abordant les principes fondamentaux du langage avec des exemples pratiques et détaillés.

## 👤 Author

**GitHub:** [maxim880000](https://github.com/maxim880000)## Objectifs d'Apprentissage



---À la fin de ce projet, vous serez capable d'expliquer les concepts suivants sans aide extérieure :



## 📚 Description### Concepts Généraux Python

Premier projet Python à Holberton School. Introduction aux bases de Python : affichage, chaînes de caractères, formatage et manipulation de strings.- **Comprendre la philosophie de Python** : Pourquoi Python est génial, simple, lisible et puissant

- **Maîtriser l'interpréteur Python** : Comment Python exécute le code ligne par ligne

---- **Utiliser le REPL** (Read-Eval-Print Loop) : L'environnement interactif Python

- **Comprendre le shebang** (`#!/usr/bin/python3`) : Son rôle dans l'exécution de scripts

## 🎯 Objectifs d'Apprentissage

### Affichage et Formatage

À la fin de ce projet, vous serez capable d'expliquer :- **Utiliser la fonction `print()`** : Mécanismes d'affichage en Python

- **Maîtriser les f-strings** : Formatage moderne et élégant (Python 3.6+)

- Comment utiliser l'interpréteur Python- **Comprendre la méthode `.format()`** : Formatage de chaînes traditionnel

- Comment imprimer du texte et des variables avec `print`- **Formater les nombres** : Précision décimale, padding, alignement

- Comment utiliser les strings et l'indexation

- Le style de code officiel Python (PEP 8)### Manipulation de Chaînes

- Comment vérifier le code avec `pycodestyle`- **Indexation de chaînes** : Accéder à des caractères spécifiques

- **Slicing** : Extraire des sous-chaînes avec la notation `[start:end:step]`

---- **Concaténation** : Assembler des chaînes de différentes manières

- **Répétition** : Multiplier des chaînes avec l'opérateur `*`

## 📋 Requirements- **Immutabilité des chaînes** : Comprendre que les chaînes ne peuvent pas être modifiées



| Critère | Spécification |### Bonnes Pratiques

|:--------|:--------------|- **Style PEP 8** : Convention de codage officielle Python

| OS | Ubuntu 20.04 LTS |- **Documentation** : Importance des commentaires et docstrings

| Python | 3.8.5 |- **Caractères d'échappement** : `\n`, `\t`, `\"`, `\\`, etc.

| Éditeurs | vi, vim, emacs |

| Style | pycodestyle 2.7.* |## Table des Matières

| Shebang | `#!/usr/bin/python3` |

1. [Concepts Clés Expliqués en Détail](#concepts-clés-expliqués-en-détail)

---2. [Fichiers du Projet](#fichiers-du-projet)

3. [Commandes Importantes](#commandes-importantes)

## 📁 Fichiers du Projet4. [Concepts Avancés](#concepts-avancés)

5. [Bonnes Pratiques](#bonnes-pratiques-détaillées)

| Fichier | Description |6. [Tests et Exécution](#tests-et-exécution)

|:--------|:------------|7. [Ressources](#ressources)

| `2-print.py` | Affiche une chaîne avec guillemets et caractère d'échappement |

| `3-print_number.py` | Affiche un entier avec f-string |---

| `4-print_float.py` | Affiche un float avec 2 décimales |

| `5-print_string.py` | Affiche une string 3 fois et extrait les caractères |## Concepts Clés Expliqués en Détail

| `6-concat.py` | Concaténation de strings |

| `7-edges.py` | Extraction de parties d'une string (slicing) |### 1. Le Shebang (`#!/usr/bin/python3`)

| `8-concat_edges.py` | Concaténation avancée avec slicing |

| `9-easter_egg.py` | Affiche le Zen de Python |Le **shebang** est la première ligne d'un script Python exécutable.



---```python

#!/usr/bin/python3

## 💻 Codes et Explications```



### 2-print.py**Explication détaillée** :

```python- `#!` : Séquence magique qui indique au système qu'il s'agit d'un script

#!/usr/bin/python3- `/usr/bin/python3` : Chemin vers l'interpréteur Python 3

print("\"Programming is like building a multilingual puzzle")- **Fonction** : Permet d'exécuter le script directement sans taper `python3` devant

```- **Utilisation** : Combiné avec `chmod +x script.py` pour rendre le script exécutable



| Élément | Description |**Exemple d'utilisation** :

|:--------|:------------|```bash

| `#!/usr/bin/python3` | Shebang - indique l'interpréteur Python 3 |# Sans shebang

| `print()` | Fonction d'affichage |python3 mon_script.py

| `\"` | Caractère d'échappement pour afficher un guillemet |

| `""` | Délimiteurs de chaîne de caractères |# Avec shebang et chmod +x

./mon_script.py

---```



### 3-print_number.py### 2. La Fonction `print()`

```python

#!/usr/bin/python3La fonction `print()` est le mécanisme principal d'affichage en Python.

number = 98

print(f"{number} Battery street")**Syntaxe de base** :

``````python

print(objet1, objet2, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

| Élément | Description |```

|:--------|:------------|

| `number = 98` | Déclaration d'une variable entière |**Paramètres importants** :

| `f""` | F-string (formatted string literal) |- `sep` : Séparateur entre les objets (par défaut : espace)

| `{number}` | Interpolation de variable dans la f-string |- `end` : Caractère de fin (par défaut : saut de ligne `\n`)

- `file` : Destination de sortie (par défaut : sortie standard)

---- `flush` : Force l'écriture immédiate



### 4-print_float.py**Exemples détaillés** :

```python```python

#!/usr/bin/python3# Affichage simple

number = 3.14159print("Hello")  # Hello

print(f"Float: {number:.2f}")

```# Plusieurs arguments

print("Hello", "World")  # Hello World

| Élément | Description |

|:--------|:------------|# Changement du séparateur

| `3.14159` | Nombre à virgule flottante (float) |print("A", "B", "C", sep="-")  # A-B-C

| `:.2f` | Formatage : 2 chiffres après la virgule |

| `f` | Spécifie un nombre flottant (float) |# Changement du caractère de fin

print("Hello", end=" ")

---print("World")  # Hello World (sur la même ligne)



### 5-print_string.py# Affichage de variables

```pythonx = 42

#!/usr/bin/python3print("La valeur est", x)  # La valeur est 42

str = "Holberton School"```

print(str * 3)

print(str[:9])### 3. Les F-Strings (Formatted String Literals)

```

Les **f-strings** sont la méthode moderne de formatage introduite dans Python 3.6.

| Élément | Description |

|:--------|:------------|**Syntaxe** :

| `str * 3` | Répétition de la chaîne 3 fois |```python

| `str[:9]` | Slicing : caractères de l'index 0 à 8 |f"texte {variable} texte {expression}"

| `[:]` | Notation de slice [début:fin] |```



---**Avantages** :

- ✅ Plus lisible que `.format()`

### 6-concat.py- ✅ Plus rapide en exécution

```python- ✅ Permet d'évaluer des expressions directement

#!/usr/bin/python3- ✅ Syntaxe concise et intuitive

str1 = "Holberton"

str2 = "School"**Exemples détaillés** :

str1 = str1 + " " + str2```python

print(f"Welcome to {str1}!")# Variables simples

```name = "Alice"

age = 25

| Élément | Description |print(f"Je m'appelle {name} et j'ai {age} ans")

|:--------|:------------|# Output: Je m'appelle Alice et j'ai 25 ans

| `+` | Opérateur de concaténation de strings |

| `" "` | Espace comme chaîne |# Expressions

| `f"..."` | F-string pour l'affichage formaté |x = 10

y = 20

---print(f"La somme est {x + y}")

# Output: La somme est 30

### 7-edges.py

```python# Formatage de nombres

#!/usr/bin/python3pi = 3.14159

word = "Holberton"print(f"Pi vaut environ {pi:.2f}")

word_first_3 = word[:3]# Output: Pi vaut environ 3.14

word_last_2 = word[-2:]

middle_word = word[1:-1]# Padding et alignement

print(f"First 3 letters: {word_first_3}")num = 42

print(f"Last 2 letters: {word_last_2}")print(f"Nombre: {num:05d}")  # Remplit avec des zéros

print(f"Middle word: {middle_word}")# Output: Nombre: 00042

```

# Alignement

| Élément | Description |print(f"|{'gauche':<10}|")  # Aligné à gauche

|:--------|:------------|# Output: |gauche    |

| `word[:3]` | Premiers 3 caractères (index 0, 1, 2) |print(f"|{'centre':^10}|")  # Centré

| `word[-2:]` | Derniers 2 caractères (index -2, -1) |# Output: |  centre  |

| `word[1:-1]` | Du 2ème au dernier exclu |print(f"|{'droite':>10}|")  # Aligné à droite

| `-1` | Index négatif = depuis la fin |# Output: |    droite|

```

---

### 4. La Méthode `.format()`

### 8-concat_edges.py

```pythonMéthode traditionnelle de formatage avant les f-strings.

#!/usr/bin/python3

str = "Python is an interpreted, interactive, object-oriented programming\**Syntaxe** :

 language that combines remarkable power with very clear syntax"```python

str = str[39:67] + str[107:112] + str[0:6]"texte {} texte {}".format(valeur1, valeur2)

print(str)```

```

**Exemples** :

| Élément | Description |```python

|:--------|:------------|# Positionnels simples

| `\` | Continuation de ligne |print("{} + {} = {}".format(1, 2, 3))

| `str[39:67]` | Extraction d'une portion de la chaîne |# Output: 1 + 2 = 3

| `+` | Concaténation de plusieurs extraits |

# Avec indices

---print("{0} {1} {0}".format("Hello", "World"))

# Output: Hello World Hello

### 9-easter_egg.py

```python# Avec noms

#!/usr/bin/python3print("{name} a {age} ans".format(name="Bob", age=30))

import this# Output: Bob a 30 ans

```

# Formatage de nombres

| Élément | Description |print("Prix: {:.2f}€".format(19.99))

|:--------|:------------|# Output: Prix: 19.99€

| `import` | Mot-clé pour importer un module |```

| `this` | Module spécial affichant le Zen de Python |

### 5. Indexation et Slicing de Chaînes

---

Les chaînes en Python sont des **séquences indexables**.

## 📊 Tableau Récapitulatif des Concepts

#### Indexation

| Concept | Syntaxe | Exemple |

|:--------|:--------|:--------|**Règles** :

| **Print** | `print(valeur)` | `print("Hello")` |- Les indices commencent à **0**

| **F-string** | `f"{variable}"` | `f"Valeur: {x}"` |- Les indices négatifs comptent depuis la fin (**-1** = dernier caractère)

| **Formatage float** | `{var:.nf}` | `{pi:.2f}` → `3.14` |

| **Concaténation** | `str1 + str2` | `"Hel" + "lo"` → `"Hello"` |```python

| **Répétition** | `str * n` | `"ab" * 3` → `"ababab"` |texte = "Python"

| **Slicing début** | `str[:n]` | `"Hello"[:2]` → `"He"` |#        012345  (indices positifs)

| **Slicing fin** | `str[-n:]` | `"Hello"[-2:]` → `"lo"` |#       -6-5-4-3-2-1  (indices négatifs)

| **Slicing milieu** | `str[a:b]` | `"Hello"[1:4]` → `"ell"` |

| **Import** | `import module` | `import this` |print(texte[0])   # 'P' (premier caractère)

| **Échappement** | `\"` `\\` `\n` | `"\"coucou\""` |print(texte[5])   # 'n' (sixième caractère)

print(texte[-1])  # 'n' (dernier caractère)

---print(texte[-6])  # 'P' (premier caractère via indice négatif)

```

## 🔑 Points Clés à Retenir

#### Slicing (Découpage)

1. **Shebang** : Toujours commencer par `#!/usr/bin/python3`

2. **F-strings** : Méthode moderne et lisible pour formater les chaînes**Syntaxe complète** :

3. **Slicing** : `[début:fin:pas]` - fin est exclusif```python

4. **Index négatifs** : `-1` = dernier élément, `-2` = avant-dernierchaine[start:end:step]

5. **Concaténation** : Utiliser `+` pour joindre des chaînes```



---- `start` : Indice de départ (inclus)

- `end` : Indice de fin (EXCLU)

## 📖 Ressources- `step` : Pas (optionnel, défaut = 1)



- [The Python Tutorial](https://docs.python.org/3/tutorial/index.html)**Exemples détaillés** :

- [Whetting Your Appetite](https://docs.python.org/3/tutorial/appetite.html)```python

- [Using the Python Interpreter](https://docs.python.org/3/tutorial/interpreter.html)texte = "Holberton"

- [An Informal Introduction to Python](https://docs.python.org/3/tutorial/introduction.html)#        012345678

- [How To Use String Formatters in Python 3](https://realpython.com/python-f-strings/)

- [Pycodestyle – Style Guide for Python Code](https://pypi.org/project/pycodestyle/)# Slicing de base

print(texte[0:3])    # 'Hol' (indices 0, 1, 2)

---print(texte[:3])     # 'Hol' (début implicite à 0)

print(texte[3:])     # 'berton' (fin implicite à la fin)

<p align="center">Made with ❤️ at Holberton School</p>print(texte[:])      # 'Holberton' (copie complète)


# Indices négatifs
print(texte[-2:])    # 'on' (deux derniers caractères)
print(texte[:-2])    # 'Holbert' (tout sauf les deux derniers)
print(texte[-5:-2])  # 'ert' (de -5 inclus à -2 exclu)

# Avec step
print(texte[::2])    # 'Hletn' (un caractère sur deux)
print(texte[1::2])   # 'obro' (un sur deux, départ à 1)
print(texte[::-1])   # 'notrebloH' (inversion complète)

# Exemples pratiques
word = "Holberton"
first_3 = word[:3]        # 'Hol' (3 premiers)
last_2 = word[-2:]        # 'on' (2 derniers)
middle = word[1:-1]       # 'olberto' (sans premier ni dernier)
```

### 6. Concaténation de Chaînes

Plusieurs méthodes pour assembler des chaînes.

```python
# Opérateur +
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2  # "Hello World"

# Répétition avec *
print("=" * 20)  # "===================="
print("Ha" * 3)  # "HaHaHa"

# Concaténation implicite (littéraux adjacents)
long_text = ("Cette chaîne est très longue "
             "et continue sur plusieurs lignes")

# Méthode join() (recommandée pour plusieurs chaînes)
words = ["Python", "est", "génial"]
sentence = " ".join(words)  # "Python est génial"

# F-strings (méthode moderne)
name = "Alice"
greeting = f"Bonjour, {name}!"  # "Bonjour, Alice!"
```

### 7. Caractères Spéciaux et Échappement

**Caractères d'échappement courants** :

| Séquence | Signification | Exemple |
|----------|---------------|---------|
| `\n` | Saut de ligne | `print("Ligne1\nLigne2")` |
| `\t` | Tabulation | `print("Nom\tPrénom")` |
| `\"` | Guillemet double | `print("Il dit \"Bonjour\"")` |
| `\'` | Guillemet simple | `print('C\'est bien')` |
| `\\` | Backslash | `print("C:\\Users\\Documents")` |
| `\r` | Retour chariot | (Rarement utilisé) |
| `\b` | Retour arrière | (Rarement utilisé) |

**Exemples** :
```python
# Guillemets dans une chaîne
print("Elle a dit \"Hello\"")  # Elle a dit "Hello"
print('C\'est parfait')        # C'est parfait

# Chemins de fichiers
print("C:\\Users\\Documents\\file.txt")

# Chaînes brutes (raw strings) - ignore l'échappement
print(r"C:\Users\Documents")  # C:\Users\Documents (pas d'échappement)
```

### 8. Le Module `this` - Le Zen de Python

```python
import this
```

Cette commande affiche **Le Zen de Python** par Tim Peters, qui énonce 19 aphorismes guidant la philosophie de design de Python.

**Quelques principes clés** :
- **Beautiful is better than ugly** : La beauté du code compte
- **Explicit is better than implicit** : Soyez explicite
- **Simple is better than complex** : Privilégiez la simplicité
- **Readability counts** : La lisibilité est primordiale
- **There should be one-- and preferably only one --obvious way to do it** : Une seule façon évidente de faire les choses

---

## Fichiers du Projet

### 📄 2-print.py

**Objectif** : Afficher une chaîne contenant des guillemets doubles

```python
#!/usr/bin/python3
print("\"Programming is like building a multilingual puzzle")
```

**Notions utilisées** :
1. **Shebang** (`#!/usr/bin/python3`) : Permet l'exécution directe du script
2. **Fonction `print()`** : Affiche du texte sur la sortie standard
3. **Échappement de guillemets** (`\"`) : Pour inclure des guillemets dans une chaîne

**Explication détaillée** :
- Le backslash `\` avant le guillemet indique qu'il fait partie du texte et non de la syntaxe
- Sans l'échappement, Python interpréterait le guillemet comme la fin de la chaîne
- Alternative : utiliser des guillemets simples pour délimiter la chaîne : `print('"Programming is like building a multilingual puzzle')`

**Sortie attendue** :
```
"Programming is like building a multilingual puzzle
```

**Test** :
```bash
python3 2-print.py
# ou
chmod +x 2-print.py
./2-print.py
```

---

### 📄 3-print_number.py

**Objectif** : Afficher un nombre entier avec une f-string

```python
#!/usr/bin/python3
number = 98
# f for
# evaluate what we ahve in {} and replace by his value
print(f"{number} Battery street")
```

**Notions utilisées** :
1. **Variables** : Stockage de valeurs en mémoire
2. **F-strings** : Formatage moderne de chaînes (Python 3.6+)
3. **Interpolation** : Insertion de variables dans des chaînes

**Explication détaillée** :

**Qu'est-ce qu'une variable ?**
- Une **variable** est un espace de stockage nommé en mémoire
- `number = 98` crée une variable nommée `number` contenant la valeur `98`
- Le signe `=` est l'**opérateur d'affectation** (pas d'égalité mathématique)

**Anatomie de la f-string** :
```python
f"{number} Battery street"
 │  └─────┘
 │     └─── Expression Python évaluée
 └───────── Préfixe 'f' indique une f-string
```

**Étapes d'exécution** :
1. Python crée la variable `number` et y stocke `98`
2. Le préfixe `f` indique à Python de traiter la chaîne comme une f-string
3. Les accolades `{}` signalent une zone d'interpolation
4. Python évalue `number` → `98`
5. La valeur est convertie en chaîne et insérée
6. Résultat final : `"98 Battery street"`
7. `print()` affiche ce résultat

**Alternatives** :
```python
# Avec .format()
print("{} Battery street".format(number))

# Avec concaténation (nécessite conversion)
print(str(number) + " Battery street")

# Avec virgule dans print()
print(number, "Battery street")
```

**Sortie attendue** :
```
98 Battery street
```

---

### 📄 4-print_float.py

**Objectif** : Afficher un nombre à virgule avec une précision de 2 décimales

```python
#!/usr/bin/python3
number = 3.14159
print(f"Float: {number:.2f}")
```

**Notions utilisées** :
1. **Nombres flottants** (float) : Nombres à virgule flottante
2. **Formatage de précision** : Contrôle du nombre de décimales
3. **Spécificateurs de format** : `:.<nombre>f`

**Explication détaillée** :

**Les nombres flottants** :
- En Python, `3.14159` est un **float** (nombre à virgule flottante)
- Représentation en mémoire selon la norme IEEE 754
- Précision limitée (environ 15-17 chiffres significatifs)

**Anatomie du formatage** :
```python
f"Float: {number:.2f}"
         └──────┬───┘
                └─── Spécificateur de format
                     :     = début du format
                     .2    = 2 décimales
                     f     = type float
```

**Spécificateurs de format courants** :

| Format | Description | Exemple | Résultat |
|--------|-------------|---------|----------|
| `:.2f` | 2 décimales | `{3.14159:.2f}` | `3.14` |
| `:.4f` | 4 décimales | `{3.14159:.4f}` | `3.1416` |
| `:.0f` | Aucune décimale | `{3.14159:.0f}` | `3` |
| `:10.2f` | Largeur 10, 2 déc. | `{3.14:.2f}` | `      3.14` |
| `:e` | Notation scientifique | `{1000:e}` | `1.000000e+03` |
| `:%` | Pourcentage | `{0.25:%}` | `25.000000%` |

**Étapes d'exécution** :
1. `number = 3.14159` → Stocke le float
2. `{number:.2f}` → Formate avec 2 décimales
3. Python arrondit `3.14159` à `3.14` (arrondi bancaire)
4. Insertion dans la chaîne : `"Float: 3.14"`

**Arrondi en Python** :
- Python utilise l'**arrondi bancaire** (round half to even)
- `3.145` → `3.14` (arrondi vers le pair)
- `3.155` → `3.16` (arrondi vers le pair)

**Sortie attendue** :
```
Float: 3.14
```

**Exemples supplémentaires** :
```python
pi = 3.14159265359

print(f"{pi:.1f}")   # 3.1
print(f"{pi:.3f}")   # 3.142
print(f"{pi:.5f}")   # 3.14159
print(f"{pi:10.2f}") #       3.14 (largeur 10)
print(f"{pi:e}")     # 3.141593e+00 (scientifique)
```

---

### 📄 5-print_string.py

**Objectif** : Répétition et slicing de chaînes

```python
#!/usr/bin/python3
str = "Holberton School"
print(str * 3)
print(str[:9])  # print str de 0 a 9
```

**Notions utilisées** :
1. **Répétition de chaînes** : Opérateur `*`
2. **Slicing** : Extraction de sous-chaînes
3. **Indexation** : Accès aux caractères

**Explication détaillée** :

**Répétition avec `*`** :
```python
str = "Holberton School"
print(str * 3)
# Output: Holberton SchoolHolberton SchoolHolberton School
```

- `chaîne * n` répète la chaîne `n` fois
- Crée une **nouvelle chaîne** (les chaînes sont immutables)
- Fonctionne aussi avec `n * chaîne`

**Slicing `str[:9]`** :
```python
str = "Holberton School"
#      0123456789...
#      H o l b e r t o n

print(str[:9])  # "Holberton"
```

**Décorticage** :
- `[:9]` est équivalent à `[0:9]`
- **Début implicite** : 0 (premier caractère)
- **Fin** : 9 (EXCLU, donc jusqu'à l'indice 8)
- Caractères extraits : indices 0, 1, 2, 3, 4, 5, 6, 7, 8

**Visualisation** :
```
Index:  0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
Char:   H o l b e r t o n   S  c  h  o  o  l
        └─────────────────┘
             str[:9]
```

**Sortie attendue** :
```
Holberton SchoolHolberton SchoolHolberton School
Holberton
```

**Exemples supplémentaires** :
```python
s = "Python"

# Répétition
print(s * 2)      # PythonPython
print(s * 0)      # (chaîne vide)
print("-" * 40)   # ----------------------------------------

# Slicing
print(s[:3])      # Pyt
print(s[3:])      # hon
print(s[1:4])     # yth
print(s[::2])     # Pto (un sur deux)
print(s[::-1])    # nohtyP (inversion)
```

---

### 📄 6-concat.py

**Objectif** : Concaténation de chaînes et utilisation de f-strings

```python
#!/usr/bin/python3
str1 = "Holberton"
str2 = "School"
str1 = str1 + " " + str2
print(f"Welcome to {str1}!")
```

**Notions utilisées** :
1. **Concaténation** : Assemblage de chaînes avec `+`
2. **Réaffectation** : Modification d'une variable
3. **F-strings** : Insertion de variables dans des chaînes

**Explication détaillée** :

**Concaténation avec `+`** :
```python
str1 = "Holberton"
str2 = "School"
str1 = str1 + " " + str2
#      └────┬────┘ └┬┘ └──┬──┘
#         ancien    │   str2
#         str1   espace
```

**Étapes** :
1. `str1 + " "` → `"Holberton "`
2. `"Holberton " + str2` → `"Holberton School"`
3. Réaffectation : `str1 = "Holberton School"`

**⚠️ Point important** : Les chaînes sont **immutables**
- `str1 = str1 + " " + str2` ne modifie pas l'ancienne chaîne
- Une **nouvelle chaîne** est créée et assignée à `str1`
- L'ancienne valeur `"Holberton"` est perdue (garbage collected)

**F-string finale** :
```python
print(f"Welcome to {str1}!")
# str1 = "Holberton School"
# Output: Welcome to Holberton School!
```

**Sortie attendue** :
```
Welcome to Holberton School!
```

**Alternatives de concaténation** :
```python
str1 = "Holberton"
str2 = "School"

# Méthode 1 : Concaténation directe
result = str1 + " " + str2

# Méthode 2 : F-string
result = f"{str1} {str2}"

# Méthode 3 : .format()
result = "{} {}".format(str1, str2)

# Méthode 4 : join() (recommandée pour plusieurs chaînes)
result = " ".join([str1, str2])

# Méthode 5 : Opérateur +=
result = str1
result += " " + str2

# Méthode 6 : % (ancien style, déprécié)
result = "%s %s" % (str1, str2)
```

---

### 📄 7-edges.py

**Objectif** : Maîtriser le slicing avec différents indices

```python
#!/usr/bin/python3
word = "Holberton"
word_first_3 = word[:3]
word_last_2 = word[-2:]
middle_word = word[1:-1]
print(f"First 3 letters: {word_first_3}")
print(f"Last 2 letters: {word_last_2}")
print(f"Middle word: {middle_word}")
```

**Notions utilisées** :
1. **Slicing avancé** : Indices positifs et négatifs
2. **Indices négatifs** : Comptage depuis la fin
3. **Extraction de sous-chaînes** : Différentes techniques

**Explication détaillée** :

**Visualisation des indices** :
```
         H   o   l   b   e   r   t   o   n
Positif: 0   1   2   3   4   5   6   7   8
Négatif:-9  -8  -7  -6  -5  -4  -3  -2  -1
```

**1. Premiers caractères** : `word[:3]`
```python
word = "Holberton"
word_first_3 = word[:3]  # "Hol"
```
- Équivalent à `word[0:3]`
- Extrait indices 0, 1, 2 (le 3 est EXCLU)
- Principe : **Début implicite = 0**

**2. Derniers caractères** : `word[-2:]`
```python
word_last_2 = word[-2:]  # "on"
```
- Démarre à l'avant-dernier caractère (indice -2)
- Va jusqu'à la fin (fin implicite)
- Indices extraits : -2, -1 (ou 7, 8 en positif)

**3. Caractères du milieu** : `word[1:-1]`
```python
middle_word = word[1:-1]  # "olberto"
```
- **Début** : 1 (deuxième caractère, 'o')
- **Fin** : -1 (EXCLU, donc sans le dernier caractère)
- Exclut le premier et le dernier caractère

**Visualisation graphique** :
```
word = "Holberton"

word[:3]
└─────┘
"Hol"

word[-2:]
         └───┘
         "on"

word[1:-1]
  └──────────┘
  "olberto"
```

**Sortie attendue** :
```
First 3 letters: Hol
Last 2 letters: on
Middle word: olberto
```

**Exemples supplémentaires** :
```python
s = "Python Programming"

# Premiers/derniers
print(s[:6])      # "Python"
print(s[-11:])    # "Programming"

# Milieu
print(s[7:-5])    # "Program"

# Tous les n caractères
print(s[::2])     # "Pto rgamn" (un sur deux)
print(s[1::2])    # "yhnPoarmi" (un sur deux, départ 1)

# Inversion
print(s[::-1])    # "gnimmargorP nohtyP"

# Combinaisons
print(s[7:][:4])  # "Prog" (Programming → premiers 4)
print(s[-11:][:7]) # "Program" (Programming → premiers 7)
```

---

### 📄 8-concat_edges.py

**Objectif** : Créer une nouvelle chaîne par assemblage de slices

```python
#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = str[39:67] + str[107:112] + str[0:6]
print(str)
```

**Notions utilisées** :
1. **Continuation de ligne** : Backslash `\` à la fin d'une ligne
2. **Slicing multiple** : Extraction de plusieurs parties
3. **Concaténation de slices** : Assemblage de sous-chaînes

**Explication détaillée** :

**Continuation de ligne** :
```python
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
```
- Le `\` à la fin de la première ligne indique que la chaîne continue
- **Important** : Pas d'espace après le `\`
- Alternative : utiliser des parenthèses (recommandé)
```python
str = ("Python is an interpreted, interactive, object-oriented programming"
       " language that combines remarkable power with very clear syntax")
```

**Décorticage des slices** :

Chaîne originale :
```
Position: ...39                  67...107112...
Contenu:  ...object-oriented programming... with... Python...
```

**Slice 1** : `str[39:67]`
- Position 39 à 66
- Extrait : `"object-oriented programming"`

**Slice 2** : `str[107:112]`
- Position 107 à 111
- Extrait : `" with"`

**Slice 3** : `str[0:6]`
- Position 0 à 5
- Extrait : `"Python"`

**Assemblage** :
```python
str = str[39:67] + str[107:112] + str[0:6]
#     └─────────┘   └─────────┘   └────┘
#     "object-oriented programming" + " with" + "Python"
#     = "object-oriented programming with Python"
```

**Visualisation complète** :
```
Chaîne originale:
"Python is an interpreted, interactive, object-oriented programming language that combines remarkable power with very clear syntax"
 0     6                                39                  67                                       107 112

Extraction:
[39:67]  → "object-oriented programming"
[107:112] → " with"
[0:6]    → "Python"

Concaténation:
"object-oriented programming" + " with" + "Python"
= "object-oriented programming with Python"
```

**Sortie attendue** :
```
object-oriented programming with Python
```

**Technique** :
- Ce type d'exercice développe la précision dans le slicing
- Utile pour l'extraction et la recomposition de données textuelles
- En pratique, on utiliserait plutôt `.split()`, `.join()`, ou regex

**Exemples similaires** :
```python
# Inversion de mots
sentence = "Hello World Python"
result = sentence[12:18] + sentence[6:11] + sentence[0:5]
# "Python World Hello"

# Extraction sélective
data = "2024-01-15"
result = data[8:10] + "/" + data[5:7] + "/" + data[0:4]
# "15/01/2024"
```

---

### 📄 9-easter_egg.py

**Objectif** : Découvrir le Zen de Python

```python
#!/usr/bin/python3
import this
# import this → affiche le Zen de Python
```

**Notions utilisées** :
1. **Import de modules** : Directive `import`
2. **Modules standards** : Bibliothèque standard Python
3. **Easter egg** : Fonctionnalité cachée amusante

**Explication détaillée** :

**Le module `this`** :
- Module spécial de la bibliothèque standard Python
- Contient **Le Zen de Python** par Tim Peters
- Easter egg (œuf de Pâques) célèbre de Python

**Qu'est-ce qu'un import ?** :
```python
import this
```
- `import` charge un module en mémoire
- Exécute le code du module
- Rend les fonctions/variables du module disponibles

**Le Zen de Python** (texte affiché) :
```
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

**Principes clés expliqués** :

1. **Beautiful is better than ugly**
   - Le code doit être esthétique et bien formaté
   - Exemple : utiliser des espaces cohérents, des noms descriptifs

2. **Explicit is better than implicit**
   - Soyez clair sur vos intentions
   - Préférez `for item in list:` à des astuces obscures

3. **Simple is better than complex**
   - Cherchez toujours la solution la plus simple
   - Évitez la sur-ingénierie

4. **Readability counts**
   - Le code est lu plus souvent qu'il n'est écrit
   - Optimisez pour la lisibilité, pas pour la concision

5. **There should be one-- and preferably only one --obvious way to do it**
   - Philosophie "Pythonic" : une façon claire et évidente
   - Contraste avec Perl : "There's more than one way to do it"

**Fait amusant** :
Le texte du Zen est encodé avec ROT13 dans le code source du module !

```python
# Contenu réel du module this
s = """Gur Mra bs Clguba, ol Gvz Crgref..."""
d = {}
for c in (65, 97):
    for i in range(26):
        d[chr(i+c)] = chr((i+13) % 26 + c)
print("".join([d.get(c, c) for c in s]))
```

**Sortie attendue** :
```
The Zen of Python, by Tim Peters
[... tout le texte du Zen ...]
```

**Utilisation interactive** :
```bash
$ python3
>>> import this
[Le Zen s'affiche]
```

---

## Commandes Importantes

### Exécution de Scripts Python

```bash
# Méthode 1 : Avec l'interpréteur Python
python3 script.py

# Méthode 2 : Exécution directe (nécessite shebang et chmod +x)
chmod +x script.py
./script.py

# Vérification de la syntaxe sans exécution
python3 -m py_compile script.py

# Exécution avec affichage détaillé
python3 -v script.py
```

### Interpréteur Interactif (REPL)

```bash
# Lancer le REPL
python3

# Dans le REPL
>>> print("Hello")
Hello
>>> 2 + 2
4
>>> exit()  # ou Ctrl+D pour quitter
```

### Vérification de Style (PEP 8)

```bash
# Installation de pycodestyle
pip install pycodestyle

# Vérification d'un fichier
pycodestyle script.py

# Vérification de tous les fichiers Python
pycodestyle *.py

# Ignorer certaines erreurs
pycodestyle --ignore=E501,W503 script.py
```

### Gestion des Permissions

```bash
# Rendre un script exécutable
chmod +x script.py

# Vérifier les permissions
ls -l script.py

# Retirer l'exécutabilité
chmod -x script.py
```

---

## Concepts Avancés

### 1. Immutabilité des Chaînes

Les chaînes Python sont **immutables** : elles ne peuvent pas être modifiées après création.

```python
# Ceci NE fonctionne PAS
s = "Hello"
s[0] = "h"  # TypeError: 'str' object does not support item assignment

# Solution : créer une nouvelle chaîne
s = "Hello"
s = "h" + s[1:]  # "hello"

# Ou utiliser des méthodes qui retournent une nouvelle chaîne
s = "Hello"
s = s.lower()  # "hello"
```

**Implications** :
- Chaque modification crée une nouvelle chaîne
- Pour de nombreuses modifications, utiliser `list` puis `''.join()`
- Exemple :
```python
# Inefficace (crée n nouvelles chaînes)
result = ""
for i in range(1000):
    result += str(i)

# Efficace (une seule création finale)
result = ''.join(str(i) for i in range(1000))
```

### 2. Encodage Unicode

Python 3 utilise **Unicode** par défaut pour les chaînes.

```python
# Caractères Unicode
print("Café ☕")
print("Python 🐍")
print("π ≈ 3.14")

# Utilisation de codes Unicode
print("\u03C0")  # π
print("\U0001F40D")  # 🐍

# Encodage/décodage
texte = "Café"
bytes_utf8 = texte.encode('utf-8')  # b'Caf\xc3\xa9'
retour = bytes_utf8.decode('utf-8')  # "Café"
```

### 3. Méthodes de Chaînes Utiles

```python
s = "  Hello World  "

# Nettoyage
s.strip()      # "Hello World" (enlève espaces début/fin)
s.lstrip()     # "Hello World  " (enlève à gauche)
s.rstrip()     # "  Hello World" (enlève à droite)

# Casse
s.lower()      # "  hello world  "
s.upper()      # "  HELLO WORLD  "
s.capitalize() # "  hello world  "
s.title()      # "  Hello World  "

# Recherche
s.find("World")     # 8 (indice de début, -1 si absent)
s.index("World")    # 8 (erreur si absent)
s.count("l")        # 3 (nombre d'occurrences)
"World" in s        # True (test d'appartenance)

# Remplacement
s.replace("World", "Python")  # "  Hello Python  "

# Séparation/jonction
"a,b,c".split(",")       # ['a', 'b', 'c']
"-".join(['a', 'b'])     # "a-b"

# Tests
"123".isdigit()          # True
"abc".isalpha()          # True
"abc123".isalnum()       # True
"   ".isspace()          # True
```

### 4. Formatage Avancé avec F-Strings

```python
# Expressions complexes
x = 10
print(f"Le double de {x} est {x * 2}")  # Le double de 10 est 20

# Appels de fonctions
name = "alice"
print(f"Bonjour {name.upper()}")  # Bonjour ALICE

# Formatage de dates
from datetime import datetime
now = datetime.now()
print(f"Date : {now:%Y-%m-%d %H:%M:%S}")

# Notation scientifique
large = 1234567890
print(f"{large:e}")  # 1.234568e+09

# Binaire, octal, hexadécimal
num = 42
print(f"Décimal: {num}, Binaire: {num:b}, Hex: {num:x}")
# Décimal: 42, Binaire: 101010, Hex: 2a

# Dictionnaires (Python 3.8+)
person = {"name": "Alice", "age": 25}
print(f"{person['name']} a {person['age']} ans")
# Avec = pour debug (Python 3.8+)
print(f"{person['name']=}")  # person['name']='Alice'
```

### 5. Chaînes Multi-lignes

```python
# Triple quotes (""" ou ''')
long_text = """
Ceci est un texte
sur plusieurs lignes
qui préserve les sauts de ligne
"""

# Concaténation implicite
text = ("Ligne 1 "
        "Ligne 2 "
        "Ligne 3")  # "Ligne 1 Ligne 2 Ligne 3"

# Avec backslash (à éviter)
text = "Ligne 1 \
Ligne 2"
```

---

## Bonnes Pratiques Détaillées

### 1. Convention de Nommage PEP 8

```python
# ✅ BON
user_name = "Alice"
total_count = 42
is_valid = True

def calculate_total():
    pass

# ❌ MAUVAIS
UserName = "Alice"      # Style Java/C#
totalCount = 42         # camelCase (réservé aux classes)
IsValid = True
def CalculateTotal():   # Majuscules (réservé aux classes)
    pass
```

**Règles PEP 8** :
- **Variables et fonctions** : `snake_case` (minuscules avec underscores)
- **Constantes** : `UPPER_CASE` (`MAX_SIZE = 100`)
- **Classes** : `PascalCase` (`class UserAccount:`)
- **Modules** : `lowercase` (pas d'underscores si possible)

### 2. Documentation et Commentaires

```python
# ✅ Commentaire utile expliquant le POURQUOI
# On utilise -1 car les indices Python commencent à 0
last_index = len(list) - 1

# ❌ Commentaire inutile expliquant ce qui est évident
# Incrémente x de 1
x = x + 1

# ✅ Docstrings pour les fonctions
def calculate_area(radius):
    """
    Calcule l'aire d'un cercle.

    Args:
        radius (float): Le rayon du cercle

    Returns:
        float: L'aire du cercle (π * r²)
    """
    import math
    return math.pi * radius ** 2
```

### 3. Utilisation des F-Strings (Python 3.6+)

```python
name = "Alice"
age = 25

# ✅ MODERNE : F-strings (recommandé)
print(f"{name} a {age} ans")

# ✅ OK : .format() (pour compatibilité Python < 3.6)
print("{} a {} ans".format(name, age))

# ⚠️ ANCIEN : % formatting (déprécié)
print("%s a %d ans" % (name, age))

# ❌ ÉVITER : Concaténation manuelle
print(name + " a " + str(age) + " ans")  # Verbeux et peu lisible
```

### 4. Gestion des Chaînes Longues

```python
# ✅ BON : Concaténation implicite
long_text = (
    "Ceci est une très longue chaîne "
    "qui est divisée sur plusieurs lignes "
    "pour améliorer la lisibilité."
)

# ✅ BON : Triple quotes pour textes multi-lignes
message = """
Bonjour,

Ceci est un message multi-lignes.

Cordialement,
"""

# ❌ MAUVAIS : Ligne trop longue (> 79 caractères selon PEP 8)
long_text = "Ceci est une très longue chaîne qui dépasse largement la limite recommandée de 79 caractères par ligne"
```

### 5. Comparaison de Chaînes

```python
# ✅ BON
if name == "Alice":
    print("Bonjour Alice")

# ✅ BON : Vérification de chaîne vide
if not text:  # Pythonic
    print("Texte vide")

# ❌ MAUVAIS
if len(text) == 0:  # Moins pythonic
    print("Texte vide")

# ✅ BON : Vérification de préfixe/suffixe
filename = "document.pdf"
if filename.endswith('.pdf'):
    print("C'est un PDF")

# ❌ MAUVAIS
if filename[-4:] == '.pdf':  # Fragile
    print("C'est un PDF")
```

### 6. Éviter les Pièges Courants

```python
# ⚠️ Piège : Réaffectation de built-ins
str = "Hello"  # ❌ Écrase le type str
print(str(42))  # TypeError!

# ✅ Solution : Utiliser un autre nom
text = "Hello"
string = "Hello"

# ⚠️ Piège : Modification "sur place" impossible
s = "Hello"
s[0] = "h"  # ❌ TypeError (chaînes immutables)

# ✅ Solution : Créer une nouvelle chaîne
s = "h" + s[1:]
```

---

## Tests et Exécution

### Tests Manuels

```bash
# Test du fichier 2-print.py
$ python3 2-print.py
"Programming is like building a multilingual puzzle

# Test du fichier 3-print_number.py
$ python3 3-print_number.py
98 Battery street

# Test du fichier 4-print_float.py
$ python3 4-print_float.py
Float: 3.14

# Test du fichier 5-print_string.py
$ python3 5-print_string.py
Holberton SchoolHolberton SchoolHolberton School
Holberton

# Test du fichier 6-concat.py
$ python3 6-concat.py
Welcome to Holberton School!

# Test du fichier 7-edges.py
$ python3 7-edges.py
First 3 letters: Hol
Last 2 letters: on
Middle word: olberto

# Test du fichier 8-concat_edges.py
$ python3 8-concat_edges.py
object-oriented programming with Python

# Test du fichier 9-easter_egg.py
$ python3 9-easter_egg.py
The Zen of Python, by Tim Peters
[...]
```

### Vérification de Style

```bash
# Vérifier tous les fichiers
$ pycodestyle *.py

# Vérifier un fichier spécifique
$ pycodestyle 2-print.py

# Résultat attendu : aucune erreur
$ echo $?
0
```

### Tests avec l'Interpréteur

```python
# Lancer Python en mode interactif
$ python3

>>> # Test de print
>>> print("Hello, World!")
Hello, World!

>>> # Test de f-strings
>>> name = "Python"
>>> print(f"J'apprends {name}")
J'apprends Python

>>> # Test de slicing
>>> word = "Holberton"
>>> word[:3]
'Hol'
>>> word[-2:]
'on'
>>> word[1:-1]
'olberto'

>>> # Test de concaténation
>>> "Hello" + " " + "World"
'Hello World'

>>> # Test de répétition
>>> "Ha" * 3
'HaHaHa'

>>> exit()
```

---

## Exigences Techniques

### Environnement

- **OS** : Ubuntu 20.04 LTS (ou compatible)
- **Python** : Version 3.8.x ou supérieure
- **Éditeur** : vi, vim, emacs, VSCode, ou autre

### Vérification de la Version Python

```bash
$ python3 --version
Python 3.8.10

$ which python3
/usr/bin/python3
```

### Installation de Python (si nécessaire)

```bash
# Sur Ubuntu/Debian
sudo apt update
sudo apt install python3 python3-pip

# Vérification
python3 --version
```

### Style de Code

Tous les fichiers doivent respecter **PEP 8** :
- Maximum 79 caractères par ligne
- 2 lignes vides entre les fonctions de niveau module
- Indentation : 4 espaces (pas de tabulations)
- Nommage : `snake_case` pour variables/fonctions

```bash
# Installation de l'outil de vérification
pip install pycodestyle

# Utilisation
pycodestyle fichier.py
```

### Structure des Fichiers

```python
#!/usr/bin/python3
# Commentaire décrivant le fichier

# Imports (si nécessaire)
import module

# Code principal
if __name__ == "__main__":
    # Code exécuté si lancé directement
    pass
```

---

## Ressources

### Documentation Officielle

- [Documentation Python 3](https://docs.python.org/3/)
- [Tutorial Python Officiel](https://docs.python.org/3/tutorial/)
- [PEP 8 - Style Guide](https://pep8.org/)
- [PEP 498 - F-Strings](https://www.python.org/dev/peps/pep-0498/)

### Formatage de Chaînes

- [PyFormat](https://pyformat.info/) - Guide complet du formatage
- [F-Strings Guide](https://realpython.com/python-f-strings/)
- [String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)

### Apprendre Python

- [Real Python](https://realpython.com/)
- [Python for Beginners](https://www.python.org/about/gettingstarted/)
- [W3Schools Python Tutorial](https://www.w3schools.com/python/)

### Outils

- [Python REPL en ligne](https://www.python.org/shell/)
- [PythonTutor](http://pythontutor.com/) - Visualisation de l'exécution
- [Regex101](https://regex101.com/) - Test de regex

---

## Résumé des Concepts

| Concept | Syntaxe | Exemple |
|---------|---------|---------|
| **Print** | `print(...)` | `print("Hello")` |
| **F-string** | `f"{var}"` | `f"Nom: {name}"` |
| **Format** | `"{}".format(var)` | `"{} ans".format(25)` |
| **Concaténation** | `str1 + str2` | `"Hello" + " World"` |
| **Répétition** | `str * n` | `"Ha" * 3` → `"HaHaHa"` |
| **Indexation** | `str[index]` | `"Python"[0]` → `'P'` |
| **Slicing** | `str[start:end]` | `"Python"[0:3]` → `"Pyt"` |
| **Longueur** | `len(str)` | `len("Hello")` → `5` |

---

## Conclusion

Ce projet vous a permis de maîtriser les fondamentaux de Python :
- ✅ Affichage avec `print()`
- ✅ Formatage avec f-strings et `.format()`
- ✅ Manipulation de chaînes : indexation, slicing, concaténation
- ✅ Bonnes pratiques PEP 8
- ✅ Compréhension des concepts de base : variables, types, immutabilité

Ces compétences constituent la base essentielle pour tous vos futurs projets Python. Continuez à pratiquer et à explorer les capacités infinies de ce langage magnifique ! 🐍

**Prochaines étapes recommandées** :
1. Structures conditionnelles (`if`, `elif`, `else`)
2. Boucles (`for`, `while`)
3. Fonctions et modules
4. Structures de données (listes, dictionnaires, tuples, sets)
5. Programmation orientée objet

---

**Auteur** : Projet Holberton School  
**Date** : 2026  
**Langage** : Python 3.8+
