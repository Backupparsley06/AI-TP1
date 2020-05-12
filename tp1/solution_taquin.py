# -*- coding: utf-8 -*-

#####
# VotreNom (VotreMatricule) .~= À MODIFIER =~.
###

# Utiliser dbg() pour faire un break dans votre code.
from pdb import set_trace as dbg


#
# AEtoileTuple : Classe représentant un tuple de TaquinEtat, score f et d'un parent
# AEtoileTuple.
#
class AEtoileTuple:

    def __init__(self, etat, g, h, parent=None):
        self.etat = etat
        self.g = g
        self.f = g + h
        self.parent = parent

    # Fonction de comparaison entre deux AEtoileTuple.
    def __lt__(self, autre):
        return self.f < autre.f

    # Fonctions d'équivalence entre deux AEtoileTuple.
    def __eq__(self, autre):
        return self.etat == autre.etat

    def __ne__(self, autre):
        return not (self == autre)


def AEtoile(start, isGoal, transitions, heuristique, cost):
    open = []
    closed = []
    open.append(AEtoileTuple(start, 0, heuristique(start)))
    while True:
        n = open.pop(0)
        closed.append(n)
        if isGoal(n.etat):
            result = []
            while n is not None:
                result.append(n.etat)
                n = n.parent
            return result[::-1]
        for nPrime in transitions(n.etat):
            nPrime = AEtoileTuple(nPrime, n.g + cost(n.etat, nPrime), heuristique(nPrime), n)
            betterValue = True
            for i in range(len(open)):
                if nPrime == open[i]:
                    if nPrime < open[i]:
                        open.pop(i)
                    else:
                        betterValue = False
                    break
            for i in range(len(closed)):
                if nPrime == closed[i]:
                    if nPrime < closed[i]:
                        closed.pop(i)
                    else:
                        betterValue = False
                    break
            if betterValue:
                open.append(nPrime)
                open.sort()
#
# joueur_taquin : Fonction qui calcule le chemin, suite d'états, optimal afin de complété
#                  le puzzle.
#
# etat_depart: Objet de la classe TaquinEtat indiquant l'état initial du jeu.
#
# fct_estEtatFinal: Fonction qui prend en entrée un objet de la classe TaquinEtat et
#                   qui vérifie si l'état passée en paramêtre est l'état final ou non.
#
# fct_transitions: Fonction qui prend en entrée un objet de la classe TaquinEtat et
#                   qui retourne la listes des états voisins pour l'état donné.
#
# fct_heuristique: Fonction qui prend en entrée un objet de la classe TaquinEtat et
#                   qui retourne le coût heuristique pour se rendre à l'état final.
#
# retour: Cette fonction retourne la liste des états de la solution triés en ordre chronologique
#          c'est-à-dire de l'état initial jusqu'à l'état final inclusivement.
#


def joueur_taquin(etat_depart, fct_estEtatFinal, fct_transitions, fct_heuristique):
    def fct_cout(x, y): return 1
    return AEtoile(etat_depart, fct_estEtatFinal, fct_transitions, fct_heuristique, fct_cout)
