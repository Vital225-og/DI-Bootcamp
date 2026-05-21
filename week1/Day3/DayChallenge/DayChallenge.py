class Farm:
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = []

    def add_animal(self, **kwargs):
        for animal_type, count in kwargs.items():
            for animal in self.animals:
                if animal['type'] == animal_type:
                    animal['count'] += count
                    break
            else:
                self.animals.append({'type': animal_type, 'count': count})

    def get_animal_types(self):
        list_of_animals = sorted(set(animal['type'] for animal in self.animals))
        return list_of_animals

    def get_short_info(self):
        info = f"{self.name} Farm has "
        animal_types = self.get_animal_types()

        if len(animal_types) == 1:
            info += f"{animal_types[0]}s."
        elif len(animal_types) == 2:
            info += f"{animal_types[0]}s and {animal_types[1]}s."
        else:
            info += ", ".join(f"{animal}s" for animal in animal_types[:-1])
            info += f", and {animal_types[-1]}s."

        return info

    def get_info(self):
        info = f"{self.name} Farm\n"

        for animal in self.animals:
            info += f"{animal['type']} : {animal['count']}\n"

        info += "E-I-E-I-O!"
        return info


macdonald = Farm("McDonald's")

macdonald.add_animal(cow=5, sheep=2, goat=12)
macdonald.add_animal(cow=3)

print(macdonald.get_info())
print(macdonald.get_short_info())