# Python - Import & Modules 🐍

## Description du Projet

Ce projet explore les systèmes d'import et de modularisation en Python, concepts fondamentaux pour organiser et structurer du code de manière professionnelle. Vous apprendrez à créer des modules réutilisables, à importer des fonctions et variables depuis d'autres fichiers, à gérer les arguments de ligne de commande, et à comprendre les mécanismes d'exécution des scripts Python. La modularisation est essentielle pour créer des applications maintenables, évolutives et conformes aux principes DRY (Don't Repeat Yourself).

## Objectifs d'Apprentissage

À la fin de ce projet, vous serez capable d'expliquer sans aide extérieure :

### Modules et Imports
- **Comprendre les modules** : Qu'est-ce qu'un module Python
- **Importer des fonctions** : Syntaxe `from module import function`
- **Importer des modules complets** : `import module`
- **Créer des modules** : Organiser son code en fichiers réutilisables
- **Éviter les exécutions non désirées** : Rôle de `if __name__ == "__main__"`

### Arguments de Ligne de Commande
- **Module `sys`** : Accéder aux arguments système
- **Variable `sys.argv`** : Liste des arguments passés au script
- **Compter les arguments** : `len(sys.argv)`
- **Traiter les arguments** : Itération et conversion

### Bonnes Pratiques
- **Éviter l'exécution d'imports** : Protéger le code principal
- **Documentation de modules** : Docstrings au niveau module
- **Gestion des chemins** : Organisation des fichiers
- **Imports spécifiques** : Importer uniquement ce dont on a besoin

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

### 1. Qu'est-ce qu'un Module ?

Un **module** est un fichier Python (`.py`) contenant des définitions de fonctions, classes, variables et code exécutable.

**Avantages des modules** :
- ✅ **Réutilisabilité** : Utiliser le même code dans plusieurs programmes
- ✅ **Organisation** : Séparer le code en fichiers logiques
- ✅ **Maintenabilité** : Modifications centralisées
- ✅ **Namespace** : Éviter les conflits de noms
- ✅ **Partage** : Distribuer du code à d'autres développeurs

**Exemple de module** :
```python
# Fichier: math_utils.py
"""Module contenant des fonctions mathématiques utiles."""

def add(a, b):
    """Additionne deux nombres."""
    return a + b

def multiply(a, b):
    """Multiplie deux nombres."""
    return a * b

PI = 3.14159
```

### 2. Importer des Modules

Il existe plusieurs façons d'importer des modules en Python.

#### Méthode 1 : `import module`

```python
# Importe le module entier
import math_utils

# Utilisation avec préfixe
resultat = math_utils.add(5, 3)
print(resultat)  # 8
print(math_utils.PI)  # 3.14159
```

**Avantages** :
- Clair sur la provenance des fonctions
- Évite les conflits de noms
- Namespace explicite

**Inconvénient** :
- Syntaxe plus longue

#### Méthode 2 : `from module import fonction`

```python
# Importe des éléments spécifiques
from math_utils import add, PI

# Utilisation directe (sans préfixe)
resultat = add(5, 3)
print(resultat)  # 8
print(PI)  # 3.14159
```

**Avantages** :
- Syntaxe courte
- Import sélectif (performances)

**Inconvénient** :
- Risque de conflit de noms

#### Méthode 3 : `from module import *`

```python
# Importe TOUT (⚠️ déconseillé)
from math_utils import *

resultat = add(5, 3)
print(PI)
```

**⚠️ À ÉVITER** :
- Pollue le namespace
- Difficile de savoir d'où viennent les fonctions
- Risque élevé de conflits

#### Méthode 4 : `import module as alias`

```python
# Alias pour un nom court
import math_utils as mu

resultat = mu.add(5, 3)
```

**Cas d'usage** :
- Modules avec noms longs
- Conventions (ex: `import numpy as np`)

### 3. Le Module `sys`

Le module **`sys`** (system) fournit des fonctions et variables liées à l'interpréteur Python et au système.

**Import** :
```python
import sys
```

**Fonctionnalités principales** :

| Élément | Description | Exemple |
|---------|-------------|---------|
| `sys.argv` | Liste des arguments CLI | `['script.py', 'arg1', 'arg2']` |
| `sys.exit()` | Quitter le programme | `sys.exit(0)` |
| `sys.path` | Chemins de recherche de modules | `['/usr/lib/python3', ...]` |
| `sys.version` | Version de Python | `'3.8.10 (default...)'` |
| `sys.platform` | Plateforme système | `'linux'`, `'win32'`, `'darwin'` |
| `sys.stdin` | Entrée standard | Lecture depuis le terminal |
| `sys.stdout` | Sortie standard | Écriture vers le terminal |
| `sys.stderr` | Sortie d'erreur | Messages d'erreur |

### 4. Arguments de Ligne de Commande (`sys.argv`)

`sys.argv` est une **liste** contenant les arguments passés au script lors de son exécution.

**Structure** :
```python
sys.argv[0]  # Nom du script
sys.argv[1]  # Premier argument
sys.argv[2]  # Deuxième argument
...
```

**Exemple** :
```bash
$ python3 script.py arg1 arg2 arg3
```

```python
import sys

print(sys.argv)
# Output: ['script.py', 'arg1', 'arg2', 'arg3']

print(sys.argv[0])  # 'script.py'
print(sys.argv[1])  # 'arg1'
print(len(sys.argv))  # 4 (script + 3 arguments)
```

**Nombre d'arguments** :
```python
argc = len(sys.argv) - 1  # Exclut le nom du script
print(f"{argc} arguments")
```

**Itération sur les arguments** :
```python
# Tous les arguments (y compris le script)
for arg in sys.argv:
    print(arg)

# Arguments uniquement (sans le script)
for arg in sys.argv[1:]:
    print(arg)

# Avec index
for i, arg in enumerate(sys.argv):
    print(f"argv[{i}] = {arg}")
```

**Conversion de types** :
```python
# sys.argv contient des CHAÎNES
# Conversion nécessaire pour les nombres

import sys

# argv[1] est une chaîne "42"
nombre = int(sys.argv[1])  # Conversion en entier
print(nombre + 10)  # 52

# Conversion flottante
prix = float(sys.argv[1])
```

### 5. `if __name__ == "__main__"`

Cette construction est **cruciale** pour créer des modules réutilisables.

#### Problème à résoudre

```python
# Fichier: mon_module.py
def saluer(nom):
    print(f"Bonjour, {nom}!")

# Code de test
saluer("Alice")  # ⚠️ S'exécute TOUJOURS, même lors d'un import!
```

Si on importe ce module :
```python
import mon_module  # Affiche "Bonjour, Alice!" (non désiré!)
```

#### Solution avec `if __name__ == "__main__"`

```python
# Fichier: mon_module.py
def saluer(nom):
    print(f"Bonjour, {nom}!")

# Code exécuté UNIQUEMENT si lancé directement
if __name__ == "__main__":
    saluer("Alice")
```

**Comportement** :

1. **Exécution directe** :
```bash
$ python3 mon_module.py
Bonjour, Alice!  # ✅ S'exécute
```

2. **Import** :
```python
import mon_module  # ✅ Rien ne s'affiche
mon_module.saluer("Bob")  # Bonjour, Bob!
```

#### Explication

- **`__name__`** : Variable spéciale Python
  - Valeur lors de l'exécution directe : `"__main__"`
  - Valeur lors d'un import : nom du module (ex: `"mon_module"`)

**Analogie** :
```python
# Fichier: exemple.py
print(f"__name__ vaut : {__name__}")

if __name__ == "__main__":
    print("Je suis exécuté directement")
else:
    print("Je suis importé")
```

```bash
# Exécution directe
$ python3 exemple.py
__name__ vaut : __main__
Je suis exécuté directement

# Import
$ python3
>>> import exemple
__name__ vaut : exemple
Je suis importé
```

#### Cas d'usage typique

```python
# Fichier: calculator.py
"""Module de calcul."""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# Tests/exemples uniquement si exécuté directement
if __name__ == "__main__":
    print("Tests du module calculator")
    print(f"5 + 3 = {add(5, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
```

### 6. Chemins de Recherche de Modules (`sys.path`)

Lorsque Python cherche un module, il parcourt les répertoires listés dans `sys.path`.

```python
import sys
print(sys.path)
```

**Ordre de recherche** :
1. Répertoire courant (où se trouve le script)
2. Variable d'environnement `PYTHONPATH`
3. Répertoires d'installation standard (`/usr/lib/python3.x/`)
4. Répertoires de packages installés (site-packages)

**Ajouter un chemin** :
```python
import sys
sys.path.append('/mon/repertoire/perso')
import mon_module  # Cherché aussi dans /mon/repertoire/perso
```

### 7. Variables Spéciales de Module

Chaque module possède des variables spéciales :

| Variable | Description | Exemple |
|----------|-------------|---------|
| `__name__` | Nom du module | `"mon_module"` ou `"__main__"` |
| `__file__` | Chemin du fichier | `"/path/to/mon_module.py"` |
| `__doc__` | Docstring du module | Première chaîne du fichier |
| `__package__` | Package parent | `"mon_package"` |
| `__dict__` | Namespace du module | Dictionnaire des attributs |

**Exemple** :
```python
# Fichier: info.py
"""Ce module affiche ses propres informations."""

import sys

def afficher_info():
    print(f"Nom : {__name__}")
    print(f"Fichier : {__file__}")
    print(f"Doc : {__doc__}")

if __name__ == "__main__":
    afficher_info()
```

---

## Fichiers du Projet

### 📄 add_0.py

**Objectif** : Module contenant une fonction d'addition

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

**Notions utilisées** :
1. **Définition de fonction** : `def add(a, b):`
2. **Docstring détaillée** : Documentation Google Style
3. **Parenthèses autour du return** : Style optionnel mais explicite

**Explication détaillée** :

**Structure de la docstring** :
```python
"""Description courte sur une ligne

Args:
    param1: Description du paramètre 1
    param2: Description du paramètre 2

Returns:
    Description de la valeur de retour
"""
```

**Format Google Style** :
- Utilisé dans les projets Google et largement adopté
- Sections : Args, Returns, Raises, Examples, Note, etc.
- Alternative : NumPy Style, reStructuredText

**Utilisation du module** :
```python
# Dans un autre fichier
from add_0 import add

resultat = add(5, 3)
print(resultat)  # 8
```

**Accès à la documentation** :
```python
from add_0 import add

# Afficher la docstring
print(add.__doc__)

# Aide interactive
help(add)
```

---

### 📄 0-add.py

**Objectif** : Importer et utiliser la fonction `add` du module `add_0`

```python
#!/usr/bin/python3
# Importe la fonction add depuis le fichier add_0.py
from add_0 import add

# Vérifie que le fichier est exécuté directement
# et pas importé depuis un autre fichier
if __name__ == "__main__":
    # Déclaration de la première variable
    a = 1

    # Déclaration de la deuxième variable
    b = 2

    # Affiche le calcul et le résultat de l'addition
    print("{} + {} = {}".format(a, b, add(a, b)))
```

**Notions utilisées** :
1. **Import spécifique** : `from module import fonction`
2. **Protection d'exécution** : `if __name__ == "__main__"`
3. **Utilisation de fonction importée** : `add(a, b)`

**Explication détaillée** :

**L'import** :
```python
from add_0 import add
```
- `add_0` : Nom du fichier (sans `.py`)
- `add` : Nom de la fonction à importer
- Résultat : `add()` est directement accessible (pas besoin de `add_0.add()`)

**Pourquoi `if __name__ == "__main__"` ?**
- Permet d'importer `0-add.py` dans un autre script sans exécuter le code de test
- Le code dans le `if` ne s'exécute que si on lance directement `0-add.py`

**Déroulement** :

1. **Exécution directe** :
```bash
$ python3 0-add.py
1 + 2 = 3
```

2. **Import (hypothétique)** :
```python
import 0-add  # Rien ne s'affiche (if __name__ == "__main__" est False)
```

**Formatage de sortie** :
```python
print("{} + {} = {}".format(a, b, add(a, b)))
#      │    │    └─── Résultat de add(1, 2) = 3
#      │    └──────── Valeur de b (2)
#      └───────────── Valeur de a (1)
# Output: "1 + 2 = 3"
```

**Sortie attendue** :
```
1 + 2 = 3
```

---

### 📄 calculator_1.py

**Objectif** : Module contenant 4 fonctions de calcul

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


def sub(a, b):
    """My subtraction function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a - b
    """
    return (a - b)


def mul(a, b):
    """My multiplication function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a * b
    """
    return (a * b)


def div(a, b):
    """My division function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a / b
    """
    return int(a / b)
```

**Notions utilisées** :
1. **Module avec plusieurs fonctions** : Organisation logique
2. **Division entière** : `int(a / b)`
3. **Fonctions homogènes** : Interface cohérente

**Explication détaillée** :

**Organisation du module** :
- Toutes les fonctions ont la même signature : `func(a, b)`
- Retournent toutes un nombre
- Documentées de manière uniforme

**Division entière** :
```python
def div(a, b):
    return int(a / b)
```

**Analyse** :
- `a / b` effectue une division flottante (Python 3)
- `int()` convertit le résultat en entier (troncature)

**Exemples** :
```python
div(10, 3)   # int(3.333...) = 3
div(7, 2)    # int(3.5) = 3
div(20, 5)   # int(4.0) = 4
div(10, 4)   # int(2.5) = 2
```

**⚠️ Différence avec `//`** :
```python
# Notre fonction
int(10 / 3)  # 3 (conversion en int)

# Opérateur de division entière
10 // 3      # 3 (division entière directe)

# Différence avec nombres négatifs
int(-7 / 2)  # -3 (troncature vers zéro)
-7 // 2      # -4 (arrondi vers moins l'infini)
```

**Utilisation du module** :
```python
from calculator_1 import add, sub, mul, div

print(add(10, 5))  # 15
print(sub(10, 5))  # 5
print(mul(10, 5))  # 50
print(div(10, 5))  # 2
```

---

### 📄 1-calculation.py

**Objectif** : Importer et utiliser toutes les fonctions du calculateur

```python
#!/usr/bin/python3
# Importe les fonctions nécessaires depuis le fichier
from calculator_1 import add, sub, mul, div

# Vérifie que le fichier est exécuté directement
# et non importé dans un autre script
if __name__ == "__main__":
    # Déclaration de la première variable
    a = 10

    # Déclaration de la deuxième variable
    b = 5

    # Affiche le résultat de l'addition
    print("{} + {} = {}".format(a, b, add(a, b)))

    # Affiche le résultat de la soustraction
    print("{} - {} = {}".format(a, b, sub(a, b)))

    # Affiche le résultat de la multiplication
    print("{} * {} = {}".format(a, b, mul(a, b)))

    # Affiche le résultat de la division
    print("{} / {} = {}".format(a, b, div(a, b)))
```

**Notions utilisées** :
1. **Import multiple** : `from module import func1, func2, func3, func4`
2. **Utilisation de plusieurs fonctions** : Calculs variés
3. **Formatage cohérent** : Même style pour tous les affichages

**Explication détaillée** :

**Import multiple** :
```python
from calculator_1 import add, sub, mul, div
```

**Équivalent à** :
```python
from calculator_1 import add
from calculator_1 import sub
from calculator_1 import mul
from calculator_1 import div
```

**Ou avec alias** :
```python
import calculator_1 as calc
calc.add(10, 5)
calc.sub(10, 5)
# etc.
```

**Déroulement des calculs** :
```python
a = 10
b = 5

add(10, 5)  # 10 + 5 = 15
sub(10, 5)  # 10 - 5 = 5
mul(10, 5)  # 10 * 5 = 50
div(10, 5)  # int(10 / 5) = int(2.0) = 2
```

**Sortie attendue** :
```
10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2
```

**Structure claire** :
- Chaque opération sur une ligne
- Format identique : `{a} {opérateur} {b} = {résultat}`
- Facile à lire et à comprendre

---

### 📄 2-args.py

**Objectif** : Afficher le nombre et la liste des arguments de ligne de commande

```python
#!/usr/bin/python3
from sys import argv
# On importe argv pour récupérer les arguments de la ligne de commande

if __name__ == "__main__":
    argc = len(argv) - 1
    # On calcule le nombre réel d'arguments (sans le nom du script)

    # Affichage de la première ligne selon le nombre d'arguments
    if argc == 0:
        print("0 arguments.")  # Pas d'arguments 1
    elif argc == 1:
        print("1 argument:")  # Un argument +2
    else:
        print(f"{argc} arguments:")  # Plusieurs arguments +2

    # Boucle pour afficher chaque argument avec son numéro
    for i in range(1, len(argv)):  # On commence à 1 pass le nom du script
        print(f"{i}: {argv[i]}")  # Affiche le numéro et l'argument
```

**Notions utilisées** :
1. **Import de `sys.argv`** : `from sys import argv`
2. **Calcul du nombre d'arguments** : `len(argv) - 1`
3. **Pluralisation conditionnelle** : "argument" vs "arguments"
4. **Itération sur les arguments** : `for i in range(1, len(argv))`

**Explication détaillée** :

**Import de `argv`** :
```python
from sys import argv
```
- Importe uniquement `argv` du module `sys`
- Permet d'utiliser `argv` au lieu de `sys.argv`

**Calcul du nombre d'arguments** :
```python
argc = len(argv) - 1
```

**Pourquoi `-1` ?**
- `argv[0]` contient le nom du script
- Les vrais arguments commencent à `argv[1]`

**Exemple** :
```bash
$ python3 2-args.py arg1 arg2 arg3
```

```python
argv = ['2-args.py', 'arg1', 'arg2', 'arg3']
len(argv)      # 4
argc = 4 - 1   # 3 (nombre réel d'arguments)
```

**Logique de pluralisation** :
```python
if argc == 0:
    print("0 arguments.")
elif argc == 1:
    print("1 argument:")  # Singulier
else:
    print(f"{argc} arguments:")  # Pluriel
```

**Détails importants** :
- `0 arguments.` : Point final (pas de liste à afficher)
- `1 argument:` : Deux-points (liste suit)
- `N arguments:` : Deux-points (liste suit)

**Itération sur les arguments** :
```python
for i in range(1, len(argv)):
    print(f"{i}: {argv[i]}")
```

- `range(1, len(argv))` : Commence à 1, exclut le nom du script
- Affiche le numéro de position et la valeur

**Exemples de sortie** :

```bash
# Aucun argument
$ python3 2-args.py
0 arguments.

# Un argument
$ python3 2-args.py Hello
1 argument:
1: Hello

# Plusieurs arguments
$ python3 2-args.py Hello World Python
3 arguments:
1: Hello
2: World
3: Python

# Arguments avec espaces (guillemets nécessaires)
$ python3 2-args.py "Hello World" Python
2 arguments:
1: Hello World
2: Python
```

**Analyse technique** :

| Commande | `argv` | `argc` | Sortie |
|----------|--------|--------|--------|
| `python3 2-args.py` | `['2-args.py']` | 0 | `0 arguments.` |
| `python3 2-args.py Hello` | `['2-args.py', 'Hello']` | 1 | `1 argument:\n1: Hello` |
| `python3 2-args.py A B C` | `['2-args.py', 'A', 'B', 'C']` | 3 | `3 arguments:\n1: A\n2: B\n3: C` |

---

### 📄 3-infinite_add.py

**Objectif** : Additionner tous les arguments numériques passés au script

```python
#!/usr/bin/python3
from sys import argv  # Pour récupérer les arguments passés au script

if __name__ == "__main__":
    total = 0  # On initialise le total à zéro

    # On parcourt tous les arguments sauf le nom du fichier
    for arg in argv[1:]:
        total += int(arg)
        # On convertit chaque argument en entier et on l'ajoute au total

    print(total)  # On affiche le résultat final
```

**Notions utilisées** :
1. **Slicing de liste** : `argv[1:]`
2. **Conversion de type** : `int(arg)`
3. **Accumulation** : `total += value`
4. **Itération directe** : `for arg in liste`

**Explication détaillée** :

**Slicing `argv[1:]`** :
```python
argv = ['3-infinite_add.py', '5', '10', '15', '20']
argv[1:]  # ['5', '10', '15', '20']
```

- `[1:]` : Depuis l'indice 1 jusqu'à la fin
- Exclut `argv[0]` (nom du script)
- Retourne une **nouvelle liste**

**Accumulation** :
```python
total = 0
for arg in argv[1:]:
    total += int(arg)
```

**Déroulement avec `argv = ['script.py', '5', '10', '15']`** :
```
Initialisation: total = 0

Itération 1: arg = '5'
  int('5') = 5
  total = 0 + 5 = 5

Itération 2: arg = '10'
  int('10') = 10
  total = 5 + 10 = 15

Itération 3: arg = '15'
  int('15') = 15
  total = 15 + 15 = 30

Résultat: print(30)
```

**Conversion `int(arg)`** :
- Les arguments dans `argv` sont toujours des **chaînes**
- `int()` convertit la chaîne en entier
- **Erreur** si l'argument n'est pas un nombre valide

```python
int('42')    # 42 ✅
int('3.14')  # ValueError ❌ (utiliser float())
int('abc')   # ValueError ❌
```

**Exemples de sortie** :

```bash
# Aucun argument
$ python3 3-infinite_add.py
0

# Un nombre
$ python3 3-infinite_add.py 42
42

# Plusieurs nombres
$ python3 3-infinite_add.py 1 2 3 4 5
15

# Grands nombres
$ python3 3-infinite_add.py 100 200 300
600

# Nombres négatifs
$ python3 3-infinite_add.py 10 -5 3
8
```

**Gestion d'erreurs (non implémentée ici)** :
```python
# Version robuste
if __name__ == "__main__":
    total = 0
    for arg in argv[1:]:
        try:
            total += int(arg)
        except ValueError:
            print(f"Erreur: '{arg}' n'est pas un entier valide")
            sys.exit(1)
    print(total)
```

**Alternative avec `sum()` et compréhension** :
```python
if __name__ == "__main__":
    total = sum(int(arg) for arg in argv[1:])
    print(total)
```

---

### 📄 variable_load_5.py

**Objectif** : Module contenant une variable simple

```python
#!/usr/bin/python3
a = 98
"""Simple variable
"""
```

**Notions utilisées** :
1. **Variable de module** : Variable au niveau du module
2. **Docstring de module** : Documentation du module

**Explication détaillée** :

**Variable de module** :
- `a = 98` : Définie au niveau du module (pas dans une fonction)
- Accessible depuis d'autres fichiers via import
- Fait partie du **namespace** du module

**Docstring de module** :
```python
"""Simple variable
"""
```
- Documentation du module
- Accessible via `module.__doc__`
- Apparaît dans `help(module)`

**Utilisation** :
```python
# Dans un autre fichier
from variable_load_5 import a

print(a)  # 98
```

---

### 📄 5-variable_load.py

**Objectif** : Importer et afficher la variable `a` du module `variable_load_5`

```python
#!/usr/bin/python3
from variable_load_5 import a  # On importe uniquement la variable 'a'

if __name__ == "__main__":
    # S'assure que ce code ne s'exécute que si lancé directement
    print(a)  # Affiche la valeur de 'a'
```

**Notions utilisées** :
1. **Import de variable** : `from module import variable`
2. **Protection d'exécution** : `if __name__ == "__main__"`
3. **Affichage simple** : `print(a)`

**Explication détaillée** :

**Import de variable** :
```python
from variable_load_5 import a
```

- Importe la variable `a` depuis le module `variable_load_5`
- `a` est directement accessible (pas besoin de `variable_load_5.a`)
- La valeur est **copiée** lors de l'import

**⚠️ Important** : Modification après import

```python
# Dans variable_load_5.py
a = 98

# Dans 5-variable_load.py
from variable_load_5 import a
print(a)  # 98

a = 100  # Modifie la COPIE locale, pas l'originale
print(a)  # 100

# Dans variable_load_5.py, a vaut toujours 98
```

**Pour modifier la variable du module** :
```python
import variable_load_5

print(variable_load_5.a)  # 98
variable_load_5.a = 100   # Modifie l'original
print(variable_load_5.a)  # 100
```

**Sortie attendue** :
```bash
$ python3 5-variable_load.py
98
```

---

## Commandes Importantes

### Exécution avec Arguments

```bash
# Sans arguments
python3 script.py

# Avec arguments
python3 script.py arg1 arg2 arg3

# Arguments avec espaces (guillemets nécessaires)
python3 script.py "Hello World" "Python 3"

# Arguments numériques
python3 3-infinite_add.py 1 2 3 4 5

# Mélange
python3 script.py --option valeur 42 "texte"
```

### Tests d'Import

```bash
# Mode interactif
$ python3
>>> from add_0 import add
>>> add(5, 3)
8
>>> exit()

# Import et test dans un script
$ python3 -c "from add_0 import add; print(add(10, 20))"
30

# Vérifier qu'un module s'importe sans erreur
$ python3 -c "import calculator_1"
# Pas d'output = succès

# Lister le contenu d'un module
$ python3 -c "import calculator_1; print(dir(calculator_1))"
```

### Inspection de Modules

```bash
# Aide sur un module
$ python3
>>> import calculator_1
>>> help(calculator_1)
>>> help(calculator_1.add)
>>> exit()

# Docstring
$ python3 -c "from add_0 import add; print(add.__doc__)"

# Attributs du module
$ python3 -c "import sys; print(sys.argv)"
```

### Gestion de `sys.path`

```bash
# Afficher les chemins de recherche
$ python3 -c "import sys; print('\n'.join(sys.path))"

# Ajouter un chemin temporairement
$ PYTHONPATH=/mon/chemin python3 script.py

# Permanent (dans le script)
import sys
sys.path.insert(0, '/mon/chemin')
```

---

## Concepts Avancés

### 1. Imports Relatifs vs Absolus

#### Imports Absolus (recommandé)
```python
# Depuis la racine du projet
from mon_package.mon_module import ma_fonction
```

#### Imports Relatifs
```python
# Dans un package
from . import module_frere        # Même niveau
from .. import module_parent       # Niveau supérieur
from .sous_package import module   # Sous-package
```

**Exemple de structure** :
```
mon_projet/
├── main.py
└── mon_package/
    ├── __init__.py
    ├── module_a.py
    └── sous_package/
        ├── __init__.py
        └── module_b.py
```

```python
# Dans module_b.py
from .. import module_a          # Import relatif
from mon_package import module_a  # Import absolu (préféré)
```

### 2. Le Fichier `__init__.py`

Transforme un répertoire en **package** Python.

```python
# mon_package/__init__.py
"""Package de calcul mathématique."""

from .calculator import add, sub
from .geometry import area, perimeter

__version__ = "1.0.0"
__all__ = ['add', 'sub', 'area', 'perimeter']
```

**Utilisation** :
```python
import mon_package

mon_package.add(5, 3)
print(mon_package.__version__)  # 1.0.0
```

### 3. L'Attribut `__all__`

Contrôle ce qui est importé avec `from module import *`.

```python
# mon_module.py
__all__ = ['fonction_publique', 'CONSTANTE']

def fonction_publique():
    pass

def _fonction_privee():  # Préfixe _ = conventionnellement privée
    pass

CONSTANTE = 42
_variable_privee = "secret"
```

```python
from mon_module import *

fonction_publique()  # ✅ Disponible
CONSTANTE            # ✅ Disponible
_fonction_privee()   # ❌ Pas importée
```

### 4. Import Circulaire (à éviter)

```python
# module_a.py
from module_b import func_b  # ❌ Import de B

def func_a():
    return func_b()

# module_b.py
from module_a import func_a  # ❌ Import de A

def func_b():
    return func_a()  # Erreur: ImportError (circular import)
```

**Solution** : Restructurer le code ou importer dans les fonctions

```python
# module_a.py
def func_a():
    from module_b import func_b  # ✅ Import local
    return func_b()
```

### 5. Modules Standards Utiles

| Module | Utilité | Exemple |
|--------|---------|---------|
| `os` | Système d'exploitation | `os.path.exists()`, `os.listdir()` |
| `sys` | Interpréteur Python | `sys.argv`, `sys.exit()` |
| `math` | Fonctions mathématiques | `math.sqrt()`, `math.pi` |
| `random` | Nombres aléatoires | `random.randint()`, `random.choice()` |
| `datetime` | Dates et heures | `datetime.now()`, `timedelta()` |
| `json` | JSON | `json.loads()`, `json.dumps()` |
| `re` | Expressions régulières | `re.search()`, `re.findall()` |
| `pathlib` | Chemins modernes | `Path()`, `.exists()` |

### 6. Reload de Module (développement)

```python
import importlib

import mon_module
# ... modifications de mon_module.py ...
importlib.reload(mon_module)  # Recharge le module
```

---

## Bonnes Pratiques Détaillées

### 1. Organisation des Imports

```python
#!/usr/bin/python3
"""Docstring du module."""

# 1. Imports de la bibliothèque standard
import os
import sys
from datetime import datetime

# 2. Imports de bibliothèques tierces
import numpy as np
import requests

# 3. Imports locaux (votre projet)
from mon_package import mon_module
from .utils import helper_function

# 4. Constantes
MAX_SIZE = 100
DEFAULT_NAME = "unknown"

# 5. Code du module
def ma_fonction():
    pass
```

**Ordre PEP 8** :
1. Bibliothèque standard
2. Bibliothèques tierces
3. Imports locaux

**Séparation** : Ligne vide entre chaque groupe

### 2. Nommage de Modules

```python
# ✅ BON
mon_module.py          # snake_case
calcul_scientifique.py
traitement_donnees.py

# ❌ MAUVAIS
MonModule.py           # PascalCase (réservé aux classes)
calculScientifique.py  # camelCase
traitement-donnees.py  # Tirets (invalide)
2_module.py            # Commence par un chiffre (invalide)
```

### 3. Documentation de Module

```python
#!/usr/bin/python3
"""Module de calcul mathématique avancé.

Ce module fournit des fonctions pour effectuer des calculs
mathématiques complexes incluant l'algèbre linéaire,
les statistiques et l'analyse numérique.

Example:
    >>> from math_utils import moyenne
    >>> moyenne([1, 2, 3, 4, 5])
    3.0

Attributes:
    PI (float): Constante pi avec précision étendue
    E (float): Constante e (nombre d'Euler)

Todo:
    * Ajouter support pour les nombres complexes
    * Optimiser les calculs matriciels
"""

PI = 3.14159265359
E = 2.71828182846

def moyenne(liste):
    """Calcule la moyenne arithmétique d'une liste."""
    return sum(liste) / len(liste)
```

### 4. Imports Conditionnels

```python
# Import conditionnel selon la plateforme
import sys

if sys.platform == 'win32':
    import winreg
else:
    import pwd  # Unix only

# Import conditionnel avec gestion d'erreur
try:
    import numpy as np
    HAS_NUMPY = True
except ImportError:
    HAS_NUMPY = False
    print("NumPy n'est pas installé, certaines fonctions seront limitées")

def fonction_avancee():
    if not HAS_NUMPY:
        raise RuntimeError("Cette fonction nécessite NumPy")
    # Utilisation de numpy
```

### 5. Éviter `from module import *`

```python
# ❌ MAUVAIS
from math import *    # Pollue le namespace
from os import *      # Conflits possibles

x = sqrt(16)  # D'où vient sqrt? math? Peu clair

# ✅ BON
import math
x = math.sqrt(16)  # Clair et explicite

# ✅ BON (si peu de fonctions)
from math import sqrt, pi, cos
x = sqrt(16)  # Clair car importé explicitement

# ✅ BON (alias)
import numpy as np  # Convention établie
x = np.sqrt(16)
```

### 6. Gestion des Arguments

```python
#!/usr/bin/python3
"""Script avec arguments bien gérés."""
import sys

def main(args):
    """Fonction principale du script."""
    if len(args) < 2:
        print("Usage: script.py <argument>")
        sys.exit(1)
    
    argument = args[1]
    # Traitement...
    return 0

if __name__ == "__main__":
    exit_code = main(sys.argv)
    sys.exit(exit_code)
```

**Bibliothèque `argparse` (recommandée)** :
```python
import argparse

def main():
    parser = argparse.ArgumentParser(description='Description du script')
    parser.add_argument('fichier', help='Fichier à traiter')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Mode verbeux')
    parser.add_argument('-n', '--nombre', type=int, default=10,
                        help='Nombre d\'itérations')
    
    args = parser.parse_args()
    
    print(f"Fichier: {args.fichier}")
    print(f"Verbose: {args.verbose}")
    print(f"Nombre: {args.nombre}")

if __name__ == "__main__":
    main()
```

---

## Tests et Exécution

### Tests des Fichiers

```bash
# 0-add.py
$ python3 0-add.py
1 + 2 = 3

# 1-calculation.py
$ python3 1-calculation.py
10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2

# 2-args.py
$ python3 2-args.py
0 arguments.

$ python3 2-args.py Hello
1 argument:
1: Hello

$ python3 2-args.py Hello World Python
3 arguments:
1: Hello
2: World
3: Python

# 3-infinite_add.py
$ python3 3-infinite_add.py
0

$ python3 3-infinite_add.py 1 2 3 4 5
15

$ python3 3-infinite_add.py 100 200 300
600

# 5-variable_load.py
$ python3 5-variable_load.py
98
```

### Tests d'Import

```bash
# Tester l'import d'un module
$ python3 -c "from add_0 import add; print(add(5, 10))"
15

# Vérifier la disponibilité des fonctions
$ python3 -c "from calculator_1 import add, sub, mul, div; print('OK')"
OK

# Tester avec arguments
$ python3 -c "import sys; sys.argv = ['script', '10', '20', '30']; exec(open('3-infinite_add.py').read())"
60
```

### Vérification de Style

```bash
# Vérifier tous les fichiers
$ pycodestyle *.py

# Vérifier les imports
$ pylint --disable=all --enable=import *.py
```

---

## Ressources

### Documentation Officielle
- [Python Modules](https://docs.python.org/3/tutorial/modules.html)
- [sys Module](https://docs.python.org/3/library/sys.html)
- [Import System](https://docs.python.org/3/reference/import.html)
- [PEP 8 - Imports](https://pep8.org/#imports)

### Tutoriels
- [Real Python - Modules and Packages](https://realpython.com/python-modules-packages/)
- [Real Python - Command Line Arguments](https://realpython.com/python-command-line-arguments/)
- [Python Module Index](https://docs.python.org/3/py-modindex.html)

### Outils
- [argparse](https://docs.python.org/3/library/argparse.html) - Arguments CLI avancés
- [importlib](https://docs.python.org/3/library/importlib.html) - Utilities d'import
- [pkgutil](https://docs.python.org/3/library/pkgutil.html) - Utilitaires de packages

---

## Résumé des Concepts

| Concept | Syntaxe | Exemple |
|---------|---------|---------|
| **Import module** | `import module` | `import math` |
| **Import fonction** | `from module import func` | `from math import sqrt` |
| **Import avec alias** | `import module as alias` | `import numpy as np` |
| **Arguments CLI** | `sys.argv` | `sys.argv[1]` |
| **Protection exécution** | `if __name__ == "__main__"` | Code exécuté si lancé directement |
| **Nombre d'arguments** | `len(sys.argv)` | `len(sys.argv) - 1` |
| **Docstring module** | `"""..."""` | Première chaîne du fichier |

---

## Conclusion

Ce projet vous a permis de maîtriser :
- ✅ Import et création de modules
- ✅ Organisation du code en fichiers séparés
- ✅ Gestion des arguments de ligne de commande
- ✅ Protection de l'exécution avec `if __name__ == "__main__"`
- ✅ Utilisation du module `sys`
- ✅ Bonnes pratiques d'import et de documentation

**Compétences acquises** :
- Créer des modules réutilisables
- Importer des fonctions et variables
- Traiter des arguments CLI
- Organiser un projet Python
- Documenter correctement son code

**Prochaines étapes recommandées** :
1. Packages Python (structures avec `__init__.py`)
2. Modules de la bibliothèque standard avancés
3. Distribution de modules (setup.py, pip)
4. Tests unitaires avec imports
5. Gestion de dépendances (requirements.txt, virtual environments)

---

**Auteur** : Projet Holberton School  
**Date** : 2026  
**Langage** : Python 3.8+
