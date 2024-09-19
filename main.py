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


def force_boss


def jeu():
    niveau_vie = 5
    numero_adversaire = 0
    numero_combat = 0
    nombre_victoires = 0
    victoires_consecutive = 0
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
            combat_boss = numero_combat % 3
            if combat_boss == 0:

            print(f"\nAdversaire : {numero_adversaire}\nForce de l’adversaire : {force_adversaires}")
            print(f"Vie de l’usager : {niveau_vie}\nCombat {numero_combat} : {nombre_victoires} vs `{nombre_defaites}`")
            print(f"\nLancer du dé : {score_du_de}")
            if score_du_de > force_adversaires:
                nombre_victoires += 1
                victoires_consecutive += 1
                niveau_vie += force_adversaires
                print(f"Victoire!\nNiveau de vie : {niveau_vie}\nNombre de victoires consécutives : {victoires_consecutive}")
                print("Nouvelle porte\n---------------------------")
            else:
                nombre_defaites += 1
                victoires_consecutive = 0
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
        elif choix == 2:
            victoires_consecutive = 0
            niveau_vie -= 1
            print(f"\nVous vous échapez.\n-1 pont de vie\nVie de l'usager : {niveau_vie}")
            print("Nouvelle porte\n---------------------------")
        elif choix == 3:
            print("\nRègles du jeu:")
            print("Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.")
            print("  Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.")
            print("Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire.")
            print("  Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.")
            print("\nLa partie se termine lorsque les points de vie de l’usager tombent sous 0.")
            print("\nL’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie.")
            print("Nouvelle porte\n---------------------------")
        elif choix == 4:
            print("Merci et au revoir...")
            break


jeu()
