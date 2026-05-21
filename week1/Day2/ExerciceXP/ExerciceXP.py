# #exercice 1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
my_dict = dict(zip(keys, values))
print(my_dict)


# exercice 2

family_dict = {}

while True:
    name = input("entrer le nom d'un membre de la famille ou total pour afficher le total : ").strip()

    if name.lower() == "total":
        break

    age = input("entrer l'age de ce membre de la famille : ").strip()

    if not age.isdigit():
        print("Erreur : l'âge doit être un nombre.")
        continue

    family_dict[name] = int(age)


prix_total = 0

for name, age in family_dict.items():

    if age < 3:
        prix_billet = 0

    elif 3 <= age < 12:
        prix_billet = 10

    else:
        prix_billet = 15

    print(f"{name} doit payer {prix_billet} $")
    prix_total += prix_billet

print(f"le prix total du billet est de {prix_total} $")


# exercice 3

zara_dict = {
    "brand": {
        "name": "Zara",
        "creation_date": 1975,
        "creator_name": "Amancio Ortega Gaona",
        "type_of_clothes": ["men", "women", "children", "home"],
        "international_competitors": ["Gap", "H&M", "Benetton"],
        "number_stores": 7000,
        "major_color": {
            "France": "blue",
            "Spain": "red",
            "US": ["pink", "green"]
        }
    }
}

zara_dict["brand"]["number_stores"] = 2

print(
    f"La majeure partie des clients de Zara sont des "
    f"{zara_dict['brand']['type_of_clothes'][0]}, "
    f"{zara_dict['brand']['type_of_clothes'][1]}, "
    f"{zara_dict['brand']['type_of_clothes'][2]} et "
    f"{zara_dict['brand']['type_of_clothes'][3]}."
)

zara_dict["brand"]["country_creation"] = "Spain"

if "international_competitors" in zara_dict["brand"]:
    zara_dict["brand"]["international_competitors"].append("Desigual")

del zara_dict["brand"]["creation_date"]

print(zara_dict["brand"]["international_competitors"][-1])
print(zara_dict["brand"]["major_color"]["US"])

print(f"Le nombre de clés est : {len(zara_dict['brand'])}")

for key in zara_dict["brand"]:
    print(key)

more_on_zara = {
    "creation_date": 1975,
    "number_stores": 7000
}

zara_dict["brand"].update(more_on_zara)

print(zara_dict)


# exercice 4

def describe_city(city, country=None): 
    if not country:
        country = "Inconnu"
    print(f"{city} est dans {country}.")

describe_city("abidjan")
describe_city("Reykjavik", "Iceland")
describe_city("Paris", "France")


# exerccice 5 

import random

def generate_random_number(parametre):
    if parametre < 1 or parametre > 100:
        print("Erreur : le paramètre doit être un nombre entre 1 et 100.")
        return

    random_number = random.randint(1, 100)

    if random_number == parametre:
        print("Success!")
    else:
        print(f"Fail! Your number: {parametre}, Random number: {random_number}")

generate_random_number(50)




# exercice 6

def make_shirt(size="large", text="I love Python"):
    print(f"The size of the shirt is {size} and the text is {text}.")

make_shirt()
make_shirt(size="medium")
make_shirt(size="small", text="God is Good")

# exercice 7 

def get_random_temp():
    import random

    month = input("Entrez un mois entre 1 et 12 : ").strip()

    if not month.isdigit():
        print("Erreur : vous devez entrer un nombre.")
        return None

    month = int(month)

    if month < 1 or month > 12:
        print("Erreur : le mois doit être compris entre 1 et 12.")
        return None

    if month == 12 or month == 1 or month == 2:
        saison = "hiver"
        temperature = random.randint(-10, 16)

    elif month == 3 or month == 4 or month == 5:
        saison = "printemps"
        temperature = random.randint(0, 23)

    elif month == 6 or month == 7 or month == 8:
        saison = "été"
        temperature = random.randint(16, 40)

    else:
        saison = "automne"
        temperature = random.randint(0, 16)

    print(f"Saison détectée : {saison}")
    return temperature


def main():
    temperature = get_random_temp()

    if temperature is None:
        return

    print(f"La température actuelle est de {temperature}°C.")

    if temperature < 0:
        print("Il fait très froid dehors. Portez des vêtements chauds !")

    elif temperature < 16:
        print("Il fait frais dehors. N'oubliez pas votre manteau !")

    elif temperature < 23:
        print("Il fait doux dehors. Profitez de la journée !")

    elif temperature < 32:
        print("Il fait chaud dehors. Restez hydraté !")

    else:
        print("Il fait très chaud dehors. Restez à l'ombre et buvez beaucoup d'eau !")


main()


# Exercice 8

def main():
    base_price = 10.0
    topping_price = 2.50
    toppings = []

    while True:
        ingredient = input("Entrez un ingrédient pour votre pizza ou 'quit' pour terminer : ").strip()
        if ingredient.lower() == 'quit':
            break
        if ingredient == '':
            continue
        toppings.append(ingredient)
        print(f"Adding {ingredient} to your pizza.")

    print('\nIngredients de votre pizza :')
    if toppings:
        for t in toppings:
            print(f"- {t}")
    else:
        print("- (aucune garniture)")

    total = base_price + topping_price * len(toppings)
    print(f"Prix total de la pizza : ${total:.2f}")


if __name__ == '__main__':
    main()