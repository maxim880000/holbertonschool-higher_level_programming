def generate_invitations(template, attendees):
    # 1. Vérification des types
    if not isinstance(template, str):
        print("Invalid input: template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Invalid input: attendees must be a list of dictionaries.")
        return

    # 2. Vérification des valeurs vides
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # 3. Génération des fichiers
    placeholders = ["name", "event_title", "event_date", "event_location"]

    for index, attendee in enumerate(attendees, start=1):
        content = template
        for key in placeholders:
            value = attendee.get(key)
            if not value:
                value = "N/A"
            content = content.replace(f"{{{key}}}", value)

        filename = f"output_{index}.txt"
        with open(filename, 'w') as f:
            f.write(content)
