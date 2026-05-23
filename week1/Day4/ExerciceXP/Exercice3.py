class Dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f'{self.name} aboie'
    def run_speed(self):
        return self.weight / self.age * 10
    
    def fight(self, other_dog):
        if self.run_speed() * self.weight > other_dog.run_speed() * other_dog.weight:
            return f'{self.name} wins the fight'
        elif self.run_speed() * self.weight < other_dog.run_speed() * other_dog.weight:
            return f'{other_dog.name} wins the fight'
        else:
            return 'The fight is a tie'


davids_dog = Dog('Rex', 5, 20)
sarahs_dog = Dog('Buddy', 3, 15)
vital_dogs = Dog('Max', 4, 25)

print(f'combat entre {davids_dog.name} et {sarahs_dog.name} : {davids_dog.fight(sarahs_dog)}')
print(f'combat entre {davids_dog.name} et {vital_dogs.name} : {davids_dog.fight(vital_dogs)}')
print(davids_dog.bark())
print(davids_dog.run_speed())
print(davids_dog.fight(sarahs_dog))
print(davids_dog.fight(vital_dogs))

print(f'combat entre {sarahs_dog.name} et {davids_dog.name} : {sarahs_dog.fight(davids_dog)}')
print(f'combat entre {vital_dogs.name} et {sarahs_dog.name} : {vital_dogs.fight(sarahs_dog)}')

print(vital_dogs.bark())
print(vital_dogs.run_speed()) 
print(vital_dogs.fight(davids_dog))
print(vital_dogs.fight(sarahs_dog))


print(f'combat entre {sarahs_dog.name} et {davids_dog.name} : {sarahs_dog.fight(davids_dog)}')
print(f'combat entre {sarahs_dog.name} et {vital_dogs.name} : {sarahs_dog.fight(vital_dogs)}')
print(sarahs_dog.bark())
print(sarahs_dog.run_speed())
print(sarahs_dog.fight(davids_dog))
print(sarahs_dog.fight(vital_dogs))

