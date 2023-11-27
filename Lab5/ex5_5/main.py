class Animal:
    def __init__(self, breed, species):
        self.breed = breed
        self.species = species

    def speak(self):
        pass


class Mammal(Animal):
    def __init__(self, breed, species, fur_color):
        super().__init__(breed, species)
        self.fur_color = fur_color

    def speak(self):
        return "Mammals make various sounds."

    def give_birth(self):
        return f"{self.breed} is a mammal and gives birth."


class Bird(Animal):
    def __init__(self, breed, species, beak_length):
        super().__init__(breed, species)
        self.beak_length = beak_length

    def speak(self):
        return "Birds sing or make chirping sounds."

    def lay_eggs(self):
        return f"{self.breed} is a bird and lays eggs."


class Fish(Animal):
    def __init__(self, breed, species, scale_type):
        super().__init__(breed, species)
        self.scale_type = scale_type

    def speak(self):
        return "Fish do not make vocal sounds."

    def swim(self):
        return f"{self.breed} is a fish and can swim in water."


# Example usage:
cat = Mammal("Siamese Cat", "feline", "white and brown")
parrot = Bird("African Gray", "parrot", "medium")
shark = Fish("Tiger shark", "shark", "no")

print(f"{cat.breed} is a {cat.species} with {cat.fur_color} fur.")
print(cat.give_birth())
print(f"{cat.breed} says: {cat.speak()}")

print(f"{parrot.breed} is a {parrot.species} with a beak of length {parrot.beak_length}.")
print(parrot.lay_eggs())
print(f"{parrot.breed} says: {parrot.speak()}")

print(f"{shark.breed} is a {shark.species} with {shark.scale_type} scales.")
print(shark.swim())
print(f"{shark.breed} says: {shark.speak()}")
