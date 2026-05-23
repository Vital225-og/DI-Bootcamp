# On importe la classe Game qui se trouve dans le fichier game.py
from game import Game


# Cette fonction affiche le menu principal et recupere le choix de l'utilisateur
def get_user_menu_choice():

    # Affichage du menu
    print("Menu principal")
    print("1. Jouer une nouvelle partie")
    print("2. Afficher les scores")
    print("x. Quitter")

    # On recupere le choix de l'utilisateur
    # lower() permet d'accepter x ou X
    choice = input("Entrez votre choix : ").lower()

    # On retourne le choix
    return choice


# Cette fonction affiche les resultats des parties jouees
def print_results(results):

    # Affichage du titre du resume
    print("\nResume des parties")
    print("-------------------")

    # Affichage du nombre de victoires
    print(f"Victoires : {results['win']}")

    # Affichage du nombre de defaites
    print(f"Defaites : {results['loss']}")

    # Affichage du nombre de matchs nuls
    print(f"Matchs nuls : {results['draw']}")

    # Message de fin
    print("\nMerci d'avoir joue !")


# Cette fonction principale controle tout le programme
def main():

    # On cree un dictionnaire pour stocker les scores
    # win = nombre de victoires
    # loss = nombre de defaites
    # draw = nombre de matchs nuls
    results = {
        "win": 0,
        "loss": 0,
        "draw": 0
    }

    # Boucle principale du programme
    # Elle permet d'afficher le menu plusieurs fois
    while True:

        # On appelle la fonction du menu et on recupere le choix
        choice = get_user_menu_choice()

        # Si l'utilisateur choisit 1, il joue une nouvelle partie
        if choice == "1":

            # On cree un objet Game
            game = Game()

            # On lance une partie et on recupere le resultat
            result = game.play()

            # Si le joueur gagne, on ajoute 1 au nombre de victoires
            if result == "victoire":
                results["win"] += 1

            # Si le joueur perd, on ajoute 1 au nombre de defaites
            elif result == "defaite":
                results["loss"] += 1

            # Si le joueur fait match nul, on ajoute 1 au nombre de matchs nuls
            elif result == "match nul":
                results["draw"] += 1

        # Si l'utilisateur choisit 2, on affiche les scores
        elif choice == "2":
            print_results(results)

        # Si l'utilisateur choisit x ou q, on affiche les scores puis on quitte
        elif choice == "x" or choice == "q":
            print_results(results)
            break

        # Si l'utilisateur donne un mauvais choix
        else:
            print("Choix invalide. Veuillez choisir 1, 2 ou x.\n")


# On appelle la fonction principale pour demarrer le programme
main()