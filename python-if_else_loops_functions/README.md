# 🐍 Python - If/Else, Loops, Functions

![Python](https://img.shields.io/badge/Python-3.8.5-blue?style=for-the-badge&logo=python)
![Ubuntu](https://img.shields.io/badge/Ubuntu-20.04_LTS-orange?style=for-the-badge&logo=ubuntu)

## 👤 Author
**GitHub:** [maxim880000](https://github.com/maxim880000)

---

## 📚 Description
Projet sur les structures de contrôle en Python : conditions `if/elif/else`, boucles `for` et `while`, et définition de fonctions.

---

## 🎯 Objectifs d'Apprentissage

À la fin de ce projet, vous serez capable d'expliquer :

- Pourquoi l'indentation est importante en Python
- Comment utiliser les instructions `if`, `elif`, `else`
- Comment utiliser les commentaires
- Comment affecter des valeurs aux variables
- Comment utiliser les boucles `while` et `for`
- Comment utiliser `break` et `continue`
- Comment utiliser les clauses `else` sur les boucles
- Qu'est-ce que la fonction `range` et comment l'utiliser
- Qu'est-ce qu'une fonction et comment en définir une
- Ce que retourne une fonction sans instruction `return`
- La portée des variables (scope)
- Ce qu'est un traceback
- Les opérateurs arithmétiques et comment les utiliser

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
| `0-positive_or_negative.py` | Affiche si un nombre est positif, négatif ou zéro |
| `1-last_digit.py` | Affiche le dernier chiffre d'un nombre |
| `2-print_alphabet.py` | Affiche l'alphabet en minuscules |
| `3-print_alphabt.py` | Affiche l'alphabet sans 'e' et 'q' |
| `4-print_hexa.py` | Affiche les nombres de 0 à 98 en décimal et hexadécimal |
| `5-print_comb2.py` | Affiche les nombres de 00 à 99 |
| `6-print_comb3.py` | Affiche toutes les combinaisons de deux chiffres |
| `7-islower.py` | Vérifie si un caractère est en minuscule |
| `8-uppercase.py` | Affiche une chaîne en majuscules |
| `9-print_last_digit.py` | Affiche et retourne le dernier chiffre |
| `10-add.py` | Additionne deux entiers |
| `11-pow.py` | Calcule a puissance b |
| `12-fizzbuzz.py` | FizzBuzz classique |

---

## 💻 Codes et Explications

### 0-positive_or_negative.py
```python
#!/usr/bin/python3
import random
number = random.randint(-10, 10)

if number > 0:
    print(number, "is positive")
elif number < 0:
    print(number, "is negative")
else:
    print(number, "is zero")
```

| Élément | Description |
|:--------|:------------|
| `import random` | Importe le module pour générer des nombres aléatoires |
| `random.randint(-10, 10)` | Génère un entier entre -10 et 10 inclus |
| `if` | Condition si vraie |
| `elif` | Sinon si (else if) |
| `else` | Sinon (dernier cas) |

---

### 1-last_digit.py
```python
#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
if number < 0:
    last_digit = -last_digit
print(f"Last digit of {number} is {last_digit}", end=" ")
if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
```

| Élément | Description |
|:--------|:------------|
| `abs()` | Retourne la valeur absolue |
| `%` | Opérateur modulo (reste de la division) |
| `end=" "` | Empêche le saut de ligne après print |
| `f"..."` | F-string pour formater la chaîne |

---

### 2-print_alphabet.py
```python
#!/usr/bin/python3
for i in range(97, 123):
    print("{}".format(chr(i)), end="")
```

| Élément | Description |
|:--------|:------------|
| `range(97, 123)` | Génère les codes ASCII de 'a' (97) à 'z' (122) |
| `chr(i)` | Convertit un code ASCII en caractère |
| `format()` | Méthode de formatage de chaîne |
| `end=""` | Pas de saut de ligne |

---

### 3-print_alphabt.py
```python
#!/usr/bin/python3
for i in range(97, 123):
    if i != 101 and i != 113:
        print("{}".format(chr(i)), end="")
```

| Élément | Description |
|:--------|:------------|
| `!=` | Opérateur de différence |
| `and` | Opérateur logique ET |
| `101` | Code ASCII de 'e' |
| `113` | Code ASCII de 'q' |

---

### 4-print_hexa.py
```python
#!/usr/bin/python3
for i in range(99):
    print("{} = {}".format(i, hex(i)))
```

| Élément | Description |
|:--------|:------------|
| `range(99)` | De 0 à 98 inclus |
| `hex(i)` | Convertit un entier en hexadécimal |

---

### 5-print_comb2.py
```python
#!/usr/bin/python3
for i in range(100):
    if i != 99:
        print("{:02d}, ".format(i), end="")
    else:
        print("{:02d}".format(i))
```

| Élément | Description |
|:--------|:------------|
| `{:02d}` | Formatage sur 2 chiffres avec zéro devant |
| `:02` | Largeur de 2 caractères |
| `d` | Format décimal (entier) |

---

### 6-print_comb3.py
```python
#!/usr/bin/python3
for i in range(10):
    for j in range(i + 1, 10):
        if i != 8 or j != 9:
            print("{}{}".format(i, j), end=", ")
        else:
            print("{}{}".format(i, j))
```

| Élément | Description |
|:--------|:------------|
| `for j in range(i + 1, 10)` | Boucle imbriquée, j > i toujours |
| `or` | Opérateur logique OU |

---

### 7-islower.py
```python
#!/usr/bin/python3
def islower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
```

| Élément | Description |
|:--------|:------------|
| `def` | Mot-clé pour définir une fonction |
| `ord(c)` | Retourne le code ASCII du caractère |
| `return` | Retourne une valeur |
| `True/False` | Booléens |

---

### 8-uppercase.py
```python
#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            c = chr(ord(c) - 32)
        print("{}".format(c), end="")
    print()
```

| Élément | Description |
|:--------|:------------|
| `ord(c) - 32` | Différence ASCII entre minuscule et majuscule |
| `chr()` | Convertit code ASCII en caractère |
| `print()` | Saut de ligne à la fin |

---

### 9-print_last_digit.py
```python
#!/usr/bin/python3
def print_last_digit(number):
    last_digit = abs(number) % 10
    print("{}".format(last_digit), end="")
    return last_digit
```

| Élément | Description |
|:--------|:------------|
| `abs(number) % 10` | Dernier chiffre en valeur absolue |
| `return last_digit` | Retourne la valeur |

---

### 10-add.py
```python
#!/usr/bin/python3
def add(a, b):
    return a + b
```

| Élément | Description |
|:--------|:------------|
| `def add(a, b)` | Fonction avec 2 paramètres |
| `a + b` | Addition des deux nombres |

---

### 11-pow.py
```python
#!/usr/bin/python3
def pow(a, b):
    return a ** b
```

| Élément | Description |
|:--------|:------------|
| `**` | Opérateur puissance |
| `a ** b` | a élevé à la puissance b |

---

### 12-fizzbuzz.py
```python
#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print("{}".format(i), end=" ")
```

| Élément | Description |
|:--------|:------------|
| `i % 3 == 0` | Vérifie si i est divisible par 3 |
| `i % 5 == 0` | Vérifie si i est divisible par 5 |
| `range(1, 101)` | De 1 à 100 inclus |

---

## 📊 Tableau Récapitulatif

| Concept | Syntaxe | Description |
|:--------|:--------|:------------|
| **if** | `if condition:` | Exécute si vrai |
| **elif** | `elif condition:` | Sinon si |
| **else** | `else:` | Sinon |
| **for** | `for i in range(n):` | Boucle for |
| **range** | `range(start, stop, step)` | Génère une séquence |
| **def** | `def nom(params):` | Définit une fonction |
| **return** | `return valeur` | Retourne une valeur |
| **%** | `a % b` | Modulo (reste) |
| **\*\*** | `a ** b` | Puissance |
| **and** | `a and b` | ET logique |
| **or** | `a or b` | OU logique |
| **not** | `not a` | NON logique |
| **chr()** | `chr(65)` → `'A'` | Code ASCII → caractère |
| **ord()** | `ord('A')` → `65` | Caractère → code ASCII |
| **abs()** | `abs(-5)` → `5` | Valeur absolue |
| **hex()** | `hex(255)` → `'0xff'` | Décimal → hexadécimal |

---

## 📖 Ressources

- [More Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html)
- [IndentationError](https://www.digitalocean.com/community/tutorials/python-indentation)
- [How To Use String Formatters in Python 3](https://realpython.com/python-f-strings/)
- [Learn to Program 2 : Looping](https://www.youtube.com/watch?v=6iF8Xb7Z3wQ)

---

<p align="center">Made with ❤️ at Holberton School</p>
