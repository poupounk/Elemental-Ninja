import random

# Les éléments du jeu Elemental Ninja : fire, water, ice
elements = ["fire", "water", "ice"]

# Les valeurs possibles des cartes
valeurs = [2, 3, 4, 5, 6, 7]

# Dictionnaire associant les cartes à leurs couleurs
couleurs_cartes = {
    "fire_2": "yellow",
    "fire_3": "blue",
    "fire_4": "green",
    "fire_5": "orange",
    "fire_6": "purple",
    "fire_7": "red",
    "ice_2": "red",
    "ice_3": "purple",
    "ice_4": "orange",
    "ice_5": "green",
    "ice_6": "blue",
    "ice_7": "yellow",
    "water_2": "red",
    "water_3": "yellow",
    "water_4": "purple",
    "water_5": "blue",
    "water_6": "orange",
    "water_7": "green"
}

# Fonction pour générer une pioche complète (toutes les combinaisons possibles)
def generer_pioche():
    pioche = []
    for element in elements:
        for valeur in valeurs:
            pioche.append({"element": element, "valeur": valeur})
    random.shuffle(pioche)  # Mélange la pioche pour plus d'aléatoire
    return pioche

# Fonction pour choisir un certain nombre de cartes depuis une pioche
def choisir_depuis_pioche(pioche, nombre):
    main = []
    while len(main) < nombre and pioche:
        carte = pioche.pop()  # Pioche une carte aléatoire de la pioche
        main.append(carte)
    return main

# Fonction pour afficher une carte sous forme de chaîne (texte)
def afficher(carte):
    return f"{carte['element']}_{carte['valeur']}"

# Comparaison des cartes
def comparer_cartes(carte_joueur, carte_ordi):
    hierarchie = {
        "fire": {"bat": "ice", "perd": "water"},
        "water": {"bat": "fire", "perd": "ice"},
        "ice": {"bat": "water", "perd": "fire"}
    }

    element_joueur = carte_joueur["element"]
    element_ordi = carte_ordi["element"]

    # Comparaison des éléments
    if element_joueur == element_ordi:
        # Si les éléments sont égaux, comparer la valeur
        if carte_joueur["valeur"] > carte_ordi["valeur"]:
            return "joueur"
        elif carte_joueur["valeur"] < carte_ordi["valeur"]:
            return "ordi"
        else:
            return "egalite"
    elif hierarchie[element_joueur]["bat"] == element_ordi:
        return "joueur"
    else:
        return "ordi"

def tirer_carte_aleatoire(pioche):
    if not pioche:
        pioche = generer_pioche()  # Régénérer la pioche si elle est vide
    return random.choice(pioche)  # Tirer une carte au hasard
