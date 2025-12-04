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

# Vérifier que l'utilisateur a bien sélectionné 3 personnages valides
def verif_nb_persos(indices, total):
    if len(indices) != 3:
        return False
    for i in indices:
        if i < 0 or i >= total:
            return False
    return True

# Vérifier que les indices sélectionnés ne sont pas déjà pris
def verif_disponibilite(indices, unavailable_indices):
    for i in indices:
        if i in unavailable_indices:
            return False
    return True 


# Sélectionner 3 personnages par l'utilisateur
def choisir_personnages(liste, unavailable_indices):
    while True:
        afficher_personnages(liste)
        choix = input("Sélectionnez 3 personnages en entrant leurs numéros séparés par des virgules (ex: 1,3,5) : ")
        try:
            indices = [int(i.strip()) - 1 for i in choix.split(",")]
            if not verif_nb_persos(indices, len(liste)):
                print("Vous devez sélectionner exactement 3 personnages valides. Veuillez réessayer.")
                continue
            if not verif_disponibilite(indices, unavailable_indices):
                print("Un ou plusieurs personnages sélectionnés ne sont pas disponibles. Veuillez réessayer.")
                continue
            equipe = [liste[i] for i in indices]
            return equipe
        except ValueError:
            print("Entrée invalide. Veuillez entrer des numéros valides séparés par des virgules.")

    # Choix aléatoire du monstre pour chaque vague
def choisir_monstre():
    monstres_data = dict(random.choice(list(db.monstres.find())))
    monstre = {
            "nom": monstres_data['nom'],
            "atk": monstres_data['atk'],
            "defense": monstres_data['defense'],
            "pv": monstres_data['pv']
        }
    print(f"\n Attention un {monstres_data['nom']} apparaît ! Brandissez vos armes !") 
    return monstre
    
    # Calcul des dégâts infligés
def calculer_degats(atk, defense):
    return max(0, atk - defense)
 
 # Fonction d'attaque entre un attaquant et une cible
def attaquer(attaquant, cible):
    degats = calculer_degats(attaquant['atk'], cible['defense'])
    cible['pv'] -= degats
    cible['pv'] = max(0, cible['pv'])
    print(f"{attaquant['nom']} attaque {cible['nom']} et inflige {degats} dégâts. PV restants de {cible['nom']} : {cible['pv']}")

# Choix aléatoire d'un personnage vivant dans l'équipe
def choix_random_perso_vivant(equipe_active):
    persos_vivants = [perso for perso in equipe_active if perso['pv'] > 0]
    return random.choice(persos_vivants) if persos_vivants else None

# Gestion d'une vague de combat entre l'équipe et un monstre
def vague_combat(equipe, monstres):
    print(f"\n Attention un {monstres['nom']} apparaît ! Brandissez vos armes !")

    for perso in equipe:
        if perso['pv'] > 0 and monstres['pv'] > 0:
            attaquer(perso, monstres)
        
    if monstres['pv'] <= 0:
        print(f"\n{monstres['nom']} a été vaincu !")
        return

    cible_perso = choix_random_perso_vivant(equipe)
    if cible_perso:
        attaquer(monstres, cible_perso)


