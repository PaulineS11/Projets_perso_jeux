import random

def boule_magique():
    reponses = [
        "Oui, définitivement.",
        "C'est certain.",
        "Sans aucun doute.",
        "Oui, absolument.",
        "Vous pouvez compter là-dessus.",
        "Comme je le vois, oui.",
        "Très probablement.",
        "Les perspectives sont bonnes.",
        "Oui.",
        "Les signes pointent vers oui.",
        "Réponse brumeuse, essayez encore.",
        "Demandez à nouveau plus tard.",
        "Mieux vaut ne pas vous le dire maintenant.",
        "Impossible de prédire maintenant.",
        "Concentrez-vous et demandez à nouveau.",
        "Ne comptez pas dessus.",
        "Ma réponse est non.",
        "Mes sources disent non.",
        "Les perspectives ne sont pas si bonnes.",
        "Très douteux."
    ]

    print("Bienvenue dans la boule magique ! Posez une question et recevez une réponse mystique.")
    while True:
        question = input("\nPosez votre question (ou tapez 'quit' pour quitter) : ")
        if question.lower() == 'quit':
            print("Merci d'avoir utilisé la boule magique. À la prochaine fois !")
            break
        print("Réponse de la boule magique : " + random.choice(reponses))

if __name__ == "__main__":
    boule_magique()
