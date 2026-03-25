def generates_invitations(template, attendees):

	# on verifie les types
	if not isinstance(template, str):
		print("Error: template must be a string")
		return
	if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
		print("Error: attendees must be a list of dictionaries")
		return

    # Vérifier si vide
    if template == "":
        print("Template is empty, no output files generated.")
        return
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

