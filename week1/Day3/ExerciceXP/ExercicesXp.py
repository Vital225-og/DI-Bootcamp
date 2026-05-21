# exercice 1 

# class Cat(): 
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# cat1 = Cat("milou", 4)

# cat2 = Cat("miaou", 5)

# cat3 = Cat("bobi", 2)


# def oldest_cat (*args): 
#     oldest = args[0]
#     for cat in args: 
#         if cat.age > oldest.age: 
#             oldest = cat
#     return oldest 

# print("the oldest cat is {} and is {} years old".format(oldest_cat(cat1, cat2, cat3).name, oldest_cat(cat1, cat2, cat3).age))

# oldest_cat(cat1, cat2, cat3)


# exercice 2

# class Dog:
#     def __init__(self, name, height):
#         self.name = name
#         self.height = height
        
#     def bark(self, name):
#             return f"{name} says woof!"
        
#     def jump(self, height):
#             return f"{self.name} jumps {height * 2} cm high!"
        
#     def __eq__(self, other):
#             return self.height == other.height
        
#     def __str__(self):
#             return f"{self.name} is {self.height} cm tall."

# davids_dog = Dog("Rex", 50)
# sarahs_dog = Dog("Teacup", 20)

# print(f"{davids_dog.name} is {davids_dog.height} cm tall \n - {sarahs_dog.name} is {sarahs_dog.height} cm tall.")


# print(davids_dog.bark(davids_dog.name))
# print(sarahs_dog.bark(sarahs_dog.name))

# print(davids_dog.jump(davids_dog.height))

# print(sarahs_dog.jump(sarahs_dog.height))



# exercice 3

class Song():
    def __init__(self, lyrics):
        self.lyrics  = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()


# exercice 4

class Zoo():
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []

    def add_animal(self, *new_animal):
        for animal in new_animal:
            if animal not in self.animals:
                self.animals.append(animal)
                print(f"{animal} has been added to the zoo.")
    
    def get_animals(self):
        print("The animals in the zoo are:")
        for animal in self.animals:
            print(animal, "\n")
    
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} has been sold.")
        else:
            print(f"{animal_sold} is not in the zoo.")
    
    def sort_animals(self):
        sorted_animals = sorted(self.animals)
        sorted_dict = {}
        for animal in sorted_animals:
            first_letter = animal[0]
            if first_letter not in sorted_dict:
                sorted_dict[first_letter] = []
            sorted_dict[first_letter].append(animal)
        return sorted_dict 

    def get_groups(self):
        sorted_animals = self.sort_animals()
        for letter, animals in sorted_animals.items():
            print(f"{letter}: {', '.join(animals)}") 

zoo_abidjan = Zoo("Abidjan Zoo")
zoo_abidjan.add_animal("Lion", "Giraffe", "Zebra", "Monkey", "Tiger", "Elephant")
zoo_abidjan.get_animals()
zoo_abidjan.sell_animal("Tiger")
zoo_abidjan.get_groups()
