# 🐍 Python - Import & Modules

![Python](https://img.shields.io/badge/Python-3.8.5-blue?style=for-the-badge&logo=python)
![Ubuntu](https://img.shields.io/badge/Ubuntu-20.04_LTS-orange?style=for-the-badge&logo=ubuntu)

## 👤 Author
**GitHub:** [maxim880000](https://github.com/maxim880000)

---

## 📚 Description
Projet sur l'importation de modules en Python : comment importer des fonctions, créer ses propres modules, utiliser la variable `__name__` et les arguments en ligne de commande.

---

## 🎯 Objectifs d'Apprentissage

À la fin de ce projet, vous serez capable d'expliquer :

- Pourquoi Python est génial
- Comment importer des fonctions depuis un autre fichier
- Comment utiliser des fonctions importées
- Comment créer un module
- Comment utiliser la fonction intégrée `dir()`
- Comment empêcher le code d'un script de s'exécuter lors de l'import
- Comment utiliser les arguments de ligne de commande avec `argv`

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
| `0-add.py` | Importe une fonction et affiche le résultat d'une addition |
| `1-calculation.py` | Importe des fonctions de calcul depuis un module |
| `2-args.py` | Affiche le nombre et la liste des arguments |
| `3-infinite_add.py` | Additionne tous les arguments |
| `5-variable_load.py` | Importe une variable depuis un module |
| `add_0.py` | Module contenant la fonction `add` |
| `calculator_1.py` | Module contenant les fonctions de calcul |
| `variable_load_5.py` | Module contenant une variable |

---

## 💻 Codes et Explications

### add_0.py (Module)
```python
#!/usr/bin/python3
def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return (a + b)
```

| Élément | Description |
|:--------|:------------|
| `def add(a, b)` | Définition de fonction avec paramètres |
| `"""..."""` | Docstring - documentation de la fonction |
| `Args:` | Section décrivant les paramètres |
| `Returns:` | Section décrivant la valeur de retour |

---

### 0-add.py
```python
#!/usr/bin/python3
from add_0 import add

if __name__ == "__main__":
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
```

| Élément | Description |
|:--------|:------------|
| `from add_0 import add` | Importe la fonction `add` du module `add_0` |
| `if __name__ == "__main__":` | Exécute seulement si lancé directement |
| `__name__` | Variable spéciale contenant le nom du module |
| `"__main__"` | Valeur de `__name__` si fichier exécuté directement |

---

### calculator_1.py (Module)
```python
#!/usr/bin/python3
def add(a, b):
    return (a + b)

def sub(a, b):
    return (a - b)

def mul(a, b):
    return (a * b)

def div(a, b):
    return (a / b)
```

| Élément | Description |
|:--------|:------------|
| `add` | Fonction d'addition |
| `sub` | Fonction de soustraction |
| `mul` | Fonction de multiplication |
| `div` | Fonction de division |

---

### 1-calculation.py
```python
#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
```

| Élément | Description |
|:--------|:------------|
| `from ... import ..., ..., ...` | Import multiple de fonctions |
| `format(a, b, add(a, b))` | Formatage avec appel de fonction |

---

### 2-args.py
```python
#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    argc = len(argv) - 1

    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("1 argument:")
    else:
        print(f"{argc} arguments:")

    for i in range(1, len(argv)):
        print(f"{i}: {argv[i]}")
```

| Élément | Description |
|:--------|:------------|
| `from sys import argv` | Importe `argv` du module `sys` |
| `argv` | Liste des arguments de ligne de commande |
| `argv[0]` | Nom du script |
| `argv[1:]` | Arguments passés au script |
| `len(argv) - 1` | Nombre d'arguments (sans le nom du script) |

---

### 3-infinite_add.py
```python
#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    total = 0
    for arg in argv[1:]:
        total += int(arg)
    print(total)
```

| Élément | Description |
|:--------|:------------|
| `argv[1:]` | Tous les arguments sauf le nom du script |
| `int(arg)` | Convertit la chaîne en entier |
| `total += int(arg)` | Additionne au total |

---

### variable_load_5.py (Module)
```python
#!/usr/bin/python3
a = 98
```

| Élément | Description |
|:--------|:------------|
| `a = 98` | Variable simple dans un module |

---

### 5-variable_load.py
```python
#!/usr/bin/python3
from variable_load_5 import a

if __name__ == "__main__":
    print(a)
```

| Élément | Description |
|:--------|:------------|
| `from ... import a` | Importe une variable depuis un module |
| `print(a)` | Affiche la valeur de la variable |

---

## 📊 Tableau Récapitulatif

| Concept | Syntaxe | Description |
|:--------|:--------|:------------|
| **Import module** | `import module` | Importe tout le module |
| **Import fonction** | `from module import func` | Importe une fonction spécifique |
| **Import multiple** | `from module import f1, f2` | Importe plusieurs éléments |
| **Import tout** | `from module import *` | Importe tout (déconseillé) |
| **Alias** | `import module as m` | Crée un alias |
| **__name__** | `if __name__ == "__main__":` | Protection contre l'import |
| **argv** | `from sys import argv` | Arguments ligne de commande |
| **argv[0]** | `argv[0]` | Nom du script |
| **argv[1:]** | `argv[1:]` | Liste des arguments |
| **len(argv)** | `len(argv)` | Nombre total d'éléments |

---

## 🔑 Concept Clé : `__name__`

```python
# Quand le fichier est exécuté directement :
# __name__ == "__main__"

# Quand le fichier est importé :
# __name__ == "nom_du_module"

if __name__ == "__main__":
    # Ce code ne s'exécute que si le fichier est lancé directement
    # Pas lors d'un import
    pass
```

---

## 📊 Méthodes d'Import

| Méthode | Exemple | Utilisation |
|:--------|:--------|:------------|
| Import complet | `import math` | `math.sqrt(4)` |
| Import spécifique | `from math import sqrt` | `sqrt(4)` |
| Import avec alias | `import numpy as np` | `np.array([1,2,3])` |
| Import multiple | `from math import sqrt, pow` | `sqrt(4), pow(2,3)` |

---

## 📖 Ressources

- [Modules](https://docs.python.org/3/tutorial/modules.html)
- [Command line arguments](https://docs.python.org/3/library/sys.html#sys.argv)
- [Pycodestyle – Style Guide for Python Code](https://pypi.org/project/pycodestyle/)

---

<p align="center">Made with ❤️ at Holberton School</p>
