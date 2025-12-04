import random
from config.db import db
from utils import choisir_monstre, vague_combat



def start_game(equipe):

    for perso in equipe:
        perso['pv_max'] = perso['pv']

    vagues = 0
    equipe_active = [dict(perso) for perso in equipe]
    monstre = None

    while any(perso['pv']> 0 for perso in equipe_active):
        if monstre is None or monstre['pv']<= 0:
            monstre = choisir_monstre()

        etat = vague_combat(equipe_active, monstre)

        if etat == "monstre_mort":
            vagues += 1
            monstre = None
            continue

        if etat == "equipe_morte":
            break

    print(f"\nL'équipe a été vaincue après {vagues} vagues de combat.")
    return vagues
# Elle prend en paramètre l'équipe de personnages sélectionnée par l'utilisateur
# et gère les vagues de monstres jusqu'à la défaite de l'équipe.   