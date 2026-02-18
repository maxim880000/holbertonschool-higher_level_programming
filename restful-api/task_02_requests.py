import requests  # Permet d'envoyer des requêtes HTTP
import csv       # Permet de travailler avec des fichiers CSV


# Fonction qui récupère les posts et affiche leurs titres
def fetch_and_print_posts():
    # Envoie une requête GET à l'API
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status Code: {response.status_code}")
    # Affiche le code HTTP de la réponse (200 = OK)

    if response.status_code == 200:  # Vérifie que la requête a réussi
        posts = response.json()  # Convertit la réponse JSON en liste Python
        for post in posts:  # Parcourt chaque post
            print(post['title'])  # Affiche le titre du post


# Fonction qui récupère les posts et les sauvegarde dans un CSV
def fetch_and_save_posts():
    # Envoie une requête GET
    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    if response.status_code == 200:  # Vérifie que la requête a réussi
        posts = response.json()  # Convertit la réponse JSON en liste Python

        # Crée une nouvelle liste avec seulement les champs utiles
        data = [
            {'id': post['id'], 'title': post['title'], 'body': post['body']}
            for post in posts
        ]

        # Ouvre (ou crée) un fichier CSV en écriture
        with open('posts.csv', 'w', newline='', encoding='utf-8') as f:
            # Définit les colonnes
            writer = csv.DictWriter(f, fieldnames=['id', 'title', 'body'])
            writer.writeheader()  # Écrit la ligne d'en-tête (id,title,body)
            writer.writerows(data)  # Écrit toutes les lignes dans le fichier
