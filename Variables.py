# coding: utf-8

# imports
import random

# variables
# liste des joueurs (dictionnaire)
Players = {
    "Matthéo" : 85,
    "Alain" : 80,
    "Sébastien" : 87,
    "Camille" : 92,
    "Corentin" : 90,
    "Corinne" : 83
}
# tire aléatoirement le premier joueur parmi la liste des clés du dictionnaire
CurrentPlayer = random.choice(list(Players.keys()))
# compteur de nombre
CurrentNumber = 1
