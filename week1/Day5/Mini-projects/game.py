# On importe le module random pour permettre a l'ordinateur
# de choisir un element au hasard
import random


# On cree une classe Game qui represente une partie du jeu
class Game:

    # Cette methode demande a l'utilisateur de choisir entre
    # pierre, feuille ou ciseaux
    def get_user_item(self):

        # Liste des choix autorises
        choices = ["pierre", "feuille", "ciseaux"]

        # On utilise une boucle infinie pour redemander le choix
        # tant que l'utilisateur ne donne pas une bonne reponse
        while True:

            # On recupere le choix de l'utilisateur
            # lower() permet de transformer le texte en minuscules
            user_item = input("Choisissez pierre, feuille ou ciseaux : ").lower()

            # Si le choix de l'utilisateur est dans la liste des choix autorises
            if user_item in choices:

                # On retourne le choix de l'utilisateur
                return user_item

            # Sinon, on affiche un message d'erreur
            else:
                print("Choix invalide. Veuillez choisir entre pierre, feuille ou ciseaux.")

    # Cette methode permet a l'ordinateur de choisir un element au hasard
    def get_computer_item(self):

        # Liste des choix possibles pour l'ordinateur
        choices = ["pierre", "feuille", "ciseaux"]

        # random.choice() choisit un element au hasard dans la liste
        computer_item = random.choice(choices)

        # On retourne le choix de l'ordinateur
        return computer_item

    # Cette methode compare le choix de l'utilisateur
    # avec celui de l'ordinateur pour determiner le resultat
    def get_game_result(self, user_item, computer_item):

        # Si les deux choix sont identiques, il y a match nul
        if user_item == computer_item:
            return "match nul"

        # Pierre gagne contre ciseaux
        elif user_item == "pierre" and computer_item == "ciseaux":
            return "victoire"

        # Feuille gagne contre pierre
        elif user_item == "feuille" and computer_item == "pierre":
            return "victoire"

        # Ciseaux gagnent contre feuille
        elif user_item == "ciseaux" and computer_item == "feuille":
            return "victoire"

        # Dans tous les autres cas, l'utilisateur perd
        else:
            return "defaite"

    # Cette methode lance une partie complete
    def play(self):

        # On recupere le choix de l'utilisateur
        user_item = self.get_user_item()

        # On recupere le choix de l'ordinateur
        computer_item = self.get_computer_item()

        # On determine le resultat de la partie
        result = self.get_game_result(user_item, computer_item)

        # On affiche les choix des deux joueurs
        print(f"\nVous avez choisi {user_item}.")
        print(f"L'ordinateur a choisi {computer_item}.")

        # On affiche un message selon le resultat
        if result == "victoire":
            print("Vous avez gagne !\n")

        elif result == "defaite":
            print("Vous avez perdu.\n")

        else:
            print("Vous avez fait match nul.\n")

        # On retourne le resultat pour pouvoir l'utiliser dans l'autre fichier
        return result