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
    monstre= {
            "nom": monstres_data['nom'],
            "atk": monstres_data['atk'],
            "defense": monstres_data['defense'],
            "pv": monstres_data['pv']
            } 
    print(f"\nAttention un {monstre['nom']} apparaît ! Brandissez vos armes !")
    print(f"Stats du monstre -> PV: {monstre['pv']}, ATK: {monstre['atk']}, DEF: {monstre['defense']}")
    return monstre



    
    # Calcul des dégâts infligés
def calculer_degats(atk, defense):
    return max(0, atk - defense)


 
 # Fonction d'attaque entre un attaquant et une cible
def attaquer(attaquant, cible, technique):
    degats = technique['degats']
    if technique['type'] == 'soin':
        cible['pv'] = min(cible['pv'] - degats, cible.get('pv_max', cible['pv']))
        print(f"{attaquant['nom']} utilise {technique['nom']} et soigne {cible['nom']} de {-degats} points de vie. PV restants : {cible['pv']}")
    else:
        degats = max(0, degats + calculer_degats(attaquant['atk'], cible['defense']))
        cible['pv'] -= degats
        print(f"{attaquant['nom']} utilise {technique['nom']} et inflige {degats} dégâts à {cible['nom']}. PV restants : {cible['pv']}")



# Choix aléatoire d'un personnage vivant dans l'équipe
def choix_random_perso_vivant(equipe_active):
    persos_vivants = [perso for perso in equipe_active if perso['pv'] > 0]
    return random.choice(persos_vivants) if persos_vivants else None


# Phase d'attaques pour un personnage donné
def phase_attaques(perso, equipe, monstre):
    if perso['pv'] <= 0:
        return
    
    technique = choix_des_techniques(perso)

    if technique['type'] == 'soin':
        gestion_soin(perso, equipe, technique)
    else:
        attaquer(perso, monstre, technique)
        if monstre["pv"]<=0:
            return "monstre_mort"



# Gestion du soin d'un allié       
def gestion_soin(perso, equipe, technique):
    afficher_equipe(equipe)
    while True:
        try:
            choix = int(input(f"Choisissez un allié à soigner (1-{len(equipe)}): ")) - 1
            if 0 <= choix < len(equipe) and equipe[choix]["pv"] > 0:
                attaquer(perso, equipe[choix], technique)
                return
            print("Choix invalide ou allié mort. Veuillez réessayer.")
        except ValueError:
            print("Entrée invalide. Veuillez entrer un numéro valide.")



# Attaque du monstre sur un personnage aléatoire de l'équipe
def attaque_monstre(monstre, equipe):
    cible = choix_random_perso_vivant(equipe)
    if not cible:
        print("Tous les personnages sont morts. Le monstre ne peut pas attaquer.")
        return
    technique_monstre = random.choice(db.monstres.find_one({"nom": monstre['nom']})['techniques'])

    if technique_monstre['type'] == 'soin':
        gestion_soin(monstre, [monstre], technique_monstre)
    else:
        attaquer(monstre, cible, technique_monstre)


# Gestion d'une vague de combat entre l'équipe et un monstre
def vague_combat(equipe, monstre):

    while monstre['pv'] > 0 and any(p['pv']>0 for p in equipe):
        for perso in equipe:
            if perso['pv']> 0:
                etat = phase_attaques(perso, equipe, monstre)
                if etat == "monstre_mort":
                    print(f"\nLe monstre {monstre['nom']} a été vaincu !")
                    return "monstre_mort"
                
        if monstre['pv']>0:
             attaque_monstre(monstre, equipe)
    
    if all(p['pv'] <= 0 for p in equipe):
        print("\nToute l'équipe a été vaincue !")
        return "equipe_morte"
            


        

# Choix de la technique par le joueur
def choix_des_techniques(perso):
    print(f"\nTechniques disponibles pour {perso['nom']}:")
    for i, tech in enumerate(perso['techniques']):
        type_tech = tech['type'].capitalize()
        degats_str = f"{abs(tech['degats'])} dégâts" if tech['degats'] >= 0 else f"{abs(tech['degats'])} points de soin"
        print(f"{i+1}. {tech['nom']} ({type_tech}, {degats_str})")
    while True:
        choix = input("Choisissez une technique en entrant son numéro : ")
        try:
            index = int(choix) - 1
            if 0 <= index < len(perso['techniques']):
                return perso['techniques'][index]
            else:
                print("Numéro invalide. Veuillez réessayer.")
        except ValueError:
            print("Entrée invalide. Veuillez entrer un numéro valide.")




