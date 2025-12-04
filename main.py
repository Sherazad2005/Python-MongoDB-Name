from pymongo import MongoClient
from utils import afficher_personnages, afficher_equipe, afficher_classement, choisir_personnages
import game
from config.db import db

def main():
    print("Bienvenue dans le jeu de combat !")

    while True:

        print("\n==================")
        print("\nMenu Principal ")
        print("\n==================")
        print("1. Jouer une partie")
        print("2. Voir le classement des scores")
        print("3. Quitter")

        choix = input("Sélectionnez une option (1-3) : ")

        if choix == '1':
            nom_joueur = input("Entrez votre nom de joueur : ")
            equipe = choisir_personnages(list(db.personnages.find()), [])
            afficher_equipe(equipe)
            vagues = game.start_game(equipe)
            print(f"Félicitations {nom_joueur} ! Vous avez terminé le jeu en {vagues} vagues.")
            db.scores.insert_one({"joueur": nom_joueur, "points": vagues
            })
        elif choix == '2':
            afficher_classement(db)
        elif choix == '3':
            print("Merci d'avoir joué ! Au revoir.")
            break
        else:
            print("Option invalide. Veuillez réessayer.")

main()
# Point d'entrée principal du programme



