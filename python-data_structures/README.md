# Python - Data Structures: Lists, Tuples

## Description
Ce projet explore en profondeur les structures de données fondamentales en Python : les listes (lists) et les tuples. Vous apprendrez à manipuler ces structures, à comprendre leurs différences, et à maîtriser les opérations courantes pour gérer efficacement les données dans vos programmes Python.

## Objectifs d'apprentissage
À la fin de ce projet, vous serez capable de :
- Comprendre ce que sont les listes et comment les utiliser
- Différencier les listes des tuples et savoir quand utiliser chacun
- Utiliser les méthodes courantes des listes
- Utiliser les listes comme des piles et des files
- Comprendre les list comprehensions
- Utiliser les tuples et le packing/unpacking
- Comprendre la séquence et le slicing

## Concepts clés

### Les Listes (Lists)
Les listes sont des collections ordonnées et modifiables qui peuvent contenir des éléments de différents types.

**Caractéristiques :**
- Modifiables (mutables)
- Ordonnées (maintiennent l'ordre d'insertion)
- Indexées (accès par position)
- Permettent les doublons

**Syntaxe de base :**
```python
ma_liste = [1, 2, 3, 4, 5]
liste_vide = []
liste_mixte = [1, "texte", 3.14, True]
```

### Les Tuples
Les tuples sont des collections ordonnées et **non modifiables** (immutables).

**Caractéristiques :**
- Non modifiables (immutables)
- Ordonnées
- Indexées
- Permettent les doublons
- Plus rapides que les listes

**Syntaxe de base :**
```python
mon_tuple = (1, 2, 3)
tuple_simple = (5,)  # Virgule nécessaire pour un seul élément
```

## Fichiers du projet

### 0-print_list_integer.py
**Objectif :** Afficher tous les entiers d'une liste, un par ligne.

**Code :**
```python
#!/usr/bin/python3
# Définition de la fonction qui affiche tous les entiers d'une liste
def print_list_integer(my_list=[]):
    # Boucle pour parcourir chaque élément de la liste
    for i in my_list:
        # Affiche l'entier avec le format {:d}
        print("{:d}".format(i))
```

**Notions utilisées :**
- **Boucle for** : Permet de parcourir chaque élément de la liste
- **str.format()** : Méthode de formatage des chaînes de caractères
- **{:d}** : Format specifier pour les entiers décimaux
- **Paramètre par défaut** : `my_list=[]` définit une liste vide comme valeur par défaut

**Explication détaillée :**
1. La fonction accepte une liste en paramètre
2. La boucle `for` itère sur chaque élément
3. `print("{:d}".format(i))` affiche l'entier avec le format décimal
4. Le format `:d` garantit que seuls les entiers sont acceptés

**Exemple d'utilisation :**
```python
my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)
# Sortie :
# 1
# 2
# 3
# 4
# 5
```

---

### 1-element_at.py
**Objectif :** Récupérer un élément d'une liste à un index donné de manière sécurisée.

**Code :**
```python
#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
```

**Notions utilisées :**
- **Indexation** : Accès aux éléments par position (`my_list[idx]`)
- **len()** : Fonction qui retourne la longueur d'une liste
- **Conditions if** : Vérification de la validité de l'index
- **return None** : Retour d'une valeur nulle en cas d'erreur
- **Opérateurs de comparaison** : `<`, `>=`
- **Opérateur logique** : `or`

**Explication détaillée :**
1. **Vérification de l'index négatif** : `idx < 0` retourne `None` si l'index est négatif
2. **Vérification de dépassement** : `idx >= len(my_list)` vérifie que l'index n'est pas trop grand
3. **Accès sécurisé** : Si les conditions sont valides, retourne l'élément à la position `idx`

**Exemple d'utilisation :**
```python
my_list = [1, 2, 3, 4, 5]
print(element_at(my_list, 3))   # Affiche : 4
print(element_at(my_list, -1))  # Affiche : None
print(element_at(my_list, 10))  # Affiche : None
```

---

### 4-new_in_list.py
**Objectif :** Remplacer un élément dans une copie de la liste sans modifier l'originale.

**Code :**
```python
#!/usr/bin/python3
# Fonction qui remplace un élément dans une copie de la liste
def new_in_list(my_list, idx, element):
    # Vérifie si l'index est négatif ou hors limites
    if idx < 0 or idx >= len(my_list):
        # Retourne une copie de la liste originale
        return my_list.copy()
    # Crée une copie de la liste originale
    new_list = my_list.copy()
    # Remplace l'élément à l'index spécifié dans la copie
    new_list[idx] = element
    # Retourne la nouvelle liste modifiée
    return new_list
```

**Notions utilisées :**
- **copy()** : Méthode qui crée une copie superficielle de la liste
- **Immutabilité des paramètres** : Préservation de la liste originale
- **Assignation par index** : `new_list[idx] = element`

**Explication détaillée :**
1. **Vérification de l'index** : Si invalide, retourne une copie de la liste originale
2. **Création de copie** : `my_list.copy()` crée une nouvelle liste indépendante
3. **Modification de la copie** : Seule la copie est modifiée, pas l'originale
4. **Retour de la nouvelle liste** : La liste modifiée est retournée

**Pourquoi copy() ?**
Sans `copy()`, modifier la liste affecterait l'originale car les listes sont mutables et passées par référence.

**Exemple d'utilisation :**
```python
my_list = [1, 2, 3, 4, 5]
new_list = new_in_list(my_list, 2, 10)
print(new_list)  # [1, 2, 10, 4, 5]
print(my_list)   # [1, 2, 3, 4, 5] - Inchangée !
```

---

### 5-no_c.py
**Objectif :** Supprimer tous les caractères 'c' et 'C' d'une chaîne.

**Code :**
```python
#!/usr/bin/python3
# Fonction qui supprime tous les caractères 'c' et 'C' d'une chaîne
def no_c(my_string):
    # Crée une nouvelle chaîne vide pour stocker le résultat
    new_string = ""
    # Parcourt chaque caractère de la chaîne originale
    for char in my_string:
        # Vérifie si le caractère n'est pas 'c' ou 'C'
        if char != 'c' and char != 'C':
            # Ajoute le caractère à la nouvelle chaîne
            new_string += char
    # Retourne la nouvelle chaîne sans 'c' et 'C'
    return new_string
```

**Notions utilisées :**
- **Itération sur chaînes** : Les chaînes sont itérables comme les listes
- **Concaténation** : `+=` pour ajouter des caractères
- **Conditions multiples** : `and` pour combiner des conditions
- **Comparaison de caractères** : `!=` pour vérifier l'inégalité

**Explication détaillée :**
1. **Initialisation** : Création d'une chaîne vide pour stocker le résultat
2. **Parcours** : Chaque caractère est examiné individuellement
3. **Filtrage** : Seuls les caractères différents de 'c' et 'C' sont conservés
4. **Construction** : La nouvelle chaîne est construite progressivement

**Exemple d'utilisation :**
```python
print(no_c("Best School"))  # Best Shool
print(no_c("Chicago"))      # hiago
print(no_c("C is fun!"))    # is fun!
```

---

### 6-print_matrix_integer.py
**Objectif :** Afficher une matrice d'entiers (liste de listes).

**Code :**
```python
#!/usr/bin/python3
# Fonction qui affiche une matrice d'entiers
def print_matrix_integer(matrix=[[]]):
    # Parcourt chaque ligne de la matrice
    for row in matrix:
        # Parcourt chaque élément de la ligne avec son index
        for i, num in enumerate(row):
            # Affiche l'entier avec le format {:d}
            print("{:d}".format(num), end="")
            # Ajoute un espace sauf pour le dernier élément
            if i < len(row) - 1:
                print(" ", end="")
        # Passe à la ligne suivante après chaque ligne
        print()
```

**Notions utilisées :**
- **Listes imbriquées** : Matrice = liste de listes
- **enumerate()** : Fonction qui retourne l'index et la valeur
- **print() avec end** : Paramètre `end=""` pour contrôler le saut de ligne
- **Boucles imbriquées** : Une boucle dans une autre

**Explication détaillée :**
1. **Boucle externe** : Parcourt chaque ligne de la matrice
2. **enumerate()** : Permet d'obtenir l'index `i` et la valeur `num` simultanément
3. **Formatage** : Affiche l'entier sans saut de ligne (`end=""`)
4. **Espacement** : Ajoute un espace entre les nombres sauf après le dernier
5. **Nouvelle ligne** : `print()` seul crée un saut de ligne après chaque ligne

**Exemple d'utilisation :**
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print_matrix_integer(matrix)
# Sortie :
# 1 2 3
# 4 5 6
# 7 8 9
```

---

### 7-add_tuple.py
**Objectif :** Additionner deux tuples élément par élément.

**Code :**
```python
#!/usr/bin/python3
# Fonction qui additionne 2 tuples
def add_tuple(tuple_a=(), tuple_b=()):
    # Récupère le premier élément de tuple_a, ou 0 si absent
    a1 = tuple_a[0] if len(tuple_a) >= 1 else 0
    # Récupère le deuxième élément de tuple_a, ou 0 si absent
    a2 = tuple_a[1] if len(tuple_a) >= 2 else 0
    # Récupère le premier élément de tuple_b, ou 0 si absent
    b1 = tuple_b[0] if len(tuple_b) >= 1 else 0
    # Récupère le deuxième élément de tuple_b, ou 0 si absent
    b2 = tuple_b[1] if len(tuple_b) >= 2 else 0
    # Retourne un nouveau tuple avec les sommes
    return (a1 + b1, a2 + b2)
```

**Notions utilisées :**
- **Tuples** : Structures de données immutables
- **Expressions conditionnelles** : `valeur if condition else autre_valeur` (opérateur ternaire)
- **Tuple packing** : Création de tuple avec `(valeur1, valeur2)`
- **Gestion des cas limites** : Tuples de tailles différentes

**Explication détaillée :**
1. **Extraction sécurisée** : Utilise des expressions conditionnelles pour gérer les tuples de tailles variables
2. **Valeur par défaut** : Si un élément n'existe pas, utilise 0
3. **Addition** : Additionne les éléments correspondants
4. **Création de tuple** : Retourne un nouveau tuple avec les résultats

**Pourquoi cette approche ?**
- Les tuples peuvent avoir moins de 2 éléments
- Les tuples de plus de 2 éléments sont ignorés (seuls les 2 premiers comptent)

**Exemple d'utilisation :**
```python
print(add_tuple((1, 89), (88, 11)))  # (89, 100)
print(add_tuple((1, 89), (1,)))      # (2, 89)
print(add_tuple((1, 89), ()))         # (1, 89)
```

---

### 8-multiple_returns.py
**Objectif :** Retourner la longueur d'une chaîne et son premier caractère.

**Code :**
```python
#!/usr/bin/python3
# Fonction qui retourne un tuple avec la longueur et le premier caractère
def multiple_returns(sentence):
    # Calcule la longueur de la chaîne
    length = len(sentence)
    # Récupère le premier caractère, ou None si la chaîne est vide
    first = sentence[0] if length > 0 else None
    # Retourne un tuple avec la longueur et le premier caractère
    return (length, first)
```

**Notions utilisées :**
- **Retours multiples** : Un tuple permet de retourner plusieurs valeurs
- **Indexation de chaînes** : `sentence[0]` accède au premier caractère
- **None** : Valeur spéciale pour représenter l'absence de valeur
- **Tuple unpacking** : Permet de récupérer les valeurs séparément

**Explication détaillée :**
1. **Calcul de longueur** : `len(sentence)` retourne le nombre de caractères
2. **Gestion chaîne vide** : Si vide, retourne `None` pour le premier caractère
3. **Retour de tuple** : Les deux valeurs sont retournées ensemble

**Exemple d'utilisation :**
```python
length, first = multiple_returns("At school, I learnt C!")
print(f"Length: {length} - First character: {first}")
# Length: 22 - First character: A

length, first = multiple_returns("")
print(f"Length: {length} - First character: {first}")
# Length: 0 - First character: None
```

---

### 9-max_integer.py
**Objectif :** Trouver le plus grand entier d'une liste sans utiliser `max()`.

**Code :**
```python
#!/usr/bin/python3
# Fonction qui trouve le plus grand entier d'une liste
def max_integer(my_list=[]):
    # Retourne None si la liste est vide
    if len(my_list) == 0:
        return None
    # Initialise le maximum avec le premier élément
    max_value = my_list[0]
    # Parcourt chaque élément de la liste
    for num in my_list:
        # Compare et met à jour le maximum si nécessaire
        if num > max_value:
            max_value = num
    # Retourne la valeur maximale trouvée
    return max_value
```

**Notions utilisées :**
- **Algorithme de recherche** : Parcours séquentiel
- **Variable d'accumulation** : `max_value` stocke le maximum actuel
- **Comparaison** : Opérateur `>`
- **Initialisation** : Commence avec le premier élément

**Explication détaillée :**
1. **Cas vide** : Retourne `None` si la liste est vide
2. **Initialisation** : Le premier élément devient le maximum de départ
3. **Parcours** : Chaque élément est comparé au maximum actuel
4. **Mise à jour** : Si un élément est plus grand, il devient le nouveau maximum
5. **Retour** : La valeur maximale finale est retournée

**Algorithme :**
```
1. Si liste vide → retourner None
2. max = premier élément
3. Pour chaque élément de la liste :
   - Si élément > max alors max = élément
4. Retourner max
```

**Exemple d'utilisation :**
```python
my_list = [1, 90, 2, 13, 34, 5, -13, 3]
print(max_integer(my_list))  # 90

print(max_integer([]))  # None
print(max_integer([-5, -10, -3]))  # -3
```

---

### 10-divisible_by_2.py
**Objectif :** Trouver tous les multiples de 2 dans une liste.

**Code :**
```python
#!/usr/bin/python3
# Fonction qui trouve tous les multiples de 2 dans une liste
def divisible_by_2(my_list=[]):
    # Crée une nouvelle liste pour stocker les résultats
    result = []
    # Parcourt chaque nombre de la liste
    for num in my_list:
        # Vérifie si le nombre est divisible par 2 et ajoute True ou False
        result.append(num % 2 == 0)
    # Retourne la liste de résultats
    return result
```

**Notions utilisées :**
- **Opérateur modulo** : `%` retourne le reste de la division
- **append()** : Méthode pour ajouter un élément à la fin d'une liste
- **Booléens** : `True` et `False`
- **Expression booléenne** : `num % 2 == 0` évalue à `True` ou `False`

**Explication détaillée :**
1. **Création de liste** : Une nouvelle liste vide est créée
2. **Parcours** : Chaque nombre est examiné
3. **Test de divisibilité** : `num % 2 == 0` est vrai si le nombre est pair
4. **Ajout du résultat** : `True` si divisible par 2, `False` sinon
5. **Retour** : Liste de booléens de même taille que l'originale

**Pourquoi `% 2 == 0` ?**
- `%` donne le reste de la division
- Si `num % 2 == 0`, le nombre est divisible par 2 (pas de reste)
- Exemples : `4 % 2 = 0`, `5 % 2 = 1`

**Exemple d'utilisation :**
```python
my_list = [0, 1, 2, 3, 4, 5, 6]
result = divisible_by_2(my_list)
print(result)  # [True, False, True, False, True, False, True]

for i in range(len(result)):
    print(f"{my_list[i]} {'is' if result[i] else 'is not'} divisible by 2")
```

---

### 11-delete_at.py
**Objectif :** Supprimer un élément à une position spécifique dans une liste.

**Code :**
```python
#!/usr/bin/python3
# Fonction qui supprime un élément à une position spécifique
def delete_at(my_list=[], idx=0):
    # Vérifie si l'index est valide (positif et dans les limites)
    if idx >= 0 and idx < len(my_list):
        # Supprime l'élément en utilisant del
        del my_list[idx]
    # Retourne la liste modifiée
    return my_list
```

**Notions utilisées :**
- **del** : Mot-clé pour supprimer un élément par index
- **Modification in-place** : La liste originale est modifiée
- **Validation d'index** : Vérifie que l'index est valide avant suppression

**Explication détaillée :**
1. **Vérification** : S'assure que l'index est positif et dans les limites
2. **Suppression** : `del my_list[idx]` supprime l'élément à la position `idx`
3. **Retour** : La liste modifiée est retournée (même objet)

**Différence avec pop() :**
- `del my_list[idx]` : Supprime sans retourner la valeur
- `my_list.pop(idx)` : Supprime ET retourne la valeur (interdit ici)

**Exemple d'utilisation :**
```python
my_list = [1, 2, 3, 4, 5]
new_list = delete_at(my_list, 3)
print(new_list)  # [1, 2, 3, 5]
print(my_list)   # [1, 2, 3, 5] - Même objet modifié !
```

---

### 12-switch.py
**Objectif :** Échanger les valeurs de deux variables.

**Code :**
```python
#!/usr/bin/python3
a = 89
b = 10
a, b = b, a
print("a={:d} - b={:d}".format(a, b))
```

**Notions utilisées :**
- **Tuple unpacking** : Déballage de tuple
- **Assignment multiple** : Assignation simultanée de plusieurs variables
- **Swap idiomatique Python** : Échange de valeurs en une ligne

**Explication détaillée :**
1. **Initialisation** : `a = 89`, `b = 10`
2. **Échange** : `a, b = b, a`
   - Côté droit : `(b, a)` crée un tuple `(10, 89)`
   - Côté gauche : Le tuple est déballé dans `a` et `b`
   - Résultat : `a = 10`, `b = 89`
3. **Affichage** : Formate et affiche les nouvelles valeurs

**Pourquoi cette méthode ?**
En Python, cette technique évite d'utiliser une variable temporaire :
```python
# Méthode classique (autres langages) :
temp = a
a = b
b = temp

# Méthode Python (plus élégante) :
a, b = b, a
```

**Exemple d'utilisation :**
```bash
$ ./12-switch.py
a=10 - b=89
```

---

## Commandes et opérations importantes

### Opérations sur les listes

```python
# Création
ma_liste = [1, 2, 3]

# Accès par index
premier = ma_liste[0]      # 1
dernier = ma_liste[-1]     # 3

# Slicing (découpage)
sous_liste = ma_liste[0:2]  # [1, 2]
copie = ma_liste[:]         # Copie complète

# Modification
ma_liste[0] = 10           # [10, 2, 3]

# Ajout
ma_liste.append(4)         # [10, 2, 3, 4]
ma_liste.insert(0, 5)      # [5, 10, 2, 3, 4]

# Suppression
ma_liste.remove(10)        # Supprime la première occurrence de 10
del ma_liste[0]            # Supprime par index
element = ma_liste.pop()   # Supprime et retourne le dernier

# Autres opérations
longueur = len(ma_liste)   # Longueur
ma_liste.sort()            # Tri en place
ma_liste.reverse()         # Inverse en place
```

### Opérations sur les tuples

```python
# Création
mon_tuple = (1, 2, 3)
simple = (5,)              # Virgule obligatoire

# Accès (comme les listes)
premier = mon_tuple[0]

# Pas de modification possible !
# mon_tuple[0] = 10  # ERREUR !

# Tuple unpacking
a, b, c = mon_tuple        # a=1, b=2, c=3

# Concaténation (crée un nouveau tuple)
nouveau = mon_tuple + (4, 5)
```

### Formatage de chaînes

```python
# str.format()
"{:d}".format(42)          # "42" (entier décimal)
"{:s}".format("texte")     # "texte" (chaîne)
"{:.2f}".format(3.14159)   # "3.14" (float avec 2 décimales)

# Positions
"{0} {1}".format("a", "b") # "a b"
"{1} {0}".format("a", "b") # "b a"

# Nommage
"{nom}: {age:d}".format(nom="Alice", age=25)
```

### Boucles

```python
# For avec liste
for element in ma_liste:
    print(element)

# For avec index
for i in range(len(ma_liste)):
    print(i, ma_liste[i])

# For avec enumerate
for i, element in enumerate(ma_liste):
    print(f"Index {i}: {element}")

# While
i = 0
while i < len(ma_liste):
    print(ma_liste[i])
    i += 1
```

### Conditions

```python
# If simple
if x > 0:
    print("positif")

# If-else
if x > 0:
    print("positif")
else:
    print("négatif ou zéro")

# If-elif-else
if x > 0:
    print("positif")
elif x == 0:
    print("zéro")
else:
    print("négatif")

# Opérateur ternaire
resultat = "pair" if x % 2 == 0 else "impair"
```

## Concepts avancés

### List Comprehensions
Manière concise de créer des listes :

```python
# Classique
carres = []
for x in range(10):
    carres.append(x**2)

# List comprehension
carres = [x**2 for x in range(10)]

# Avec condition
pairs = [x for x in range(10) if x % 2 == 0]

# Matrice
matrice = [[i*j for j in range(3)] for i in range(3)]
```

### Slicing (découpage)
```python
ma_liste = [0, 1, 2, 3, 4, 5]

ma_liste[2:5]      # [2, 3, 4] - de l'index 2 à 4
ma_liste[:3]       # [0, 1, 2] - du début à l'index 2
ma_liste[3:]       # [3, 4, 5] - de l'index 3 à la fin
ma_liste[::2]      # [0, 2, 4] - tous les 2 éléments
ma_liste[::-1]     # [5, 4, 3, 2, 1, 0] - inverse
```

### Copie vs Référence
```python
# Référence (même objet)
liste_a = [1, 2, 3]
liste_b = liste_a
liste_b[0] = 10
print(liste_a)  # [10, 2, 3] - Modifiée aussi !

# Copie superficielle
liste_a = [1, 2, 3]
liste_b = liste_a.copy()  # ou liste_a[:]
liste_b[0] = 10
print(liste_a)  # [1, 2, 3] - Non modifiée
```

## Bonnes pratiques

1. **Utiliser des noms descriptifs**
   ```python
   # Mauvais
   l = [1, 2, 3]
   
   # Bon
   nombres = [1, 2, 3]
   ```

2. **Préférer les list comprehensions pour des opérations simples**
   ```python
   # Au lieu de
   carres = []
   for x in range(10):
       carres.append(x**2)
   
   # Utiliser
   carres = [x**2 for x in range(10)]
   ```

3. **Utiliser enumerate() au lieu de range(len())**
   ```python
   # Éviter
   for i in range(len(ma_liste)):
       print(i, ma_liste[i])
   
   # Préférer
   for i, element in enumerate(ma_liste):
       print(i, element)
   ```

4. **Choisir entre liste et tuple**
   - **Liste** : Pour des données qui changent
   - **Tuple** : Pour des données fixes (coordonnées, retours multiples)

5. **Vérifier les index avant d'accéder**
   ```python
   if 0 <= idx < len(ma_liste):
       element = ma_liste[idx]
   ```

## Exigences techniques
- **Python** : 3.8.5
- **OS** : Ubuntu 20.04 LTS
- **Style** : pycodestyle 2.7.*
- **Shebang** : `#!/usr/bin/python3` en première ligne
- **Permissions** : Tous les fichiers doivent être exécutables (`chmod +x fichier.py`)
- **Documentation** : Commentaires explicatifs dans le code
- **Imports** : Aucun module externe sauf indication contraire

## Comment tester
```bash
# Rendre le fichier exécutable
chmod +x 0-print_list_integer.py

# Exécuter le main
./0-main.py

# Vérifier le style
pycodestyle 0-print_list_integer.py

# Vérifier la longueur
wc -l 0-print_list_integer.py
```

## Ressources recommandées
- Documentation Python officielle sur les listes
- Documentation Python officielle sur les tuples
- PEP 8 - Style Guide for Python Code
- Python Tutorial - Data Structures

## Auteur
Projet réalisé dans le cadre du curriculum **Holberton School**

---

*Dernière mise à jour : 2026*
