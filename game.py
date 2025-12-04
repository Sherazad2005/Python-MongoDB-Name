import random
from config.db import db
from utils import choisir_monstre, vague_combat



def start_game(equipe):
    vague = 0
    equipe_active = [dict(perso) for perso in equipe]

    while any(perso['pv'] > 0 for perso in equipe_active):
        vague += 1
        print(f"\n--- Vague {vague} ---")
        monstre = choisir_monstre()
        vague_combat(equipe_active, monstre)

    print("\nTous vos personnages sont vaincus ! Fin du jeu.")
    return vague 

# Fonction principale pour démarrer le jeu
# Elle prend en paramètre l'équipe de personnages sélectionnée par l'utilisateur
# et gère les vagues de monstres jusqu'à la défaite de l'équipe.   