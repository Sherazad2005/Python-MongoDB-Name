import random

class Personnage:
    def __init__(self, nom, atk, defense, pv):
        self.nom = nom
        self.atk = atk
        self.defense = defense
        self.pv = pv
#Initialisation de la classes Personnage


class Monstre:
    def __init__(self, nom, atk, defense, pv):
        self.nom = nom
        self.atk = atk
        self.defense = defense
        self.pv = pv
#Initialisation de la classes Monstre



class Score:
    def __init__(self, joueur, points):
        self.joueur = joueur
        self.points = points
#Initialisation de la classes Score

