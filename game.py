import random
from config.db import db


def start_game(equipe):
    vague = 0
    equipe_active = [dict(perso) for perso in equipe]

    while True:
        vague += 1
        print(f"\n--- Vague {vague} ---")

        monstres_data = dict(random.choice(list(db.monstres.find())))
        monstres = {
            "nom": monstres_data['nom'],
            "atk": monstres_data['atk'],
            "defense": monstres_data['defense'],
            "pv": monstres_data['pv']
        }
        print("\n Attention un {monstre['nom]} apparaît ! Brandissez vos armes !") 
                        
        while monstres['pv'] > 0 and any(perso['pv'] > 0 for perso in equipe_active):
            print("\n=== Tour des combatants ===")
            for perso in equipe_active:
                if perso['pv'] > 0 and monstres['pv'] > 0:
                    degats = max(0, perso['atk'] - monstres['defense'])
                    monstres['pv'] -= degats
                    print(f"{perso['nom']} attaque {monstres['nom']} et inflige {degats} dégâts. PV restants du monstre : {max(0, monstres['pv'])}")
            if monstres['pv'] <= 0:
                print(f"\n{monstres['nom']} a été vaincu !")
                break
            for perso in equipe_active:
                if perso['pv'] > 0 and monstres['pv'] > 0:
                    degats = max(0, monstres['atk'] - perso['defense'])
                    perso['pv'] -= degats
                    print(f"{monstres['nom']} attaque {perso['nom']} et inflige {degats} dégâts. PV restants de {perso['nom']} : {max(0, perso['pv'])}")    
        if all(perso['pv'] <= 0 for perso in equipe_active):
            print("\nVotre équipe a été vaincue ! Fin du jeu.")
            break   
    return vague    

# Fonction principale pour démarrer le jeu
# Elle prend en paramètre l'équipe de personnages sélectionnée par l'utilisateur
# et gère les vagues de monstres jusqu'à la défaite de l'équipe.   