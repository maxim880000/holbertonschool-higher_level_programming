# 🐍 Python - More Data Structures: Set, Dictionary

![Python](https://img.shields.io/badge/Python-3.8.5-blue?style=for-the-badge&logo=python)
![Ubuntu](https://img.shields.io/badge/Ubuntu-20.04_LTS-orange?style=for-the-badge&logo=ubuntu)

## 👤 Author
**GitHub:** [maxim880000](https://github.com/maxim880000)

---

## 📚 Description
Projet sur les structures de données avancées en Python : ensembles (sets), dictionnaires, fonctions lambda, et les fonctions `map`, `filter`, `reduce`.

---

## 🎯 Objectifs d'Apprentissage

À la fin de ce projet, vous serez capable d'expliquer :

- Ce que sont les sets et comment les utiliser
- Les méthodes les plus courantes des sets
- Quand utiliser sets vs listes
- Comment itérer sur un set
- Ce que sont les dictionnaires et comment les utiliser
- Quand utiliser dictionnaires vs listes/sets
- Ce qu'est une clé dans un dictionnaire
- Comment itérer sur un dictionnaire
- Ce qu'est une fonction lambda
- Ce que sont les fonctions `map`, `filter` et `reduce`

---

## 📋 Requirements

| Critère | Spécification |
|:--------|:--------------|
| OS | Ubuntu 20.04 LTS |
| Python | 3.8.5 |
| Éditeurs | vi, vim, emacs |
| Style | pycodestyle 2.7.* |
| Shebang | `#!/usr/bin/python3` |

---

## 📁 Fichiers du Projet

| Fichier | Description |
|:--------|:------------|
| `0-square_matrix_simple.py` | Calcule le carré de tous les entiers d'une matrice |
| `1-search_replace.py` | Remplace toutes les occurrences d'un élément |
| `2-uniq_add.py` | Additionne tous les entiers uniques |
| `3-common_elements.py` | Retourne les éléments communs à deux ensembles |
| `4-only_diff_elements.py` | Retourne les éléments présents dans un seul ensemble |
| `5-number_keys.py` | Retourne le nombre de clés d'un dictionnaire |
| `6-print_sorted_dictionary.py` | Affiche un dictionnaire trié par clés |
| `7-update_dictionary.py` | Remplace ou ajoute une clé/valeur |
| `8-simple_delete.py` | Supprime une clé d'un dictionnaire |
| `9-multiply_by_2.py` | Multiplie toutes les valeurs par 2 |
| `10-best_score.py` | Retourne la clé avec la plus grande valeur |
| `11-multiply_list_map.py` | Multiplie une liste avec map et lambda |
| `12-roman_to_int.py` | Convertit un chiffre romain en entier |

---

## 💻 Codes et Explications

### 0-square_matrix_simple.py
```python
#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [[num ** 2 for num in row] for row in matrix]
```

| Élément | Description |
|:--------|:------------|
| `[[...] for row in matrix]` | List comprehension imbriquée |
| `num ** 2` | Carré de chaque nombre |
| `for num in row` | Parcourt chaque élément de la ligne |
| `for row in matrix` | Parcourt chaque ligne de la matrice |

---

### 1-search_replace.py
```python
#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return [replace if item == search else item for item in my_list]
```

| Élément | Description |
|:--------|:------------|
| `replace if item == search else item` | Expression conditionnelle |
| `for item in my_list` | Parcourt la liste |

---

### 2-uniq_add.py
```python
#!/usr/bin/python3
def uniq_add(my_list=[]):
    return sum(set(my_list))
```

| Élément | Description |
|:--------|:------------|
| `set(my_list)` | Convertit en set (élimine les doublons) |
| `sum()` | Additionne tous les éléments |

---

### 3-common_elements.py
```python
#!/usr/bin/python3
def common_elements(set_1, set_2):
    return set_1 & set_2
```

| Élément | Description |
|:--------|:------------|
| `&` | Opérateur d'intersection de sets |
| Intersection | Éléments présents dans les deux ensembles |

---

### 4-only_diff_elements.py
```python
#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    return set_1 ^ set_2
```

| Élément | Description |
|:--------|:------------|
| `^` | Opérateur de différence symétrique |
| Différence symétrique | Éléments dans l'un OU l'autre, mais pas les deux |

---

### 5-number_keys.py
```python
#!/usr/bin/python3
def number_keys(a_dictionary):
    return len(a_dictionary)
```

| Élément | Description |
|:--------|:------------|
| `len(a_dictionary)` | Nombre de clés dans le dictionnaire |

---

### 6-print_sorted_dictionary.py
```python
#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for key in sorted(a_dictionary.keys()):
        print("{}: {}".format(key, a_dictionary[key]))
```

| Élément | Description |
|:--------|:------------|
| `sorted(a_dictionary.keys())` | Trie les clés alphabétiquement |
| `a_dictionary[key]` | Accède à la valeur par la clé |

---

### 7-update_dictionary.py
```python
#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    return a_dictionary
```

| Élément | Description |
|:--------|:------------|
| `a_dictionary[key] = value` | Ajoute ou met à jour une clé |

---

### 8-simple_delete.py
```python
#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
```

| Élément | Description |
|:--------|:------------|
| `key in a_dictionary` | Vérifie si la clé existe |
| `del a_dictionary[key]` | Supprime la clé et sa valeur |

---

### 9-multiply_by_2.py
```python
#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = {}
    for key, value in a_dictionary.items():
        new_dictionary[key] = value * 2
    return new_dictionary
```

| Élément | Description |
|:--------|:------------|
| `a_dictionary.items()` | Retourne paires (clé, valeur) |
| `for key, value in ...` | Décompose chaque paire |

---

### 10-best_score.py
```python
#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    best_key = None
    best_value = None
    for key, value in a_dictionary.items():
        if best_value is None or value > best_value:
            best_value = value
            best_key = key
    return best_key
```

| Élément | Description |
|:--------|:------------|
| `if not a_dictionary` | Vérifie si dict vide ou None |
| `best_value is None` | Vérifie si pas encore initialisé |

---

### 11-multiply_list_map.py
```python
#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    return list(map(lambda x: x * number, my_list))
```

| Élément | Description |
|:--------|:------------|
| `lambda x: x * number` | Fonction anonyme |
| `map(func, iterable)` | Applique func à chaque élément |
| `list()` | Convertit le résultat en liste |

---

### 12-roman_to_int.py
```python
#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                  'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0
    for char in reversed(roman_string):
        value = roman_dict.get(char, 0)
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    return total
```

| Élément | Description |
|:--------|:------------|
| `isinstance(roman_string, str)` | Vérifie le type |
| `roman_dict.get(char, 0)` | Récupère valeur ou 0 par défaut |
| `reversed(roman_string)` | Parcourt de droite à gauche |
| Règle romaine | Si valeur < précédente, on soustrait |

---

## 📊 Tableau Comparatif : Set vs Liste vs Dict

| Caractéristique | Liste | Set | Dict |
|:----------------|:------|:----|:-----|
| **Syntaxe** | `[1, 2, 3]` | `{1, 2, 3}` | `{"a": 1}` |
| **Ordre** | ✅ Ordonné | ❌ Non ordonné | ✅ Ordonné (3.7+) |
| **Doublons** | ✅ Autorisés | ❌ Interdits | Clés uniques |
| **Accès** | Par index | Pas d'index | Par clé |
| **Mutable** | ✅ Oui | ✅ Oui | ✅ Oui |

---

## 📊 Opérations sur les Sets

| Opération | Syntaxe | Description |
|:----------|:--------|:------------|
| **Union** | `set1 | set2` | Tous les éléments |
| **Intersection** | `set1 & set2` | Éléments communs |
| **Différence** | `set1 - set2` | Dans set1 mais pas set2 |
| **Diff. symétrique** | `set1 ^ set2` | Dans l'un ou l'autre, pas les deux |
| **Ajout** | `set.add(x)` | Ajoute un élément |
| **Suppression** | `set.remove(x)` | Supprime (erreur si absent) |
| **Suppression safe** | `set.discard(x)` | Supprime (pas d'erreur) |

---

## 📊 Méthodes des Dictionnaires

| Méthode | Description | Exemple |
|:--------|:------------|:--------|
| `keys()` | Retourne les clés | `dict.keys()` |
| `values()` | Retourne les valeurs | `dict.values()` |
| `items()` | Retourne paires (clé, valeur) | `dict.items()` |
| `get(key, default)` | Valeur ou default | `dict.get("x", 0)` |
| `pop(key)` | Supprime et retourne | `dict.pop("x")` |
| `update(dict2)` | Fusionne deux dicts | `dict.update(dict2)` |
| `clear()` | Vide le dictionnaire | `dict.clear()` |

---

## 🔑 Fonctions Lambda, Map, Filter

### Lambda (Fonction Anonyme)
```python
# Syntaxe : lambda arguments: expression
square = lambda x: x ** 2
add = lambda a, b: a + b
```

### Map (Applique une fonction)
```python
# map(fonction, iterable)
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, numbers))
# [1, 4, 9, 16]
```

### Filter (Filtre les éléments)
```python
# filter(fonction, iterable)
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
# [2, 4, 6]
```

---

## 📖 Ressources

- [Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
- [Lambda, filter, reduce and map](https://www.python-course.eu/lambda.php)
- [Learn to Program 12: Lambda Map Filter Reduce](https://www.youtube.com/watch?v=1GAC6KQUPeg)

---

<p align="center">Made with ❤️ at Holberton School</p>
