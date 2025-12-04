from pymongo import MongoClient
from config.db import db

# Suppression des anciennes données
db.personnages.drop()
db.monstres.drop()
db.scores.drop()


# Liste des personnages
personnages = [
   {
        "nom": "Guerrier", "atk": 15, "defense": 10, "pv": 100,
        "techniques": [
            {"nom": "Coup d'épée maladroit", "type": "normale", "degats": 15},
            {"nom": "Cri de guerre dramatique", "type": "spéciale", "degats": 30},
            {"nom": "Bandage sur le bobo", "type": "soin", "degats": -20}
        ]
    },
    {
        "nom": "Mage", "atk": 20, "defense": 5, "pv": 80,
        "techniques": [
            {"nom": "Abracadabra", "type": "normale", "degats": 18},
            {"nom": "Vous ne passerez pas", "type": "spéciale", "degats": 40},
            {"nom": "Potion goût fraise, framboise, myrtille", "type": "soin", "degats": -25}
        ]
    },
    {
        "nom": "Voleur", "atk": 22, "defense": 8, "pv": 85,
        "techniques": [
            {"nom": "Je l'avais pourtant bien sécurisé avec le cadenat", "type": "normale", "degats": 17},
            {"nom": "Vol des bijoux de la courone", "type": "spéciale", "degats": 38},
            {"nom": "Pansement volé", "type": "soin", "degats": -18}
        ]
    },
    {
        "nom": "Paladin", "atk": 14, "defense": 12, "pv": 110,
        "techniques": [
            {"nom": "Coup de masse divinement bof", "type": "normale", "degats": 14},
            {"nom": "Jugement sacré (très bruyant)", "type": "spéciale", "degats": 32},
            {"nom": "Prière de la dernière chance", "type": "soin", "degats": -30}
        ]
    },
    {
        "nom": "Sorcier", "atk": 25, "defense": 3, "pv": 70,
        "techniques": [
            {"nom": "Sort de confusion", "type": "normale", "degats": 20},
            {"nom": "Malédiction ancestrale", "type": "spéciale", "degats": 45},
            {"nom": "Infusion de grenouilles", "type": "soin", "degats": -22}
        ]
    },
    {
        "nom": "Chevalier", "atk": 17, "defense": 15, "pv": 120,
        "techniques": [
            {"nom": "Charge un peu trop lente", "type": "normale", "degats": 15},
            {"nom": "Coup héroïque de tournoi", "type": "spéciale", "degats": 33},
            {"nom": "Serment de protection", "type": "soin", "degats": -27}
        ]
    },
    {
        "nom": "Moine", "atk": 19, "defense": 9, "pv": 95,
        "techniques": [
            {"nom": "Paume de la tranquillité", "type": "normale", "degats": 17},
            {"nom": "Chakra explosif", "type": "spéciale", "degats": 37},
            {"nom": "Respiration zen", "type": "soin", "degats": -25}
        ]
    },
    {
        "nom": "Berserker", "atk": 23, "defense": 6, "pv": 105,
        "techniques": [
            {"nom": "Coup de hache sauvage", "type": "normale", "degats": 20},
            {"nom": "Rage incontrôlable", "type": "spéciale", "degats": 45},
            {"nom": "Respire un coup (ça marche un peu)", "type": "soin", "degats": -15}
        ]
    },
    {
        "nom": "Chasseur", "atk": 16, "defense": 11, "pv": 100,
        "techniques": [
            {"nom": "Piège poussiéreux", "type": "normale", "degats": 15},
            {"nom": "Tir de précision improbable", "type": "spéciale", "degats": 34},
            {"nom": "Baume animal", "type": "soin", "degats": -22}
        ]
    }

]

# Liste des monstres
monstres = [
    {
        "nom": "Gobelin", "atk": 10, "defense": 5, "pv": 50,
        "techniques": [
            {"nom": "Jet de caillou", "type": "normale", "degats": 10},
            {"nom": "Cris stridents", "type": "spéciale", "degats": 22},
            {"nom": "Manger un vieux champignon", "type": "soin", "degats": -12}
        ]
    },
    {
        "nom": "Orc", "atk": 20, "defense": 8, "pv": 120,
        "techniques": [
            {"nom": "Coup de massue", "type": "normale", "degats": 18},
            {"nom": "Rugissement brutal", "type": "spéciale", "degats": 35},
            {"nom": "Mâcher un os", "type": "soin", "degats": -20}
        ]
    },
    {
        "nom": "Dragon", "atk": 35, "defense": 20, "pv": 300,
        "techniques": [
            {"nom": "Queue balayante", "type": "normale", "degats": 30},
            {"nom": "Flammes apocalyptiques", "type": "spéciale", "degats": 60},
            {"nom": "Repos draconique", "type": "soin", "degats": -40}
        ]
    },
    {
        "nom": "Zombie", "atk": 12, "defense": 6, "pv": 70,
        "techniques": [
            {"nom": "Morsure molle", "type": "normale", "degats": 10},
            {"nom": "Arrachement de membre (au hasard)", "type": "spéciale", "degats": 25},
            {"nom": "Recoudre un bout qui traîne", "type": "soin", "degats": -15}
        ]
    },
    {
        "nom": "Troll", "atk": 25, "defense": 15, "pv": 200,
        "techniques": [
            {"nom": "Coup de poing massif", "type": "normale", "degats": 22},
            {"nom": "Écrasement total", "type": "spéciale", "degats": 45},
            {"nom": "Régénération sale", "type": "soin", "degats": -30}
        ]
    },
    {
        "nom": "Spectre", "atk": 18, "defense": 10, "pv": 100,
        "techniques": [
            {"nom": "Souffle glacial", "type": "normale", "degats": 16},
            {"nom": "Hurlement spectral", "type": "spéciale", "degats": 35},
            {"nom": "Récupération astrale", "type": "soin", "degats": -20}
        ]
    },
    {
        "nom": "Golem", "atk": 30, "defense": 25, "pv": 250,
        "techniques": [
            {"nom": "Coup rocheux", "type": "normale", "degats": 28},
            {"nom": "Séisme miniature", "type": "spéciale", "degats": 50},
            {"nom": "Compaction minérale", "type": "soin", "degats": -35}
        ]
    },
    {
        "nom": "Vampire", "atk": 22, "defense": 12, "pv": 150,
        "techniques": [
            {"nom": "Coup de griffe", "type": "normale", "degats": 20},
            {"nom": "Absorption de vie", "type": "spéciale", "degats": 40},
            {"nom": "Siroter une poche de sang", "type": "soin", "degats": -30}
        ]
    },
    {
        "nom": "Loup-garou", "atk": 28, "defense": 18, "pv": 180,
        "techniques": [
            {"nom": "Griffure rapide", "type": "normale", "degats": 22},
            {"nom": "Hurlement lunaire", "type": "spéciale", "degats": 45},
            {"nom": "Léchage des blessures", "type": "soin", "degats": -25}
        ]
    },
    {
        "nom": "Squelette", "atk": 15, "defense": 7, "pv": 90,
        "techniques": [
            {"nom": "Lancer d’os", "type": "normale", "degats": 13},
            {"nom": "Déchaînement d’ossements", "type": "spéciale", "degats": 30},
            {"nom": "Repositionner ses os", "type": "soin", "degats": -18}
        ]
    }
]

# Liste des scores (initialement vide)
scores = [
    # Initialement vide
]


# Insertion des données
db.personnages.insert_many(personnages)
db.monstres.insert_many(monstres)


print("Base de données initialisée avec succès !")
