from http.server import HTTPServer, BaseHTTPRequestHandler
import json


class requete(BaseHTTPRequestHandler):
    """Gestionnaire de requetes HTTP"""

    def do_GET(self):
        """
        Methode appelee automatiquement par Python
        a chaque fois qu'une requete GET arrive sur le serveur.
        self.path contient l'URL demandee ("/", "/data")
        """

        # Route "/"
        if self.path == "/":

            # Envoie le code de statut HTTP 200 = succes
            self.send_response(200)

            # Precise le type de contenu retourne : texte simple
            self.send_header("Content-Type", "text/plain")

            # Fin des headers - OBLIGATOIRE avant d'ecrire le contenu
            self.end_headers()

            # Envoie le contenu en bytes (le b devant la string)
            # Les bytes sont le format brut des donnees sur le reseau
            self.wfile.write(b"Hello, this is a simple API!")

        # ── Route "/data"
        elif self.path == "/data":

            self.send_response(200)

            # application/json indique au client que c'est du JSON
            self.send_header("Content-Type", "application/json")

            self.end_headers()

            # Le dictionnaire Python a retourner
            data = {"name": "John", "age": 30, "city": "New York"}

            # json.dumps() convertit le dict Python en string JSON
            # .encode("utf-8") convertit la string en bytes
            self.wfile.write(json.dumps(data).encode("utf-8"))

        # ── Route "/status"
        elif self.path == "/status":

            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        # ── Toute autre route → 404
        else:

            # 404 = la ressource demandee n'existe pas
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


if __name__ == "__main__":

    # HTTPServer prend : (adresse, port) et la classe gestionnaire
    # "" = ecoute sur toutes les interfaces reseau disponibles
    server = HTTPServer(("", 8000), requete)

    print("Server running on port 8000...")

    # Garde le serveur actif en permanence jusqu'a Ctrl+C
    server.serve_forever()
