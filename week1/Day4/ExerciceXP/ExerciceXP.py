from Exercice3 import Dog  
import random


# # class Pets():
# #     def __init__(self, animals):
# #         self.animals = animals

# #     def walk(self):
# #         for animal in self.animals:
# #             print(animal.walk())

# # class Cat():
# #     is_lazy = True

# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age

# #     def walk(self):
# #         return f'{self.name} is just walking around'

# # class Bengal(Cat):
# #     def sing(self, sounds):
# #         return f'{sounds}'

# # class Chartreux(Cat):
# #     def sing(self, sounds):
# #         return f'{sounds}'


# # class Siamese(Cat):
# #     def sing(self, sounds):
# #         return f'{sounds}'

# # bengal = Bengal('bengal', 5)
# # chartreux = Chartreux('chartreux' , 3)
# # siamese = Siamese('siamese' , 4)
# # all_cats = [bengal, chartreux, siamese]
# # sara_pets = Pets(all_cats)

# # sara_pets.walk()




# # exercice 2


# class Dog():
#     def __init__(self, name, age, weight):
#         self.name = name
#         self.age = age
#         self.weight = weight

#     def bark(self):
#         return f'{self.name} aboie'
#     def run_speed(self):
#         return self.weight / self.age * 10
    
#     def fight(self, other_dog):
#         if self.run_speed() * self.weight > other_dog.run_speed() * other_dog.weight:
#             return f'{self.name} wins the fight'
#         elif self.run_speed() * self.weight < other_dog.run_speed() * other_dog.weight:
#             return f'{other_dog.name} wins the fight'
#         else:
#             return 'The fight is a tie'


# davids_dog = Dog('Rex', 5, 20)
# sarahs_dog = Dog('Buddy', 3, 15)
# vital_dogs = Dog('Max', 4, 25)

# print(f'combat entre {davids_dog.name} et {sarahs_dog.name} : {davids_dog.fight(sarahs_dog)}')
# print(f'combat entre {davids_dog.name} et {vital_dogs.name} : {davids_dog.fight(vital_dogs)}')
# print(davids_dog.bark())
# print(davids_dog.run_speed())
# print(davids_dog.fight(sarahs_dog))
# print(davids_dog.fight(vital_dogs))

# print(f'combat entre {sarahs_dog.name} et {davids_dog.name} : {sarahs_dog.fight(davids_dog)}')
# print(f'combat entre {vital_dogs.name} et {sarahs_dog.name} : {vital_dogs.fight(sarahs_dog)}')

# print(vital_dogs.bark())
# print(vital_dogs.run_speed()) 
# print(vital_dogs.fight(davids_dog))
# print(vital_dogs.fight(sarahs_dog))


# print(f'combat entre {sarahs_dog.name} et {davids_dog.name} : {sarahs_dog.fight(davids_dog)}')
# print(f'combat entre {sarahs_dog.name} et {vital_dogs.name} : {sarahs_dog.fight(vital_dogs)}')
# print(sarahs_dog.bark())
# print(sarahs_dog.run_speed())
# print(sarahs_dog.fight(davids_dog))
# print(sarahs_dog.fight(vital_dogs))



# # exerccice 3


class PetDog(Dog):
    def __init__(self, name, age, weight, trained = False):
        super().__init__(name, age, weight)
        self.trained = trained

    def train(self):
        self.trained = True
        print(self.bark())
    
    def play(self, *args):
        return f'{", ".join(args)} all play together'
    
    def do_a_trick(self):
        if self.trained:
            tricks = [f'{self.name} does a barrel roll', f'{self.name} stands on his back legs', f'{self.name} shakes your hand', f'{self.name} plays dead']
            return random.choice(tricks)
        else:
            return f'{self.name} is not trained yet'
        
        
my_dog = PetDog('Charlie', 2, 10)
my_milou = PetDog('Milou', 3, 12)
print(my_dog.train())
print(my_dog.do_a_trick())
print(my_milou.do_a_trick())
print(my_dog.play(my_milou.name))
my_dog.play("Buddy", "Max")


# exercise 4

class Person:
    def __init__(self, first_name, age, last_name=""):
        self.first_name = first_name
        self.age = age
        self.last_name = last_name

    def is_18(self):
        return self.age >= 18


class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def born(self, first_name, age):
        new_person = Person(first_name, age, self.last_name)
        self.members.append(new_person)

    def check_majority(self, first_name):
        for person in self.members:
            if person.first_name.lower() == first_name.lower():
                if person.is_18():
                    print("You are over 18, your parents Jane and John accept that you will go out with your friends")
                else:
                    print("Sorry, you are not allowed to go out with your friends.")
                return

        print(f"{first_name} is not in the family.")

    def family_presentation(self):
        print(f"Family name: {self.last_name}")

        for person in self.members:
            print(f"{person.first_name} {person.last_name}, {person.age} years old")


my_family = Family("Coulibaly")

my_family.born("Vital", 20)
my_family.born("Elisa", 19)
my_family.born("Junior", 12)

my_family.family_presentation()

my_family.check_majority("Vital")
my_family.check_majority("Junior")