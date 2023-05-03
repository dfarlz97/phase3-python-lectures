import ipdb

class Pet:
    count = 0
    def __init__(self, name, species, age, size, temperment):
        self.name = name
        self.species = species
        self.age = age
        self.size = size
        self.temperment = temperment
        Pet.count += 1


    def print_pet_details(self):
        print(f'''
              name: {self.name}
              species: {self.species}
              age: {self.age}
              size: {self.size}
              temperment: {self.temperment}
              ''')
        
    def get_details_in_one_line(self):
        print(f"{self.name} is a {self.temperment} {self.species}, who is {self.size} in size and {self.age} years old.")

    @classmethod
    def get_pet_count(Pet):
        print(f"There are {Pet.count} pets")

spot = Pet("Spot", "Dog", "6", "Medium", "Playful")
rose = Pet("Rose", "Cat", "4", "Small", "Crazy")
piper = Pet("Piper", "dog", "9", "medium", "mean")


ipdb.set_trace()
