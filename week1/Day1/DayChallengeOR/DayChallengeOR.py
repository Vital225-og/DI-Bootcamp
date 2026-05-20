from datetime import datetime


def parse_birthdate(date_str):
    for separator in ['/', '-']:
        parts = date_str.split(separator)
        if len(parts) == 3:
            try:
                day, month, year = map(int, parts)
                return datetime(year, month, day)
            except ValueError:
                return None
    return None


def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def calculate_age(birthdate, today=None):
    if today is None:
        today = datetime.today()
    age = today.year - birthdate.year
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        age -= 1
    return age


def print_cake(candles_count):
    top = f"       ___{'i' * candles_count}___"
    lines = [
        top,
        "      |:H:a:p:p:y:|",
        "    __|___________|__",
        "   |^^^^^^^^^^^^^^^^^|",
        "   |:B:i:r:t:h:d:a:y:|",
        "   |                 |",
        "   ~~~~~~~~~~~~~~~~~~~",
    ]
    print("\n".join(lines))


def main():
    print("Bienvenue au gâteau d'anniversaire !")
    print("Entrez votre date de naissance au format DD/MM/YYYY.")

    birthdate = None
    while birthdate is None:
        user_input = input("Date de naissance : ").strip()
        birthdate = parse_birthdate(user_input)
        if birthdate is None:
            print("Format invalide. Utilisez DD/MM/YYYY, par exemple 21/05/1990.")

    today = datetime.today()
    if birthdate > today:
        print("La date de naissance ne peut pas être dans le futur.")
        return

    age = calculate_age(birthdate, today)
    last_digit = age % 10 if age >= 0 else 0
    print(f"\nVous avez {age} ans. Dernier chiffre de l'âge : {last_digit}.")

    print_cake(last_digit)

    if is_leap_year(birthdate.year):
        print("\nBonus : année bissextile détectée ! Voici un deuxième gâteau :")
        print_cake(last_digit)


if __name__ == "__main__":
    main()
