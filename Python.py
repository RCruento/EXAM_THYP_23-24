# Exemple Python



nom = input("Quel est votre nom ? ")


filiere = input("Quelle filière d'études préférez-vous ? ")


niveau_etudes = input("Quel est votre niveau d'études actuel (Licence, Master, Doctorat, etc.) ? ")

if niveau_etudes in ["Licence", "Master"] and filiere.lower() == "informatique":
    print(f"Félicitations {nom} ! Vous êtes accepté(e) dans la filière d'informatique de notre université.")
else:
    print(f"Désolé {nom}, votre candidature n'a pas été retenue pour le moment. Merci de postuler à nouveau plus tard.")
