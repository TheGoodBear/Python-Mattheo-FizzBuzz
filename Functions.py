# coding: utf-8

# imports
import random

import Variables as Var


def ShowTitle():

    # démarrage
    print("\nJeu du FizzBuzz")
    print("---------------")

    # afficher la liste des joueurs
    ShowPlayers()

    # démarrer la partie
    input("\nEntrée pour démarrer la partie.")


def StartGame():

    # tant qu'il reste plus de 1 joueur
    while len(Var.Players) > 1:

        # tire un nombre aléatoire entre 1 et 100
        TurnChance = random.randint(1, 100)

        # réponse
        Answer = ""

        # teste si le joueur courant donne la bonne réponse
        if Var.Players[Var.CurrentPlayer] >= TurnChance:
            # bonne réponse

            if Var.CurrentNumber % 15 == 0:
                Answer = f"{Var.CurrentPlayer} dit FizzBuzz ({Var.Players[Var.CurrentPlayer]} >= {TurnChance})"
            elif Var.CurrentNumber % 5 == 0:
                Answer = f"{Var.CurrentPlayer} dit Buzz ({Var.Players[Var.CurrentPlayer]} >= {TurnChance})"
            elif Var.CurrentNumber % 3 == 0:
                Answer = f"{Var.CurrentPlayer} dit Fizz ({Var.Players[Var.CurrentPlayer]} >= {TurnChance})"
            else:
                Answer = f"{Var.CurrentPlayer} dit {Var.CurrentNumber} ({Var.Players[Var.CurrentPlayer]} >= {TurnChance})"

            # sélectionne le joueur suivant
            GetNextPlayer()

            # affiche le résultat du tour
            print(Answer)

        else:
            # mauvaise réponse

            # indique une mauvaise réponse
            Answer = f"{Var.CurrentPlayer} se trompe ({Var.Players[Var.CurrentPlayer]} < {TurnChance})"

            # affiche le résultat du tour
            print(Answer)

            # sauve le joueur courant
            BadPlayer = Var.CurrentPlayer

            # sélectionne le joueur suivant
            GetNextPlayer()

            # retire le joueur qui a donné la mauvaise réponse
            Var.Players.pop(BadPlayer)

            # afficher la liste des joueurs
            ShowPlayers()

            # continuer la partie
            input("\nEntrée pour continuer la partie...")


        # incrémente le nombre
        Var.CurrentNumber += 1


def EndGame():
    
    # déclarer le vainqueur
    print(f"\n{Var.CurrentPlayer} a gagné(e) !")

    # fin de la partie
    print("\nAu revoir.\n")


def ShowPlayers():

    # afficher la liste des joueurs
    print("\nParticipants en jeu : ")

    # for Player in Players:
    #     print(f"{Player} avec {Players[Player]}% de chances de donner une bonne réponse")
    for PlayerName, PlayerChance in Var.Players.items():
        
        IsFirstPlayer = ""
        # teste s'il s'agit du 1er joueur
        if PlayerName == Var.CurrentPlayer:
            IsFirstPlayer = " (premier joueur)"
        print(f"  {PlayerName}{IsFirstPlayer} avec {PlayerChance}% de chances de donner une bonne réponse")


def GetNextPlayer():

    # sélectionne le joueur suivant
    NextPlayerSelected = False
    PlayerHasChanged = False
    for PlayerName in Var.Players:
        if PlayerName == Var.CurrentPlayer:
            NextPlayerSelected = True
        elif NextPlayerSelected:
            Var.CurrentPlayer = PlayerName
            PlayerHasChanged = True
            break
    # si le prochain joueur n'a pas été défini, il s'agit du premier de la liste
    if not PlayerHasChanged:
        Var.CurrentPlayer = list(Var.Players.keys())[0]
