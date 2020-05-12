# -*- coding: utf-8 -*-

#####
# VotreNom (VotreMatricule) .~= À MODIFIER =~.
###

from pdb import set_trace as dbg  # Utiliser dbg() pour faire un break dans votre code.

import random
import numpy as np

########################
# Solution tic-tac-toe #
########################

#####
# joueur_tictactoe : Fonction qui calcule le prochain coup optimal pour gagner la
#                     la partie de Tic-tac-toe à l'aide d'Alpha-Beta Prunning.
#
# etat: Objet de la classe TicTacToeEtat indiquant l'état actuel du jeu.
#
# fct_but: Fonction qui prend en entrée un objet de la classe TicTacToeEtat et
#          qui retourne le score actuel tu plateau. Si le score est positif, les 'X' ont l'avantage
#          si c'est négatif ce sont les 'O' qui ont l'avantage, si c'est 0 la partie est nulle.
#
# fct_transitions: Fonction qui prend en entrée un objet de la classe TicTacToeEtat et
#                   qui retourne une liste de tuples actions-états voisins pour l'état donné.
#
# str_joueur: String indiquant c'est à qui de jouer : les 'X' ou 'O'.
#
# retour: Cette fonction retourne l'action optimal à joueur pour le joueur actuel c.-à-d. 'str_joueur'.
###

def joueur_tictactoe(etat,fct_but,fct_transitions,str_joueur):

    def tour_max(n, alpha, beta):
        if fct_but(n) is not None:
            return fct_but(n), None
        u = -float("inf")
        a = None
        for a_prime, n_prime in fct_transitions(n).items():
            u_prime, _ = tour_min(n_prime, alpha, beta)
            if u_prime > u:
                a = a_prime
                u = u_prime
            if u >= beta:
                return u, a
            alpha = max(alpha, u)
        return u, a

    def tour_min(n, alpha, beta):
        if fct_but(n) is not None:
            return fct_but(n), None
        u = float("inf")
        a = None
        for a_prime, n_prime in fct_transitions(n).items():
            u_prime, _ = tour_max(n_prime, alpha, beta)
            if u_prime < u:
                a = a_prime
                u = u_prime
            if u <= alpha:
                return u, a
            beta = max(beta, u)
        return u, a

    # Retourne une action aléatoire (.~= À MODIFIER =~.)
    # action = random.choice(list(fct_transitions(etat)))
    if str_joueur == 'X':
        _, action = tour_max(etat, -float("inf"), float("inf"))
    else:
        _, action = tour_min(etat, -float("inf"), float("inf"))

    return action
