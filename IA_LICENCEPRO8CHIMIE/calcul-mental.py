import random

def jeu_calcul_mental():
    print("Bienvenue au jeu de calcul mental !")
    print("Essayez de répondre correctement aux questions.")
    print("Tapez 'exit' pour quitter le jeu.\n")

    score = 0  # Initialiser le score

    while True:
        # Générer deux nombres aléatoires
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        
        # Choisir une opération aléatoire
        operation = random.choice(["+", "-", "*", "/"])
        
        # Calculer le résultat attendu
        if operation == "+":
            resultat_attendu = num1 + num2
        elif operation == "-":
            resultat_attendu = num1 - num2
        elif operation == "*":
            resultat_attendu = num1 * num2
        elif operation == "/":
            # Éviter la division par zéro et limiter à 2 décimales
            if num2 != 0:
                resultat_attendu = round(num1 / num2, 2)
            else:
                continue  # Passer à une nouvelle question
        
        # Poser la question
        question = f"Combien fait {num1} {operation} {num2} ? "
        reponse = input(question)
        
        # Permettre à l'utilisateur de quitter
        if reponse.lower() == "exit":
            print("\nMerci d'avoir joué ! Votre score final est :", score)
            break
        
        # Vérifier la réponse
        try:
            reponse_utilisateur = float(reponse)
            if abs(reponse_utilisateur - resultat_attendu) < 0.01:
                print("Bonne réponse ! 🎉")
                score += 1
            else:
                print(f"Mauvaise réponse. La bonne réponse était : {resultat_attendu}")
        except ValueError:
            print("Veuillez entrer un nombre valide.")

        print(f"Score actuel : {score}\n")

# Lancer le jeu
jeu_calcul_mental()