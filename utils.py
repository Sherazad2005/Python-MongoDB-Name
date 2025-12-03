import random
from config.db import db


#fonctions d'affichage et de sélection des personnages et des scores
def afficher_personnages(liste):
    print("\nListe des personnages :")
    for i, perso in enumerate(liste):
        print(f"{i+1}. {perso['nom']} - ATK: {perso['atk']} - DEF: {perso['defense']} - PV: {perso['pv']}")


# Afficher l'équipe sélectionnée
def afficher_equipe(equipe):
    print("\nÉquipe sélectionnée :")
    for perso in equipe:
        print(f"{perso['nom']} - ATK: {perso['atk']} - DEF: {perso['defense']} - PV: {perso['pv']}")


# Afficher le classement des scores
def afficher_classement(db):
    print("\n=== Classement des meillieurs Scores ===")
    top_scores = db.scores.find().sort("points", -1).limit(3)
    for i, score in enumerate(top_scores):
        print(f"{i+1}. {score['joueur']} - {score['points']} vagues")
        print("=========================")


# Sélectionner 3 personnages par l'utilisateur
def choisir_personnages(liste, unavailable_indices):
    while True:
        afficher_personnages(liste)
        choix = input("Sélectionnez 3 personnages en entrant leurs numéros séparés par des virgules (ex: 1,3,5) : ")
        try:
            indices = [int(i.strip()) - 1 for i in choix.split(",")]
            if len(indices) != 3 or any(i < 0 or i >= len(liste) or i in unavailable_indices for i in indices):
                raise ValueError
            return [liste[i] for i in indices]
        except ValueError:
            print("Sélection invalide. Veuillez réessayer.")

