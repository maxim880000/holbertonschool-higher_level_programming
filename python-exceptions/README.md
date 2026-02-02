# 🐍 Python - Exceptions

![Python](https://img.shields.io/badge/Python-3.8.5-blue?style=for-the-badge&logo=python)
![Ubuntu](https://img.shields.io/badge/Ubuntu-20.04_LTS-orange?style=for-the-badge&logo=ubuntu)

## 👤 Author
**GitHub:** [maxim880000](https://github.com/maxim880000)

---

## 📚 Description
Projet sur la gestion des exceptions en Python : `try/except`, `raise`, gestion des erreurs et création d'exceptions personnalisées.

---

## 🎯 Objectifs d'Apprentissage

À la fin de ce projet, vous serez capable d'expliquer :

- La différence entre erreurs et exceptions
- Ce que sont les exceptions et comment les utiliser
- Quand utiliser les exceptions
- Comment gérer correctement une exception
- Le but de capturer des exceptions
- Comment lever une exception intégrée
- Quand implémenter un nettoyage après une exception

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
| `0-safe_print_list.py` | Imprime x éléments d'une liste |
| `1-safe_print_integer.py` | Imprime un entier avec format |
| `2-safe_print_list_integers.py` | Imprime les x premiers entiers d'une liste |
| `3-safe_print_division.py` | Divise 2 entiers et affiche le résultat |
| `4-list_division.py` | Divise élément par élément deux listes |
| `5-raise_exception.py` | Lève une exception TypeError |
| `6-raise_exception_msg.py` | Lève une exception avec un message |

---

## 💻 Codes et Explications

### 0-safe_print_list.py
```python
#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print(my_list[i], end='')
            count += 1
        except IndexError:
            break
    print()
    return count
```

| Élément | Description |
|:--------|:------------|
| `try:` | Bloc de code à tenter |
| `except IndexError:` | Capture l'erreur d'index invalide |
| `break` | Sort de la boucle |
| `count` | Compte les éléments effectivement imprimés |

---

### 1-safe_print_integer.py
```python
#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
```

| Élément | Description |
|:--------|:------------|
| `{:d}` | Format décimal (entier uniquement) |
| `except (ValueError, TypeError):` | Capture plusieurs types d'erreurs |
| `ValueError` | Valeur incorrecte pour le format |
| `TypeError` | Type incompatible |

---

### 2-safe_print_list_integers.py
```python
#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
        except IndexError:
            break
    print()
    return count
```

| Élément | Description |
|:--------|:------------|
| `continue` | Passe à l'itération suivante |
| Ordre des except | Du plus spécifique au plus général |

---

### 3-safe_print_division.py
```python
#!/usr/bin/python3
def safe_print_division(a, b):
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
```

| Élément | Description |
|:--------|:------------|
| `ZeroDivisionError` | Erreur de division par zéro |
| `finally:` | Bloc toujours exécuté (succès ou erreur) |
| `result = None` | Valeur par défaut en cas d'erreur |

---

### 4-list_division.py
```python
#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            division = my_list_1[i] / my_list_2[i]
        except IndexError:
            print("out of range")
            division = 0
        except ZeroDivisionError:
            print("division by 0")
            division = 0
        except (TypeError, ValueError):
            print("wrong type")
            division = 0
        finally:
            result.append(division)
    return result
```

| Élément | Description |
|:--------|:------------|
| `IndexError` | Index hors limites |
| `ZeroDivisionError` | Division par zéro |
| `TypeError` | Type incompatible |
| `finally` avec `append` | Ajoute toujours le résultat |

---

### 5-raise_exception.py
```python
#!/usr/bin/python3
def raise_exception():
    raise TypeError
```

| Élément | Description |
|:--------|:------------|
| `raise` | Mot-clé pour lever une exception |
| `TypeError` | Type d'exception levée |

---

### 6-raise_exception_msg.py
```python
#!/usr/bin/python3
def raise_exception_msg(message=""):
    raise NameError(message)
```

| Élément | Description |
|:--------|:------------|
| `raise NameError(message)` | Lève une exception avec un message |
| `NameError` | Exception pour nom invalide |
| `message` | Message d'erreur personnalisé |

---

## 📊 Structure Try/Except/Else/Finally

```python
try:
    # Code qui peut lever une exception
    result = risky_operation()
except SpecificError:
    # Gère cette erreur spécifique
    handle_specific_error()
except (Error1, Error2):
    # Gère plusieurs types d'erreurs
    handle_multiple_errors()
except Exception as e:
    # Capture toute exception (à éviter si possible)
    print(f"Erreur: {e}")
else:
    # Exécuté si AUCUNE exception n'est levée
    success_operation()
finally:
    # TOUJOURS exécuté (nettoyage)
    cleanup()
```

---

## 📊 Types d'Exceptions Courantes

| Exception | Description | Exemple |
|:----------|:------------|:--------|
| `IndexError` | Index hors limites | `list[100]` quand len < 100 |
| `KeyError` | Clé de dictionnaire inexistante | `dict["missing"]` |
| `TypeError` | Type incompatible | `"hello" + 5` |
| `ValueError` | Valeur incorrecte | `int("abc")` |
| `ZeroDivisionError` | Division par zéro | `5 / 0` |
| `FileNotFoundError` | Fichier non trouvé | `open("missing.txt")` |
| `AttributeError` | Attribut inexistant | `"hello".missing()` |
| `NameError` | Variable non définie | `print(undefined_var)` |
| `ImportError` | Import échoué | `import nonexistent` |
| `SyntaxError` | Erreur de syntaxe | `if True print("x")` |

---

## 🔑 Bonnes Pratiques

### ✅ À faire
```python
# Capturer des exceptions spécifiques
try:
    result = int(user_input)
except ValueError:
    print("Veuillez entrer un nombre valide")

# Utiliser finally pour le nettoyage
try:
    file = open("data.txt")
    data = file.read()
finally:
    file.close()
```

### ❌ À éviter
```python
# NE PAS capturer toutes les exceptions sans raison
try:
    risky_code()
except:  # Capture TOUT, même Ctrl+C
    pass

# NE PAS ignorer les erreurs silencieusement
try:
    risky_code()
except Exception:
    pass  # L'erreur est perdue
```

---

## 📊 Hiérarchie des Exceptions

```
BaseException
├── SystemExit
├── KeyboardInterrupt
├── GeneratorExit
└── Exception
    ├── StopIteration
    ├── ArithmeticError
    │   ├── ZeroDivisionError
    │   └── OverflowError
    ├── AssertionError
    ├── AttributeError
    ├── LookupError
    │   ├── IndexError
    │   └── KeyError
    ├── NameError
    ├── OSError
    │   └── FileNotFoundError
    ├── TypeError
    └── ValueError
```

---

## 📖 Ressources

- [Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Learn to Program 11 Static & Exception Handling](https://www.youtube.com/watch?v=7vbgD-3s-w4)

---

<p align="center">Made with ❤️ at Holberton School</p>
