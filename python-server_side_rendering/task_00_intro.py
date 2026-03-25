def generate_invitations(template, attendees):
    # Vérifie que template est bien une string
    if not isinstance(template, str):
        print("Invalid input: template must be a string.")
        return
    
    # Vérifie que attendees est bien une liste de dictionnaires
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Invalid input: attendees must be a list of dictionaries.")
        return

    # Vérifie que le template n'est pas vide
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return
    
    # Vérifie que la liste n'est pas vide
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    placeholders = ["name", "event_title", "event_date", "event_location"]

    # Parcourt chaque participant avec son index (commence à 1)
    for index, attendee in enumerate(attendees, start=1):
        content = template
        
        # Remplace chaque placeholder par la valeur du dictionnaire
        for key in placeholders:
            value = attendee.get(key)  # Retourne None si la clé est absente
            if not value:
                value = "N/A"  # Valeur par défaut si manquante ou None
            content = content.replace(f"{{{key}}}", value)

        # Écrit le résultat dans un fichier output_X.txt
        filename = f"output_{index}.txt"
        with open(filename, 'w') as f:
            f.write(content)