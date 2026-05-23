import math


class Circle:
    # Le constructeur permet de creer un cercle
    # On peut creer le cercle avec un rayon ou avec un diametre
    def __init__(self, radius=None, diameter=None):

        # Si l'utilisateur donne un rayon
        if radius is not None:
            self.radius = radius

        # Si l'utilisateur donne un diametre
        elif diameter is not None:
            self.radius = diameter / 2

        # Si l'utilisateur ne donne ni rayon ni diametre
        else:
            self.radius = 1

    # Cette propriete permet d'obtenir le diametre du cercle
    @property
    def diameter(self):
        return self.radius * 2

    # Cette propriete permet de modifier le diametre
    # Quand on change le diametre, le rayon est aussi mis a jour
    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    # Cette propriete permet de calculer l'aire du cercle
    @property
    def area(self):
        return math.pi * self.radius ** 2

    # Cette methode permet d'afficher les informations du cercle
    def __str__(self):
        return f"Circle(radius={self.radius}, diameter={self.diameter}, area={self.area:.2f})"

    # Cette methode permet d'additionner deux cercles
    # Elle retourne un nouveau cercle avec la somme des deux rayons
    def __add__(self, other):
        new_radius = self.radius + other.radius
        return Circle(radius=new_radius)

    # Cette methode permet de verifier si un cercle est plus grand qu'un autre
    def __gt__(self, other):
        return self.radius > other.radius

    # Cette methode permet de verifier si deux cercles sont egaux
    def __eq__(self, other):
        return self.radius == other.radius

    # Cette methode permet de trier les cercles dans une liste
    def __lt__(self, other):
        return self.radius < other.radius


# Creation de plusieurs cercles
circle1 = Circle(radius=5)
circle2 = Circle(diameter=20)
circle3 = Circle(radius=3)
circle4 = Circle(diameter=8)


# Affichage des cercles
print(circle1)
print(circle2)
print(circle3)
print(circle4)


# Affichage du rayon et du diametre
print("\nRayon du cercle 1 :", circle1.radius)
print("Diametre du cercle 1 :", circle1.diameter)


# Modification du diametre
circle1.diameter = 30
print("\nApres modification du diametre du cercle 1 :")
print(circle1)


# Calcul de l'aire
print("\nAire du cercle 2 :", circle2.area)


# Addition de deux cercles
circle5 = circle1 + circle2
print("\nAddition du cercle 1 et du cercle 2 :")
print(circle5)


# Comparaison entre deux cercles
print("\nLe cercle 1 est plus grand que le cercle 2 :", circle1 > circle2)
print("Le cercle 1 est egal au cercle 2 :", circle1 == circle2)


# Stockage des cercles dans une liste
circles = [circle1, circle2, circle3, circle4, circle5]

# Tri des cercles du plus petit au plus grand
sorted_circles = sorted(circles)

print("\nCercles tries du plus petit au plus grand :")
for circle in sorted_circles:
    print(circle)


# BONUS : Dessiner les cercles avec turtle
import turtle


def draw_circles(circles):
    # On cree une fenetre turtle
    screen = turtle.Screen()
    screen.title("Cercles tries")

    # On cree le crayon
    pen = turtle.Turtle()
    pen.speed(3)

    # Position de depart
    x_position = -300

    # On parcourt les cercles tries
    for circle in circles:
        # On leve le crayon pour se deplacer sans dessiner
        pen.penup()

        # On place le crayon a une nouvelle position
        pen.goto(x_position, -circle.radius)

        # On pose le crayon pour commencer a dessiner
        pen.pendown()

        # On dessine le cercle avec son rayon
        pen.circle(circle.radius)

        # On avance la position pour le prochain cercle
        x_position += circle.diameter + 30

    # On garde la fenetre ouverte
    turtle.done()


# Appel de la fonction bonus pour dessiner les cercles tries
draw_circles(sorted_circles)