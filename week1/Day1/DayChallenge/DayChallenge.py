def get_integer(prompt):
    while True:
        value = input(prompt).strip()
        if not value:
            print("Veuillez entrer un nombre valide.")
            continue
        try:
            return int(value)
        except ValueError:
            print("Entrée invalide. Entrez un nombre entier.")


def challenge_1():
    print("\n--- Défi 1 : Liste de multiples ---")
    number = get_integer("Entrez un nombre : ")
    length = get_integer("Entrez la longueur de la liste : ")

    if length <= 0:
        print("La longueur doit être supérieure à 0.")
        return

    multiples = [number * i for i in range(1, length + 1)]
    print(f"Résultat : {multiples}")


def challenge_2():
    print("\n--- Défi 2 : Supprimer les lettres consécutives identiques ---")
    word = input("Entrez un mot : ").strip()
    if not word:
        print("Aucun mot saisi.")
        return

    result = []
    previous = None
    for char in word:
        if char != previous:
            result.append(char)
            previous = char

    print(f"Résultat : {''.join(result)}")


def main():
    print("Bienvenue dans les défis Python !")
    challenge_1()
    challenge_2()


if __name__ == "__main__":
    main()
