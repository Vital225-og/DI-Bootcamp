#exercise 1
print("hello world \n"*4)

#exercise 2
print((99**3)*8)   

# #exercise 3

5 < 3 #false
3 == 3 #true
3 == "3" #false because 3 is an integer and "3" is a string
# "3" > 3 # error because "3" is a string and 3 is an integer and '>' is not supported between instances of 'str' and 'int'
"Hello" == "hello" #false because the first letter of "Hello" is uppercase and the first letter of "hello" is lowercase

# #exercise 4
computer_brand= "Lenovo"
print(f"i have a {computer_brand} computer")

# #exercise 5
name= "Vital"
age= 21
shoe_size= 42
info = f"je suis {name}, j'ai {age} ans et je chausse du {shoe_size}" 
print(info)

# #exercise 6
a = 10
b=15
if a>b :
    print("hello world")

# exercise 7
nombre_str = input("entrer un nombre : ").strip()
if not nombre_str:
    print("Veuillez entrer un nombre entier.")
else:
    try:
        nombre = int(nombre_str)
    except ValueError:
        if "." in nombre_str or "," in nombre_str:
            print("Veuillez entrer un entier, pas un nombre à virgule.")
        else:
            print("Veuillez entrer un nombre entier valide.")
    else:
        if nombre % 2 == 0:
            print(f"{nombre} est pair")
        else:
            print(f"{nombre} est impair")


# #exercise 8
b = "vital"
a = input("entrer un nom : ").strip()
if a.casefold() == b:
    print("vous avez le meme nom que moi ")
else :
    print("ce n'est pas le même nom ")

# exercise 9
# exercise 9
while True:
    taille_str = input("entrer votre taille en cm (entier) ou 'q' pour quitter : ").strip()
    if taille_str.lower() == 'q':
        print("Abandon de la saisie de la taille.")
        break
    if not taille_str:
        print("Veuillez entrer une valeur pour la taille.")
        continue

    # Normaliser la virgule en point pour la conversion
    taille_norm = taille_str.replace(',', '.')

    # Cas entier (ex: "150")
    if taille_norm.lstrip('-').isdigit():
        taille = int(taille_norm)
        if taille < 0:
            print("La taille ne peut pas être négative.")
            continue
        if taille > 145:
            print("vous etes grands pour monter à cheval.")
        else:
            print("vous devez grandir pour pouvoir monter à cheval.")
        break

    # Cas nombre à virgule (ex: "150.0" ou "150,0")
    try:
        taille_float = float(taille_norm)
    except ValueError:
        print("Valeur non numérique. Veuillez entrer un entier en centimètres.")
        continue
    else:
        if not taille_float.is_integer():
            print("Veuillez entrer un entier en centimètres (pas un nombre à virgule).")
            continue
        taille = int(taille_float)
        if taille < 0:
            print("La taille ne peut pas être négative.")
            continue
        if taille > 145:
            print("vous etes grands pour monter à cheval.")
        else:
            print("vous devez grandir pour pouvoir monter à cheval.")
        break