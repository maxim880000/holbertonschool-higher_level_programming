# 🐍 Python - Data Structures: Lists, Tuples

![Python](https://img.shields.io/badge/Python-3.8.5-blue?style=for-the-badge&logo=python)
![Ubuntu](https://img.shields.io/badge/Ubuntu-20.04_LTS-orange?style=for-the-badge&logo=ubuntu)

## 👤 Author
**GitHub:** [maxim880000](https://github.com/maxim880000)

---

## 📚 Description
Projet sur les structures de données en Python : listes (mutables), tuples (immutables), séquences et leurs méthodes.

---

## 🎯 Objectifs d'Apprentissage

À la fin de ce projet, vous serez capable d'expliquer :

- Ce que sont les listes et comment les utiliser
- Les différences et similitudes entre strings et listes
- Les méthodes les plus courantes des listes
- Comment utiliser les listes comme des piles et des files
- Ce que sont les list comprehensions et comment les utiliser
- Ce que sont les tuples et comment les utiliser
- Quand utiliser tuples vs listes
- Ce qu'est une séquence
- Ce que sont le tuple packing et unpacking
- Ce qu'est l'instruction `del` et comment l'utiliser

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
| `0-print_list_integer.py` | Affiche tous les entiers d'une liste |
| `1-element_at.py` | Récupère un élément à un index spécifique |
| `2-replace_in_list.py` | Remplace un élément à une position donnée |
| `3-print_reversed_list_integer.py` | Affiche une liste en ordre inverse |
| `4-new_in_list.py` | Remplace dans une copie de la liste |
| `5-no_c.py` | Supprime les caractères 'c' et 'C' |
| `6-print_matrix_integer.py` | Affiche une matrice d'entiers |
| `7-add_tuple.py` | Additionne 2 tuples |
| `8-multiple_returns.py` | Retourne longueur et premier caractère |
| `9-max_integer.py` | Trouve le plus grand entier |
| `10-divisible_by_2.py` | Trouve les multiples de 2 |
| `11-delete_at.py` | Supprime un élément à un index |
| `12-switch.py` | Échange deux variables |

---

## 💻 Codes et Explications

### 0-print_list_integer.py
```python
#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for i in my_list:
        print("{:d}".format(i))
```

| Élément | Description |
|:--------|:------------|
| `my_list=[]` | Paramètre avec valeur par défaut (liste vide) |
| `for i in my_list` | Parcourt chaque élément de la liste |
| `{:d}` | Format décimal (entier) |

---

### 1-element_at.py
```python
#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
```

| Élément | Description |
|:--------|:------------|
| `idx < 0` | Vérifie si index négatif |
| `idx >= len(my_list)` | Vérifie si index hors limites |
| `my_list[idx]` | Accès à un élément par son index |
| `None` | Valeur nulle en Python |

---

### 2-replace_in_list.py
```python
#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    if idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
```

| Élément | Description |
|:--------|:------------|
| `my_list[idx] = element` | Modification en place (mutable) |
| `return my_list` | Retourne la liste modifiée |

---

### 3-print_reversed_list_integer.py
```python
#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for i in range(len(my_list) - 1, -1, -1):
        print("{:d}".format(my_list[i]))
```

| Élément | Description |
|:--------|:------------|
| `range(start, stop, step)` | Génère une séquence |
| `len(my_list) - 1` | Dernier index |
| `-1` | Stop (exclusif) |
| `-1` | Step négatif (décrémentation) |

---

### 4-new_in_list.py
```python
#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list.copy()
    new_list = my_list.copy()
    new_list[idx] = element
    return new_list
```

| Élément | Description |
|:--------|:------------|
| `my_list.copy()` | Crée une copie de la liste |
| Copie superficielle | Ne modifie pas l'original |

---

### 5-no_c.py
```python
#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            new_string += char
    return new_string
```

| Élément | Description |
|:--------|:------------|
| `for char in my_string` | Parcourt chaque caractère |
| `char != 'c'` | Vérifie si différent de 'c' |
| `new_string += char` | Concaténation de string |

---

### 6-print_matrix_integer.py
```python
#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, num in enumerate(row):
            print("{:d}".format(num), end="")
            if i < len(row) - 1:
                print(" ", end="")
        print()
```

| Élément | Description |
|:--------|:------------|
| `matrix=[[]]` | Matrice vide par défaut |
| `for row in matrix` | Parcourt chaque ligne |
| `enumerate(row)` | Retourne index et valeur |
| `end=""` | Pas de saut de ligne |

---

### 7-add_tuple.py
```python
#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a1 = tuple_a[0] if len(tuple_a) >= 1 else 0
    a2 = tuple_a[1] if len(tuple_a) >= 2 else 0
    b1 = tuple_b[0] if len(tuple_b) >= 1 else 0
    b2 = tuple_b[1] if len(tuple_b) >= 2 else 0
    return (a1 + b1, a2 + b2)
```

| Élément | Description |
|:--------|:------------|
| `tuple_a=()` | Tuple vide par défaut |
| `if ... else` | Expression conditionnelle ternaire |
| `(a1 + b1, a2 + b2)` | Création d'un nouveau tuple |

---

### 8-multiple_returns.py
```python
#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first = sentence[0] if length > 0 else None
    return (length, first)
```

| Élément | Description |
|:--------|:------------|
| `len(sentence)` | Longueur de la chaîne |
| `sentence[0]` | Premier caractère |
| `return (length, first)` | Retourne un tuple |

---

### 9-max_integer.py
```python
#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    max_value = my_list[0]
    for num in my_list:
        if num > max_value:
            max_value = num
    return max_value
```

| Élément | Description |
|:--------|:------------|
| `max_value = my_list[0]` | Initialise avec le premier élément |
| `if num > max_value` | Compare avec le maximum actuel |

---

### 10-divisible_by_2.py
```python
#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = []
    for num in my_list:
        result.append(num % 2 == 0)
    return result
```

| Élément | Description |
|:--------|:------------|
| `result = []` | Liste vide pour les résultats |
| `num % 2 == 0` | True si pair, False si impair |
| `result.append()` | Ajoute à la fin de la liste |

---

### 11-delete_at.py
```python
#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx >= 0 and idx < len(my_list):
        del my_list[idx]
    return my_list
```

| Élément | Description |
|:--------|:------------|
| `del my_list[idx]` | Supprime l'élément à l'index |
| `del` | Instruction de suppression |

---

### 12-switch.py
```python
#!/usr/bin/python3
a = 89
b = 10
a, b = b, a
print("a={:d} - b={:d}".format(a, b))
```

| Élément | Description |
|:--------|:------------|
| `a, b = b, a` | Échange de variables (tuple unpacking) |

---

## 📊 Tableau Comparatif : Liste vs Tuple

| Caractéristique | Liste | Tuple |
|:----------------|:------|:------|
| **Syntaxe** | `[1, 2, 3]` | `(1, 2, 3)` |
| **Mutable** | ✅ Oui | ❌ Non |
| **Modification** | `list[0] = 5` | Impossible |
| **Ajout** | `list.append(x)` | Impossible |
| **Suppression** | `del list[0]` | Impossible |
| **Performance** | Plus lent | Plus rapide |
| **Utilisation** | Données modifiables | Données constantes |

---

## 📊 Méthodes des Listes

| Méthode | Description | Exemple |
|:--------|:------------|:--------|
| `append(x)` | Ajoute x à la fin | `list.append(5)` |
| `insert(i, x)` | Insère x à l'index i | `list.insert(0, 5)` |
| `remove(x)` | Supprime la première occurrence de x | `list.remove(5)` |
| `pop(i)` | Supprime et retourne l'élément à i | `list.pop(0)` |
| `clear()` | Vide la liste | `list.clear()` |
| `index(x)` | Retourne l'index de x | `list.index(5)` |
| `count(x)` | Compte les occurrences de x | `list.count(5)` |
| `sort()` | Trie la liste | `list.sort()` |
| `reverse()` | Inverse la liste | `list.reverse()` |
| `copy()` | Retourne une copie | `list.copy()` |

---

## 🔑 Slicing (Découpage)

| Syntaxe | Description | Exemple |
|:--------|:------------|:--------|
| `list[i]` | Élément à l'index i | `list[0]` → premier |
| `list[-i]` | i-ème depuis la fin | `list[-1]` → dernier |
| `list[a:b]` | De a à b-1 | `list[1:4]` |
| `list[:b]` | Du début à b-1 | `list[:3]` |
| `list[a:]` | De a à la fin | `list[2:]` |
| `list[::2]` | Un élément sur deux | `list[::2]` |
| `list[::-1]` | Liste inversée | `list[::-1]` |

---

## 📖 Ressources

- [Lists](https://docs.python.org/3/tutorial/introduction.html#lists)
- [Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
- [Learn to Program 6 : Lists](https://www.youtube.com/watch?v=1yUn-ydsgKk)

---

<p align="center">Made with ❤️ at Holberton School</p>
