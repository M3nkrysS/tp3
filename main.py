"""
Nom : Lucas B. Tinkler
Groupe : 401
Détail : jeu de combat de monstre
"""
import random


def score_de():
    lance_de = random.randint(1, 6)
    return lance_de


def force_adversaire():
    force_ennemi = random.randint(1, 5)
    return force_ennemi


def jeu():
    niveau_vie = 5
    numero_adversaire = 0
    numero_combat = 0
    nombre_victoires = 0
    nombre_defaites = 0
    while True:
        force_adversaires = force_adversaire()
        score_du_de = score_de()
        print(f"Vous tombez face à face avec un adversaire de difficulté : {force_adversaires}\nQue voulez-vous faire?")
        print("1- Combattre cet adversaire\n2- Contourner cet adversaire et aller ouvrir une autre porte")
        choix = int(input("3- Afficher les règles du jeu\n4- Quitter la partie\n>>"))
        numero_adversaire += 1
        if choix == 1:
            numero_combat += 1
            print(f"\nAdversaire : {numero_adversaire}\nForce de l’adversaire : {force_adversaires}")
            print(f"Vie de l’usager : {niveau_vie}\nCombat {numero_combat} : {nombre_victoires} vs `{nombre_defaites}`")
            print(f"\nLancer du dé : {score_du_de}")
            if score_du_de > force_adversaires:
                nombre_victoires += 1
                niveau_vie += force_adversaires
                print(f"Victoire!\nNiveau de vie : {niveau_vie}\nNombre de victoires consécutives : {nombre_victoires}")
                print("Nouvelle porte\n---------------------------")
            else:
                nombre_defaites += 1
                niveau_vie -= force_adversaires
                print("défaite :(")
                if niveau_vie > 0:
                    print(f"Vie de l’usager : {niveau_vie}")
                    print("Nouvelle porte\n---------------------------")
                else:
                    print(f"Vie de l’usager : {niveau_vie}")
                    print(f"La partie est terminée, vous avez vaincu {nombre_victoires} monstre(s).\n")
                    print("GAME OVER")
                    break


jeu()
