# Holberton School - Higher Level Programming

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow?style=for-the-badge&logo=javascript&logoColor=black)
![SQL](https://img.shields.io/badge/MySQL-8.0-blue?style=for-the-badge&logo=mysql&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.0-lightgrey?style=for-the-badge&logo=flask)
![Ubuntu](https://img.shields.io/badge/Ubuntu-20.04_LTS-orange?style=for-the-badge&logo=ubuntu)

**Auteur :** [maxim880000](https://github.com/maxim880000)

---

## Qu'est-ce que ce repository ?

Ce repository regroupe **tous les projets de programmation** realises dans le cadre du cursus **Higher Level Programming** a Holberton School. Il couvre un parcours complet allant des bases de Python jusqu'au developpement web full-stack, en passant par les bases de donnees SQL et le JavaScript.

**Pourquoi "Higher Level" ?** En informatique, on distingue les langages **bas niveau** (comme le C, proche de la machine) des langages **haut niveau** (comme Python, plus proches du langage humain). Ce cursus se concentre sur ces langages haut niveau qui permettent de developper plus vite et plus facilement.

---

## Comment naviguer dans ce repository

Le repository est organise en **19 dossiers**, chacun correspondant a un module d'apprentissage. Ils sont classes ci-dessous en **4 grands themes** :

1. **Python** - Le coeur du cursus (14 modules)
2. **SQL** - Les bases de donnees (2 modules)
3. **JavaScript** - La programmation cote client (2 modules)
4. **API & Web** - Le developpement web et les APIs (1 module)

Chaque dossier contient :
- Des fichiers de code numerotes (`0-xxx`, `1-xxx`, etc.) dans l'ordre de difficulte croissante
- Des fichiers `*-main.py` ou `*-main.js` qui servent de **tests** pour verifier le code
- Un `README.md` local avec les consignes specifiques du projet

---

# THEME 1 : PYTHON

Python est un langage de programmation **interprete**, **haut niveau** et **multi-paradigme**. C'est le langage principal de ce cursus car il est lisible, polyvalent et enormement utilise dans l'industrie (web, data science, IA, automatisation).

---

## 1.1 python-hello_world

> **Objectif :** Decouvrir Python, ecrire ses premiers programmes, comprendre `print()` et les strings.

C'est le tout premier contact avec Python. On apprend a afficher du texte dans le terminal.

| Fichier | Ce qu'il fait | Concept cle |
|---------|---------------|-------------|
| `2-print.py` | Affiche une phrase avec des caracteres speciaux | La fonction `print()` et les caracteres d'echappement (`\"`, `\n`) |
| `3-print_number.py` | Affiche un nombre avec du texte autour | Les **f-strings** : `f"Le nombre est {variable}"` |
| `4-print_float.py` | Affiche un nombre decimal arrondi a 2 chiffres | Le formatage de precision : `f"{nombre:.2f}"` |
| `5-print_string.py` | Repete et decoupe une chaine de caracteres | L'operateur `*` sur les strings et le **slicing** `[debut:fin]` |
| `6-concat.py` | Colle deux morceaux de texte ensemble | La **concatenation** avec `+` et les f-strings |
| `7-edges.py` | Extrait le debut, la fin et le milieu d'un texte | Le **slicing** avec index positifs et negatifs `[-2:]` |
| `8-concat_edges.py` | Recompose un texte a partir de morceaux | Le slicing avance avec plusieurs decoupages |
| `9-easter_egg.py` | Affiche le "Zen of Python" (philosophie du langage) | Le module `this` et `import` |

**Ce qu'il faut retenir :**
- `print("texte")` affiche du texte dans le terminal
- Les **f-strings** (`f"..."`) permettent d'inserer des variables dans du texte : `f"J'ai {age} ans"`
- Le **slicing** `[debut:fin]` decoupe une chaine : `"Bonjour"[0:3]` donne `"Bon"`
- Les index negatifs comptent depuis la fin : `"Bonjour"[-4:]` donne `"jour"`

---

## 1.2 python-if_else_loops_functions

> **Objectif :** Maitriser les conditions, les boucles et ecrire ses premieres fonctions.

C'est ici qu'on commence a faire des programmes qui **prennent des decisions** et **repetent des actions**.

| Fichier | Ce qu'il fait | Concept cle |
|---------|---------------|-------------|
| `0-positive_or_negative.py` | Genere un nombre aleatoire et dit s'il est positif, negatif ou zero | `if`, `elif`, `else` et le module `random` |
| `1-last_digit.py` | Extrait le dernier chiffre d'un nombre et le classe | L'operateur **modulo** `%` (reste de la division) |
| `2-print_alphabet.py` | Affiche l'alphabet en minuscules sur une ligne | La boucle `for`, `chr()` pour convertir un code ASCII en lettre |
| `3-print_alphabt.py` | Affiche l'alphabet sans 'e' ni 'q' | Filtrage avec `if` dans une boucle |
| `4-print_hexa.py` | Affiche les nombres de 0 a 98 en decimal et hexadecimal | La conversion hexadecimale avec `hex()` |
| `5-print_comb2.py` | Affiche toutes les combinaisons de 2 chiffres (00-99) | Le formatage `{:02d}` pour afficher avec un zero devant |
| `6-print_comb3.py` | Affiche les combinaisons uniques de 2 chiffres differents | Les **boucles imbriquees** (une boucle dans une boucle) |
| `7-islower.py` | Verifie si un caractere est en minuscule | Les **fonctions** : `def ma_fonction(parametre):` |
| `8-uppercase.py` | Convertit un texte en majuscules | L'arithmetique ASCII (la difference entre 'a' et 'A' est 32) |
| `9-print_last_digit.py` | Retourne le dernier chiffre d'un nombre | `return` dans une fonction |
| `10-add.py` | Additionne deux nombres | Fonction avec deux parametres et `return` |
| `11-pow.py` | Calcule une puissance (ex: 2^3 = 8) | L'operateur `**` (puissance) |
| `12-fizzbuzz.py` | Le celebre algorithme FizzBuzz | Conditions multiples avec `%` (modulo) |

**Ce qu'il faut retenir :**
- **`if / elif / else`** : permet au programme de prendre des decisions
  ```python
  if age >= 18:
      print("Majeur")
  elif age >= 16:
      print("Presque majeur")
  else:
      print("Mineur")
  ```
- **`for i in range(10)`** : repete une action 10 fois (de 0 a 9)
- **`def ma_fonction(x, y):`** : cree une fonction reutilisable
- **`return resultat`** : renvoie une valeur depuis une fonction
- **`%` (modulo)** : donne le reste de la division. `10 % 3` donne `1` car 10 = 3*3 + **1**

---

## 1.3 python-import_modules

> **Objectif :** Comprendre comment importer et utiliser des modules (fichiers de code reutilisables).

En Python, on ne reinvente pas la roue : on **importe** du code deja ecrit.

| Fichier | Ce qu'il fait | Concept cle |
|---------|---------------|-------------|
| `0-add.py` | Importe une fonction `add` depuis un autre fichier | `from fichier import fonction` |
| `1-calculation.py` | Importe 4 fonctions mathematiques et les utilise | Import de plusieurs fonctions depuis un module |
| `2-args.py` | Affiche le nombre d'arguments passes en ligne de commande | `sys.argv` pour acceder aux arguments du terminal |
| `3-infinite_add.py` | Additionne un nombre variable d'arguments | `sys.argv[1:]` pour ignorer le nom du script |
| `5-variable_load.py` | Importe une simple variable depuis un module | Les modules peuvent contenir des variables, pas que des fonctions |

**Fichiers "helper" (modules importes) :**
- `add_0.py` : contient la fonction `add(a, b)`
- `calculator_1.py` : contient `add`, `sub`, `mul`, `div`
- `variable_load_5.py` : contient la variable `a = 98`

**Ce qu'il faut retenir :**
- `import module` : importe tout le module, on accede avec `module.fonction()`
- `from module import fonction` : importe directement la fonction
- `sys.argv` : liste des arguments passes au script (`python3 script.py arg1 arg2`)
- `if __name__ == "__main__":` : ce bloc ne s'execute que quand le fichier est lance directement (pas quand il est importe)

---

## 1.4 python-data_structures

> **Objectif :** Maitriser les listes et les tuples, les deux structures de donnees les plus fondamentales.

Une **liste** est un conteneur ordonne et modifiable. Un **tuple** est pareil mais **non modifiable** (immutable).

| Fichier | Ce qu'il fait | Concept cle |
|---------|---------------|-------------|
| `0-print_list_integer.py` | Affiche chaque element d'une liste d'entiers | Boucle `for element in liste:` |
| `1-element_at.py` | Recupere un element a un index donne | L'indexation `liste[index]` et la gestion des limites |
| `2-replace_in_list.py` | Remplace un element a un index donne | Modification en place `liste[index] = valeur` |
| `3-print_reversed_list_integer.py` | Affiche une liste a l'envers | `range(len-1, -1, -1)` pour parcourir en sens inverse |
| `4-new_in_list.py` | Cree une copie de liste avec un element modifie | `.copy()` pour ne pas modifier l'originale |
| `5-no_c.py` | Supprime tous les 'c' et 'C' d'une chaine | Construction de nouvelle chaine par filtrage |
| `6-print_matrix_integer.py` | Affiche une matrice (liste de listes) en grille | Les **listes imbriquees** (tableaux 2D) |
| `7-add_tuple.py` | Additionne deux tuples element par element | Le **tuple unpacking** et les valeurs par defaut |
| `8-multiple_returns.py` | Retourne la longueur et le premier caractere d'un string | Retourner un **tuple** depuis une fonction |
| `9-max_integer.py` | Trouve le plus grand nombre d'une liste | Algorithme de recherche du maximum |
| `10-divisible_by_2.py` | Cree une liste de booleens (divisible par 2 ou non) | Les **list comprehensions** : `[x % 2 == 0 for x in liste]` |
| `11-delete_at.py` | Supprime un element a un index donne | Le mot-cle `del` |
| `12-switch.py` | Echange les valeurs de deux variables | Le swap Python : `a, b = b, a` |

**Ce qu'il faut retenir :**
- **Liste** `[1, 2, 3]` : modifiable, ordonnee, accede par index
  - `.append(x)` ajoute a la fin, `.pop()` retire le dernier, `del liste[i]` supprime a l'index i
- **Tuple** `(1, 2, 3)` : non modifiable, utile pour des donnees fixes
- **List comprehension** : `[expression for element in liste if condition]`
  - Exemple : `[x**2 for x in range(10) if x % 2 == 0]` donne `[0, 4, 16, 36, 64]`
- Le **slicing** marche aussi sur les listes : `liste[1:4]` donne les elements d'index 1, 2, 3

---

## 1.5 python-more_data_structures

> **Objectif :** Maitriser les sets (ensembles) et les dictionnaires, et decouvrir les fonctions lambda.

| Fichier | Ce qu'il fait | Concept cle |
|---------|---------------|-------------|
| `0-square_matrix_simple.py` | Carre tous les elements d'une matrice | **Comprehension imbriquee** `[[x**2 for x in row] for row in matrix]` |
| `1-search_replace.py` | Remplace toutes les occurrences d'une valeur dans une liste | Comprehension conditionnelle |
| `2-uniq_add.py` | Additionne les elements uniques d'une liste | **`set()`** pour supprimer les doublons |
| `3-common_elements.py` | Trouve les elements communs a deux ensembles | L'operateur **`&`** (intersection de sets) |
| `4-only_diff_elements.py` | Trouve les elements presents dans un seul des deux ensembles | L'operateur **`^`** (difference symetrique) |
| `5-number_keys.py` | Compte le nombre de cles d'un dictionnaire | `len(dictionnaire)` |
| `6-print_sorted_dictionary.py` | Affiche un dictionnaire trie par cles | `sorted()` sur les cles |
| `7-update_dictionary.py` | Ajoute ou modifie une entree dans un dictionnaire | `dico[cle] = valeur` |
| `8-simple_delete.py` | Supprime une cle d'un dictionnaire | `del dico[cle]` avec verification `if cle in dico` |
| `9-multiply_by_2.py` | Cree un nouveau dictionnaire avec les valeurs x2 | **Dict comprehension** `{k: v*2 for k, v in dico.items()}` |
| `10-best_score.py` | Trouve la cle avec la plus grande valeur | `max()` avec le parametre `key` |
| `11-multiply_list_map.py` | Multiplie chaque element par un nombre avec `map()` | **`map()`** et **`lambda`** |
| `12-roman_to_int.py` | Convertit un nombre romain ("XIV") en entier (14) | Dictionnaire de correspondances et algorithme iteratif |

**Ce qu'il faut retenir :**
- **Set** `{1, 2, 3}` : pas de doublons, pas d'ordre, operations mathematiques (union `|`, intersection `&`, difference `-`)
- **Dictionnaire** `{"nom": "Alice", "age": 25}` : paires cle-valeur, acces par cle
  - `.keys()` : toutes les cles, `.values()` : toutes les valeurs, `.items()` : paires (cle, valeur)
- **Lambda** : fonction anonyme en une ligne
  ```python
  carre = lambda x: x ** 2    # equivalent a def carre(x): return x ** 2
  ```
- **`map(fonction, liste)`** : applique une fonction a chaque element

---

## 1.6 python-exceptions

> **Objectif :** Apprendre a gerer les erreurs proprement au lieu de faire planter le programme.

Quand Python rencontre une erreur, il leve une **exception**. Sans gestion, le programme s'arrete. Avec `try/except`, on peut **attraper** l'erreur et reagir.

| Fichier | Ce qu'il fait | Concept cle |
|---------|---------------|-------------|
| `0-safe_print_list.py` | Affiche les N premiers elements d'une liste (meme si N est trop grand) | `try/except IndexError` |
| `1-safe_print_integer.py` | Essaie d'afficher une valeur comme entier | `try/except (ValueError, TypeError)` |
| `2-safe_print_list_integers.py` | Affiche seulement les entiers d'une liste mixte | Filtrer par type avec les exceptions |
| `3-safe_print_division.py` | Divise deux nombres en gerant la division par zero | `try/except/finally` (finally s'execute toujours) |
| `4-list_division.py` | Divise deux listes element par element | Gestion de **plusieurs types d'erreurs** |
| `5-raise_exception.py` | Declenche volontairement une erreur TypeError | Le mot-cle **`raise`** |
| `6-raise_exception_msg.py` | Declenche une erreur avec un message personnalise | `raise NameError("message")` |

**Ce qu'il faut retenir :**
```python
try:
    resultat = 10 / 0          # Code qui peut echouer
except ZeroDivisionError:
    print("Division par zero !") # Ce qui se passe si erreur
except TypeError as e:
    print(f"Erreur de type : {e}")
finally:
    print("Ceci s'execute toujours")  # Nettoyage garanti
```
- **`try`** : le code a surveiller
- **`except TypeErreur`** : ce qu'on fait si cette erreur arrive
- **`finally`** : s'execute toujours (erreur ou pas)
- **`raise`** : declenche volontairement une erreur
- Erreurs courantes : `TypeError` (mauvais type), `ValueError` (mauvaise valeur), `IndexError` (index hors limites), `ZeroDivisionError` (division par 0)

---

## 1.7 python-classes

> **Objectif :** Decouvrir la Programmation Orientee Objet (POO) en creant une classe `Square`.

La POO permet de creer ses propres **types de donnees**. Une **classe** est un plan, un **objet** est une instance de ce plan.

| Fichier | Ce qu'il fait | Concept cle |
|---------|---------------|-------------|
| `0-square.py` | Classe vide `Square` | La syntaxe `class NomClasse:` et `pass` |
| `1-square.py` | Classe avec un constructeur qui prend une taille | `__init__(self, size)` et les attributs **prives** `__size` |
| `2-square.py` | Ajoute la validation de la taille | `isinstance()` pour verifier le type, `raise` pour les erreurs |
| `3-square.py` | Ajoute la methode `area()` qui calcule l'aire | Les **methodes d'instance** |
| `4-square.py` | Ajoute un getter et setter avec `@property` | **Encapsulation** : controler l'acces aux attributs |
| `5-square.py` | Ajoute `my_print()` qui dessine le carre avec des `#` | Methodes d'affichage |
| `6-square.py` | Ajoute un decalage (position) a l'affichage | Parametres de methode et logique d'affichage |

**Ce qu'il faut retenir :**
```python
class Square:
    def __init__(self, size=0):        # Constructeur
        self.__size = size              # Attribut prive

    @property
    def size(self):                     # Getter
        return self.__size

    @size.setter
    def size(self, value):              # Setter avec validation
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):                     # Methode
        return self.__size ** 2

# Utilisation :
mon_carre = Square(5)      # Cree un carre de taille 5
print(mon_carre.area())     # Affiche 25
mon_carre.size = 10         # Modifie la taille (passe par le setter)
```
- **`self`** : reference a l'objet lui-meme (comme `this` en JS)
- **`__init__`** : methode speciale appelee automatiquement a la creation
- **`@property`** : transforme une methode en attribut accessible avec la syntaxe `objet.attribut`
- **Attribut prive** `__nom` : pas directement accessible depuis l'exterieur

---

## 1.8 python-more_classes

> **Objectif :** Approfondir la POO avec les methodes magiques, les methodes de classe et les methodes statiques.

On construit ici une classe `Rectangle` complete, etape par etape.

| Fichier | Ce qu'il fait | Concept cle |
|---------|---------------|-------------|
| `0-rectangle.py` | Classe vide | Point de depart |
| `1-rectangle.py` | Proprietes width et height avec validation | Getters/setters pour deux attributs |
| `2-rectangle.py` | Methodes `area()` et `perimeter()` | Calculs sur les attributs |
| `3-rectangle.py` | `__str__()` et `__repr__()` | Representation textuelle de l'objet |
| `4-rectangle.py` | `__del__()` : message quand l'objet est supprime | Le **destructeur** |
| `5-rectangle.py` | Compteur d'instances (variable de classe) | **Variable de classe** vs variable d'instance |
| `6-rectangle.py` | Symbole d'affichage personnalisable | Variable de classe modifiable |
| `7-rectangle.py` | `bigger_or_equal()` compare deux rectangles | **`@staticmethod`** : methode sans `self` |
| `8-rectangle.py` | `square(cls, size)` cree un carre | **`@classmethod`** : methode qui recoit la classe |
| `9-rectangle.py` | Tri de rectangles par aire | Logique de comparaison avancee |

**Ce qu'il faut retenir :**
- **`__str__(self)`** : ce qui s'affiche avec `print(objet)` - pour les humains
- **`__repr__(self)`** : representation technique - pour les developpeurs, permet `eval(repr(objet))`
- **`__del__(self)`** : appele quand `del objet` est execute
- **Variable de classe** : partagee entre toutes les instances (`Rectangle.nb_instances`)
- **Variable d'instance** : propre a chaque objet (`self.width`)
- **`@staticmethod`** : fonction dans la classe mais qui n'a pas besoin de `self` ni `cls`
- **`@classmethod`** : recoit la classe en parametre (`cls`), utile pour des constructeurs alternatifs

---

## 1.9 python-test_driven_development

> **Objectif :** Apprendre a ecrire des tests AVANT le code (TDD) et utiliser `doctest`.

Le TDD (Test-Driven Development) est une methode ou on ecrit d'abord le test qui echoue, puis on code la solution.

| Fichier | Ce qu'il fait | Concept cle |
|---------|---------------|-------------|
| `0-add_integer.py` | Additionne deux nombres avec validation de type | Docstrings avec exemples testables |
| `2-matrix_divided.py` | Divise tous les elements d'une matrice | Validation complexe (type, taille, division par zero) |
| `3-say_my_name.py` | Affiche un nom formate | Validation de strings |
| `4-print_square.py` | Dessine un carre de `#` | Validation de taille |
| `5-text_indentation.py` | Coupe le texte apres `.`, `?` et `:` | Traitement de texte caractere par caractere |

**Fichiers de tests dans `tests/` :**
| Fichier | Ce qu'il teste |
|---------|----------------|
| `tests/0-add_integer.txt` | Cas normaux, floats, erreurs de type |
| `tests/2-matrix_divided.txt` | Matrice valide, division par zero, types invalides |
| `tests/3-say_my_name.txt` | Noms valides et invalides |
| `tests/4-print_square.txt` | Carres de differentes tailles |
| `tests/5-text_indentation.txt` | Textes avec differents separateurs |
| `tests/6-max_integer_test.py` | Test unitaire avec `unittest` |

**Ce qu'il faut retenir :**
```python
def add_integer(a, b=98):
    """Additionne deux entiers.

    >>> add_integer(1, 2)
    3
    >>> add_integer(100, -2)
    98
    >>> add_integer("hello", 3)
    Traceback (most recent call last):
    TypeError: a must be an integer
    """
```
Pour lancer les tests :
```bash
python3 -m doctest tests/0-add_integer.txt     # Lance les doctests
python3 -m unittest tests/6-max_integer_test    # Lance les tests unittest
```

---

## 1.10 python-inheritance

> **Objectif :** Comprendre l'heritage entre classes : une classe enfant herite des attributs et methodes de sa classe parente.

| Fichier | Ce qu'il fait | Concept cle |
|---------|---------------|-------------|
| `0-lookup.py` | Liste tous les attributs/methodes d'un objet | `dir()` pour l'introspection |
| `1-my_list.py` | Liste avec methode `print_sorted()` | **Heritage** de types natifs (`class MyList(list)`) |
| `2-is_same_class.py` | Verifie si un objet est exactement d'un type | `type(obj) is ClasseName` |
| `3-is_kind_of_class.py` | Verifie si un objet est d'un type ou d'un type enfant | `isinstance(obj, Classe)` |
| `4-inherits_from.py` | Verifie si un objet herite d'une classe (sans etre directement cette classe) | Difference entre `type()` et `isinstance()` |
| `5-base_geometry.py` | Classe de base vide | Fondation pour l'heritage |
| `6-base_geometry.py` | Methode `area()` qui leve une erreur | `raise Exception("area() is not implemented")` |
| `7-base_geometry.py` | Ajout de `integer_validator()` | Methode utilitaire de validation |
| `8-rectangle.py` | Rectangle heritant de BaseGeometry | `super().__init__()` pour appeler le constructeur parent |
| `9-rectangle.py` | Rectangle avec `area()` et `__str__()` | **Surcharge de methode** (override) |
| `10-square.py` | Square heritant de Rectangle | **Heritage multi-niveaux** (Square -> Rectangle -> BaseGeometry) |
| `11-square.py` | Square avec `__str__()` personnalise | Representation specifique dans la chaine d'heritage |

**Ce qu'il faut retenir :**
```python
class Animal:                       # Classe parente
    def parler(self):
        raise NotImplementedError

class Chien(Animal):                # Classe enfant (herite de Animal)
    def parler(self):               # Surcharge la methode du parent
        return "Woof!"

class Caniche(Chien):               # Heritage multi-niveaux
    pass                            # Herite de parler() de Chien

isinstance(Caniche(), Animal)  # True - un Caniche EST un Animal
type(Caniche()) is Animal      # False - son type exact est Caniche
```
- **`class Enfant(Parent):`** : la classe Enfant herite de tout ce que Parent possede
- **`super().__init__()`** : appelle le constructeur de la classe parente
- **Surcharge** : redefinir une methode heritee pour changer son comportement

---

## 1.11 python-abc

> **Objectif :** Maitriser les Classes Abstraites (ABC), le duck typing, les iterateurs et les mixins.

Ce module aborde des concepts avances de la POO.

| Fichier | Ce qu'il fait | Concept cle |
|---------|---------------|-------------|
| `task_00_abc.py` | Classe abstraite `Animal` avec `Dog` et `Cat` | `ABC` et `@abstractmethod` : obliger les classes enfants a implementer des methodes |
| `task_01_duck_typing.py` | `Shape` abstraite avec `Circle` et `Rectangle` | **Duck typing** : "si ca marche comme un canard, c'est un canard" |
| `task_02_verboselist.py` | Liste qui affiche un message a chaque modification | Surcharge de `append()`, `extend()`, `remove()`, `pop()` |
| `task_03_countediterator.py` | Iterateur qui compte les elements consommes | Le **protocole iterateur** : `__iter__()` et `__next__()` |
| `task_04_flyingfish.py` | Poisson volant qui nage ET vole | Heritage simple avec methodes multiples |
| `task_05_dragon.py` | Dragon avec plusieurs capacites via mixins | **Pattern Mixin** : heritage multiple pour ajouter des capacites |

**Ce qu'il faut retenir :**
```python
from abc import ABC, abstractmethod

class Forme(ABC):                    # Classe abstraite (ne peut pas etre instanciee)
    @abstractmethod
    def aire(self):                  # DOIT etre implementee par les enfants
        pass

class Cercle(Forme):
    def __init__(self, rayon):
        self.rayon = rayon
    def aire(self):                  # Implementation obligatoire
        return 3.14 * self.rayon ** 2

# Forme()     # ERREUR : ne peut pas creer une instance de classe abstraite
# Cercle(5)   # OK : Cercle a implemente aire()
```
- **ABC** : force les classes enfants a implementer certaines methodes
- **Mixin** : petite classe avec une fonctionnalite specifique qu'on ajoute par heritage multiple

---

## 1.12 python-serialization

> **Objectif :** Convertir des donnees Python en differents formats pour les sauvegarder ou les transmettre.

La **serialisation** c'est transformer des donnees en memoire en un format stockable (fichier, reseau).

| Fichier | Ce qu'il fait | Concept cle |
|---------|---------------|-------------|
| `task_00_basic_serialization.py` | Sauvegarde/charge un dictionnaire en JSON | `json.dump()` / `json.load()` |
| `task_01_pickle.py` | Sauvegarde/charge un objet Python en binaire | `pickle` : serialisation binaire Python |
| `task_02_csv.py` | Convertit un fichier CSV en JSON | `csv.DictReader` pour lire du CSV structuré |
| `task_03_xml.py` | Sauvegarde/charge un dictionnaire en XML | `xml.etree.ElementTree` |

**Ce qu'il faut retenir :**
| Format | Humainement lisible | Utilisation typique | Module Python |
|--------|:--:|---------|---------|
| **JSON** | Oui | APIs web, configuration | `json` |
| **CSV** | Oui | Tableaux, donnees tabulaires | `csv` |
| **XML** | Oui | Configurations, echanges entre systemes | `xml.etree.ElementTree` |
| **Pickle** | Non (binaire) | Sauvegarde d'objets Python complexes | `pickle` |

---

## 1.13 python-input_output

> **Objectif :** Lire et ecrire des fichiers, et manipuler le format JSON.

| Fichier | Ce qu'il fait | Concept cle |
|---------|---------------|-------------|
| `0-read_file.py` | Lit et affiche le contenu d'un fichier | `with open(fichier, "r") as f:` |
| `1-write_file.py` | Ecrit du texte dans un fichier (ecrase le contenu) | Mode `"w"` (write) |
| `2-append_write.py` | Ajoute du texte a la fin d'un fichier | Mode `"a"` (append) |
| `3-to_json_string.py` | Convertit un objet Python en chaine JSON | `json.dumps()` |
| `4-from_json_string.py` | Convertit une chaine JSON en objet Python | `json.loads()` |
| `5-save_to_json_file.py` | Sauvegarde un objet dans un fichier JSON | `json.dump(objet, fichier)` |
| `6-load_from_json_file.py` | Charge un objet depuis un fichier JSON | `json.load(fichier)` |
| `7-add_item.py` | Ajoute des arguments a une liste sauvegardee en JSON | Combinaison I/O + JSON + `sys.argv` |
| `8-class_to_json.py` | Convertit un objet en dictionnaire | `objet.__dict__` |
| `9-student.py` | Classe Student avec methode `to_json()` | Serialisation d'objet personnalisee |
| `10-student.py` | Student avec methode de classe `from_json()` | Deserialisation personnalisee |
| `11-student.py` | `to_json()` avec filtrage d'attributs | Serialisation selective |

**Ce qu'il faut retenir :**
```python
# LIRE un fichier
with open("fichier.txt", "r") as f:
    contenu = f.read()

# ECRIRE dans un fichier (ecrase)
with open("fichier.txt", "w") as f:
    f.write("Nouveau contenu")

# AJOUTER a un fichier
with open("fichier.txt", "a") as f:
    f.write("Texte ajoute a la fin")
```
- **`with`** : garantit que le fichier est ferme automatiquement
- **Modes** : `"r"` lecture, `"w"` ecriture (ecrase), `"a"` ajout a la fin
- **JSON** : format texte universel pour echanger des donnees entre programmes

---

## 1.14 python-everything_is_object

> **Objectif :** Comprendre en profondeur comment Python gere les objets en memoire.

Ce module est un **quiz** : chaque fichier contient une seule reponse a une question sur le comportement de Python.

**Concepts testes :**
- La difference entre `==` (egalite de valeur) et `is` (meme objet en memoire)
- Les objets **mutables** (listes, dicts) vs **immutables** (int, str, tuple)
- L'aliasing : quand deux variables pointent vers le meme objet
- Le passage par reference vs par valeur

**Point cle :** En Python, **tout est un objet**. Quand on ecrit `a = [1, 2, 3]` puis `b = a`, les deux variables pointent vers **la meme liste**. Modifier `b` modifie aussi `a`. Pour creer une copie independante : `b = a.copy()` ou `b = list(a)`.

---

## 1.15 python-object_relational_mapping

> **Objectif :** Connecter Python a une base de donnees MySQL, d'abord avec des requetes SQL brutes, puis avec un ORM (SQLAlchemy).

| Fichier | Ce qu'il fait | Concept cle |
|---------|---------------|-------------|
| `0-select_states.py` | Liste tous les etats depuis MySQL | Connexion avec `MySQLdb`, `cursor.execute()` |
| `1-filter_states.py` | Filtre les etats commencant par 'N' | Clause `WHERE` en SQL |
| `2-my_filter_states.py` | Filtre avec un input utilisateur (VULNERABLE) | **Injection SQL** : ce qu'il ne faut PAS faire |
| `3-my_safe_filter_states.py` | Filtre avec requete parametree (SECURISE) | `cursor.execute("... WHERE name = %s", (input,))` |
| `4-cities_by_state.py` | Liste les villes avec leur etat (JOIN) | `JOIN` SQL pour relier deux tables |
| `5-filter_cities.py` | Filtre les villes d'un etat donne | Requete parametree avec JOIN |
| `model_state.py` | Definition du modele State avec SQLAlchemy | `declarative_base()`, `Column`, `Integer`, `String` |
| `model_city.py` | Definition du modele City avec cle etrangere | `ForeignKey`, relation entre tables |
| `7-model_state_fetch_all.py` | Liste tous les etats via ORM | `session.query(State).all()` |
| `8-model_state_fetch_first.py` | Recupere le premier etat | `.first()` |
| `9-model_state_filter_a.py` | Filtre les etats contenant 'a' | `.filter(State.name.like('%a%'))` |
| `10-model_state_my_get.py` | Cherche un etat par nom | `.filter(State.name == nom)` |
| `11-model_state_insert.py` | Cree un nouvel etat | `session.add()` + `session.commit()` |
| `12-model_state_update_id_2.py` | Met a jour un etat | Modification d'attribut + `commit()` |
| `13-model_state_delete_a.py` | Supprime des etats | `session.delete()` + `commit()` |
| `14-model_city_fetch_by_state.py` | Liste les villes avec leur etat via ORM | Relations ORM et jointures |

**Ce qu'il faut retenir :**
- **MySQLdb** : execute du SQL brut. Simple mais risque d'injection SQL.
- **SQLAlchemy ORM** : on manipule des objets Python au lieu d'ecrire du SQL. Plus sur, plus maintenable.
- **JAMAIS** de formatage de string dans les requetes SQL : `f"WHERE name = '{input}'"` est **DANGEREUX**
- **TOUJOURS** utiliser des requetes parametrees : `cursor.execute("WHERE name = %s", (input,))`

---

# THEME 2 : SQL

SQL (Structured Query Language) est le langage standard pour interagir avec les **bases de donnees relationnelles**. Une base de donnees stocke des informations de maniere structuree dans des **tables** (comme des tableaux Excel).

---

## 2.1 SQL_introduction

> **Objectif :** Maitriser les commandes SQL de base : creer des bases, des tables, et manipuler des donnees.

| Fichier | Ce qu'il fait | Concept cle |
|---------|---------------|-------------|
| `0-list_databases.sql` | Affiche toutes les bases de donnees | `SHOW DATABASES;` |
| `1-create_database_if_missing.sql` | Cree une base seulement si elle n'existe pas | `CREATE DATABASE IF NOT EXISTS nom;` |
| `2-remove_database.sql` | Supprime une base de donnees | `DROP DATABASE IF EXISTS nom;` |
| `3-list_tables.sql` | Affiche toutes les tables d'une base | `SHOW TABLES;` |
| `4-first_table.sql` | Cree une table avec colonnes id et name | `CREATE TABLE` avec types `INT` et `VARCHAR` |
| `5-full_table.sql` | Affiche la structure complete d'une table | `SHOW CREATE TABLE nom;` |
| `6-list_values.sql` | Affiche tout le contenu d'une table | `SELECT * FROM table;` |
| `7-insert_value.sql` | Insere une ligne dans une table | `INSERT INTO table (col1, col2) VALUES (val1, val2);` |
| `8-count_89.sql` | Compte les lignes correspondant a un critere | `SELECT COUNT(*) FROM table WHERE condition;` |
| `9-full_creation.sql` | Cree une table avec id, name et score | `CREATE TABLE` avec plusieurs colonnes |
| `10-top_score.sql` | Affiche les scores tries du plus grand au plus petit | `ORDER BY score DESC` |
| `11-best_score.sql` | Affiche les scores >= 10 | `WHERE score >= 10` |
| `12-no_cheating.sql` | Met a jour le score d'un enregistrement | `UPDATE table SET colonne = valeur WHERE condition;` |
| `13-change_class.sql` | Supprime les enregistrements avec score <= 5 | `DELETE FROM table WHERE condition;` |
| `14-average.sql` | Calcule la moyenne des scores | `SELECT AVG(score) FROM table;` |
| `15-groups.sql` | Compte les enregistrements par score | `GROUP BY score` avec `COUNT(*)` |
| `16-no_link.sql` | Affiche les lignes ou le nom n'est pas vide | `WHERE name IS NOT NULL` |

**Ce qu'il faut retenir :**
```sql
-- CREER
CREATE TABLE eleves (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    note INT DEFAULT 0
);

-- LIRE
SELECT nom, note FROM eleves WHERE note >= 10 ORDER BY note DESC;

-- INSERER
INSERT INTO eleves (nom, note) VALUES ('Alice', 18);

-- MODIFIER
UPDATE eleves SET note = 15 WHERE nom = 'Alice';

-- SUPPRIMER
DELETE FROM eleves WHERE note < 5;

-- AGGREGER
SELECT AVG(note) FROM eleves;                    -- Moyenne
SELECT note, COUNT(*) FROM eleves GROUP BY note; -- Compter par groupe
```
On appelle ca le **CRUD** : Create, Read, Update, Delete.

---

## 2.2 SQL_more_queries

> **Objectif :** Gerer les utilisateurs, les contraintes, les relations entre tables et les jointures.

| Fichier | Ce qu'il fait | Concept cle |
|---------|---------------|-------------|
| `0-privileges.sql` | Affiche les privileges d'un utilisateur | `SHOW GRANTS FOR 'user'@'host';` |
| `1-create_user.sql` | Cree un utilisateur avec tous les droits | `CREATE USER` + `GRANT ALL PRIVILEGES` |
| `2-create_read_user.sql` | Cree un utilisateur en lecture seule | `GRANT SELECT` sur une base specifique |
| `3-force_name.sql` | Table avec contrainte NOT NULL | Empecher les valeurs vides |
| `4-never_empty.sql` | Table avec valeur par defaut | `DEFAULT "valeur"` |
| `5-unique_id.sql` | Table avec contrainte d'unicite | `UNIQUE` : pas de doublons |
| `6-states.sql` | Cree la base et la table states | `AUTO_INCREMENT` et `PRIMARY KEY` |
| `7-cities.sql` | Table cities avec cle etrangere vers states | `FOREIGN KEY (state_id) REFERENCES states(id)` |
| `8-cities_of_california_subquery.sql` | Villes de Californie avec sous-requete | `WHERE state_id = (SELECT id FROM states WHERE ...)` |
| `9-cities_by_state_join.sql` | Villes avec nom d'etat via JOIN | `SELECT ... FROM cities JOIN states ON cities.state_id = states.id` |
| `10-genre_id_by_show.sql` | Genres d'une emission (JOIN) | JOIN entre tables de relation |
| `11-genre_id_all_shows.sql` | Toutes les emissions avec ou sans genre | **`LEFT JOIN`** : garde toutes les lignes de gauche |
| `12-no_genre.sql` | Emissions sans genre | `LEFT JOIN ... WHERE genre IS NULL` |
| `13-count_shows_by_genre.sql` | Nombre d'emissions par genre | `GROUP BY` avec `COUNT()` |
| `14-my_genres.sql` | Genres d'une emission specifique | JOINs multiples (3 tables) |
| `15-comedy_only.sql` | Emissions de comedie uniquement | Filtrage avec JOIN et WHERE |
| `16-shows_by_genre.sql` | Emissions groupees par genre | JOIN + GROUP BY + ORDER BY |

**Ce qu'il faut retenir :**
```sql
-- CLE ETRANGERE : relie deux tables
CREATE TABLE cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL,
    state_id INT NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)  -- Lien vers states
);

-- INNER JOIN : seulement les lignes qui matchent dans les deux tables
SELECT cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id;

-- LEFT JOIN : toutes les lignes de gauche, meme sans correspondance
SELECT shows.title, genres.name
FROM shows
LEFT JOIN genres ON shows.genre_id = genres.id;
-- Les shows sans genre auront NULL dans genres.name

-- SOUS-REQUETE : une requete dans une requete
SELECT name FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California');
```

---

# THEME 3 : JAVASCRIPT

JavaScript est le langage du web. Il s'execute dans le navigateur (cote client) et permet de rendre les pages web **interactives**.

---

## 3.1 javascript-warm_up

> **Objectif :** Apprendre les bases de JavaScript : variables, conditions, boucles, fonctions.

| Fichier | Ce qu'il fait | Concept cle |
|---------|---------------|-------------|
| `0-javascript_is_amazing.js` | Affiche un texte avec `console.log` | `const` pour declarer une constante |
| `1-multi_languages.js` | Affiche plusieurs lignes | Plusieurs `console.log()` |
| `2-arguments.js` | Verifie le nombre d'arguments en ligne de commande | `process.argv` (equivalent de `sys.argv` en Python) |
| `3-value_argument.js` | Affiche le premier argument ou "No argument" | Conditions avec `if/else` et `undefined` |
| `4-concat.js` | Concatene deux arguments avec un espace | `+` pour concatener des strings |
| `5-to_integer.js` | Convertit un argument en entier | `parseInt()` et `isNaN()` |
| `6-multi_languages_loop.js` | Affiche des lignes avec une boucle `for` | Boucle `for (let i = 0; i < n; i++)` |
| `7-multi_c.js` | Affiche "C is fun" N fois | Boucle avec argument en parametre |
| `8-square.js` | Dessine un carre de `X` | Boucles imbriquees |
| `9-add.js` | Fonction qui additionne deux nombres | `function add(a, b) { return a + b; }` |
| `10-factorial.js` | Calcule la factorielle (recursivite) | Une fonction qui **s'appelle elle-meme** |
| `11-second_biggest.js` | Trouve le 2e plus grand nombre | Tri de tableau et acces par index |
| `12-object.js` | Cree et modifie un objet | Objets `{ cle: valeur }` |
| `13-add.js` | Export d'une fonction dans un module | `module.exports` pour rendre une fonction importable |

**Ce qu'il faut retenir :**
```javascript
// Variables
const PI = 3.14;          // Constante (ne peut pas changer)
let age = 25;             // Variable (peut changer)

// Conditions
if (age >= 18) {
    console.log("Majeur");
} else {
    console.log("Mineur");
}

// Boucle
for (let i = 0; i < 5; i++) {
    console.log(i);        // Affiche 0, 1, 2, 3, 4
}

// Fonction
function add(a, b) {
    return a + b;
}

// Recursivite
function factorielle(n) {
    if (n <= 1) return 1;
    return n * factorielle(n - 1);  // S'appelle elle-meme
}
```

**Differences cles Python vs JavaScript :**
| Concept | Python | JavaScript |
|---------|--------|-----------|
| Afficher | `print()` | `console.log()` |
| Variable | `x = 5` | `let x = 5;` |
| Constante | `X = 5` (convention) | `const X = 5;` |
| Bloc de code | Indentation | Accolades `{ }` |
| Fin de ligne | Rien | `;` (optionnel mais recommande) |
| Arguments CLI | `sys.argv` | `process.argv` |

---

## 3.2 javascript-dom_manipulation

> **Objectif :** Manipuler le contenu d'une page web avec JavaScript (le DOM).

Le **DOM** (Document Object Model) est la representation de la page HTML en memoire. JavaScript peut le modifier pour changer ce que l'utilisateur voit.

| Fichiers | Ce qu'ils font | Concept cle |
|----------|---------------|-------------|
| `0-script.js` + `0-main.html` | Change la couleur du titre en rouge | `document.querySelector()` et `element.style` |
| `1-script.js` + `1-main.html` | Change la couleur au clic | **Evenements** : `element.addEventListener('click', fonction)` |
| `2-script.js` + `2-main.html` | Cree des elements HTML dynamiquement | `document.createElement()` et `element.appendChild()` |
| `3-script.js` + `3-main.html` | Alterne entre deux classes CSS | `element.classList.add()`, `.remove()`, `.contains()` |
| `4-script.js` + `4-main.html` | Ajoute/supprime des elements du DOM | `element.removeChild()` |
| `5-script.js` + `5-main.html` | Charge des donnees depuis une API | **`fetch()`** : requetes HTTP asynchrones |
| `6-script.js` + `6-main.html` | Gere une liste dynamique | Manipulation de listes dans le DOM |
| `7-script.js` + `7-main.html` | Recherche et filtre des elements | Evenements de saisie et filtrage |
| `8-script.js` + `8-main.html` | Interactions multiples et complexes | Combinaison de tous les concepts |

**Ce qu'il faut retenir :**
```javascript
// SELECTIONNER un element
const titre = document.querySelector('h1');          // Par balise
const bouton = document.querySelector('#mon-id');    // Par ID
const items = document.querySelectorAll('.classe');   // Tous les elements avec cette classe

// MODIFIER un element
titre.textContent = 'Nouveau texte';                 // Changer le texte
titre.style.color = 'red';                           // Changer le style
titre.classList.add('active');                        // Ajouter une classe CSS

// CREER un element
const nouveau = document.createElement('li');
nouveau.textContent = 'Nouvel item';
document.querySelector('ul').appendChild(nouveau);

// ECOUTER un evenement
bouton.addEventListener('click', function() {
    alert('Bouton clique !');
});

// CHARGER des donnees depuis une API
fetch('https://api.exemple.com/donnees')
    .then(response => response.json())
    .then(data => {
        console.log(data);
    });
```

---

# THEME 4 : API & WEB

Les **APIs** (Application Programming Interfaces) permettent a des programmes de communiquer entre eux. Le **developpement web cote serveur** genere les pages HTML envoyees au navigateur.

---

## 4.1 restful-api

> **Objectif :** Comprendre les APIs REST, consommer des APIs avec Python, et creer sa propre API avec Flask.

| Fichier | Ce qu'il fait | Concept cle |
|---------|---------------|-------------|
| Fichiers de consommation d'API | Envoient des requetes HTTP a des APIs externes | Le module `requests` : `requests.get()`, `requests.post()` |
| Fichiers de creation d'API Flask | Creent des endpoints qui renvoient du JSON | Decorateur `@app.route()`, `jsonify()` |
| Fichiers de serialisation API | Convertissent des objets en reponses JSON | Serialisation pour API |

**Ce qu'il faut retenir :**

**Les methodes HTTP (verbes REST) :**
| Methode | Action | Exemple |
|---------|--------|---------|
| `GET` | Lire des donnees | Afficher la liste des utilisateurs |
| `POST` | Creer une donnee | Ajouter un nouvel utilisateur |
| `PUT` | Modifier entierement | Remplacer toutes les infos d'un utilisateur |
| `DELETE` | Supprimer | Supprimer un utilisateur |

```python
# CONSOMMER une API (client)
import requests

response = requests.get("https://api.exemple.com/users")
data = response.json()  # Convertit la reponse JSON en dictionnaire Python
print(data)

# CREER une API (serveur)
from flask import Flask, jsonify, request

app = Flask(__name__)

users = [{"id": 1, "name": "Alice"}]

@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/api/users', methods=['POST'])
def create_user():
    new_user = request.get_json()
    users.append(new_user)
    return jsonify(new_user), 201

if __name__ == '__main__':
    app.run(debug=True)
```

---

## 4.2 python-server_side_rendering

> **Objectif :** Generer des pages HTML cote serveur avec Flask et le moteur de templates Jinja2.

| Fichier | Ce qu'il fait | Concept cle |
|---------|---------------|-------------|
| `task_00_intro.py` | Genere des fichiers a partir d'un template texte | Remplacement de variables dans un template |
| `task_01_jinja.py` | App Flask avec templates HTML | `render_template()` et fichiers `.html` dans `templates/` |
| `task_02_logic.py` | Charge des donnees JSON et les passe au template | Variables Jinja2 `{{ variable }}` et boucles `{% for %}` |
| `task_03_files.py` | Charge des donnees depuis JSON ou CSV selon un parametre | `request.args.get()` pour les parametres d'URL |
| `task_04_db.py` | Charge des donnees depuis une base SQLite | Connexion SQLite + templates |

**Templates (dossier `templates/`) :**
| Fichier | Role |
|---------|------|
| `header.html` | Navigation partagee (incluse dans les autres pages) |
| `footer.html` | Pied de page partage |
| `index.html` | Page d'accueil |
| `about.html` | Page "A propos" |
| `contact.html` | Page de contact |
| `items.html` | Liste d'elements avec boucle et conditions |
| `product_display.html` | Tableau de produits avec style |

**Ce qu'il faut retenir :**
```python
# Flask : le serveur web
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def accueil():
    produits = [{"nom": "Laptop", "prix": 999}, {"nom": "Phone", "prix": 699}]
    return render_template('index.html', produits=produits)
```

```html
<!-- templates/index.html : le template Jinja2 -->
{% include 'header.html' %}

<h1>Nos produits</h1>

{% for produit in produits %}
    <div>
        <h2>{{ produit.nom }}</h2>
        <p>Prix : {{ produit.prix }} EUR</p>
        {% if produit.prix > 900 %}
            <span>Premium</span>
        {% endif %}
    </div>
{% endfor %}

{% include 'footer.html' %}
```
- **`{{ variable }}`** : affiche la valeur d'une variable
- **`{% for ... %}`** : boucle dans le template
- **`{% if ... %}`** : condition dans le template
- **`{% include 'fichier.html' %}`** : insere un autre template (reutilisation)

---

# Recapitulatif : Progression d'apprentissage

```
SEMAINES 1-2     Python basics (hello world, if/else, boucles, fonctions)
    |
SEMAINES 3-4     Structures de donnees (listes, tuples, dicts, sets)
    |
SEMAINES 5-6     Modules, imports, exceptions
    |
SEMAINES 7-10    POO (classes, heritage, ABC, methodes magiques)
    |
SEMAINES 11-12   Fichiers, JSON, serialisation, TDD
    |
SEMAINES 13-14   SQL (bases, tables, CRUD, jointures)
    |
SEMAINES 15-16   Python + SQL (MySQLdb, SQLAlchemy ORM)
    |
SEMAINES 17-18   JavaScript (bases, DOM, manipulation web)
    |
SEMAINES 19-20   API REST, Flask, templates Jinja2, SSR
```

---

# Requirements techniques

| Critere | Specification |
|---------|---------------|
| **OS** | Ubuntu 20.04 LTS |
| **Python** | 3.8+ |
| **JavaScript** | Node.js (ES6) |
| **SQL** | MySQL 8.0 |
| **Style Python** | pycodestyle 2.7.* |
| **Shebang Python** | `#!/usr/bin/python3` |
| **Shebang JS** | `#!/usr/bin/node` |
| **Editeurs** | vi, vim, emacs |

---

# Comment utiliser ce repository

```bash
# 1. Cloner le repository
git clone https://github.com/maxim880000/holbertonschool-higher_level_programming.git
cd holbertonschool-higher_level_programming

# 2. Naviguer vers un projet
cd python-hello_world

# 3. Rendre un fichier executable
chmod +x 2-print.py

# 4. Executer
./2-print.py
# ou
python3 2-print.py

# 5. Pour les fichiers SQL, utiliser MySQL
mysql -u root -p < SQL_introduction/0-list_databases.sql

# 6. Pour JavaScript
node javascript-warm_up/0-javascript_is_amazing.js

# 7. Pour Flask (API et SSR)
pip install flask
python3 python-server_side_rendering/task_01_jinja.py
# Puis ouvrir http://localhost:5000 dans le navigateur
```

---

# Ressources recommandees

**Python :**
- [Documentation officielle Python](https://docs.python.org/3/)
- [PEP 8 - Guide de style](https://peps.python.org/pep-0008/)
- [Real Python](https://realpython.com/) - Tutoriels de qualite

**SQL :**
- [SQLBolt](https://sqlbolt.com/) - Exercices interactifs SQL
- [W3Schools SQL](https://www.w3schools.com/sql/) - Reference rapide

**JavaScript :**
- [MDN Web Docs](https://developer.mozilla.org/fr/docs/Web/JavaScript) - La reference
- [javascript.info](https://javascript.info/) - Cours complet moderne

**Flask & APIs :**
- [Documentation Flask](https://flask.palletsprojects.com/)
- [HTTP Status Codes](https://httpstatuses.com/) - Comprendre les codes de reponse

---

*Ce repository fait partie du cursus Higher Level Programming de Holberton School.*
