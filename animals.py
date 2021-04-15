

class Animal:
    def __init__(self, noise):
        self.noise = noise  # noise property/attribute adj

    def speak(self):  # method - Verb action word
        print(self.noise)


a = Animal(noise="grrrr!")

a.speak()


class Bird(Animal):
    def __init__(self):
        self.noise = "tweet"


b = Bird()
b.speak()


class Pet(Animal):
    def __init__(self, name, noise):
        self.name = name
        super().__init__(noise)

    def speak(self): #overrides speak from the base class
        print(f"My name is {self.name} and I go \"{self.noise}\".")


pet1 = Pet("Bianca", "meeeeooow")
pet2 = Pet("Toby", "wooffle")

pet1.speak()
pet2.speak()

creatures = [a, b, pet1, pet2]

for creature in creatures:
    print("Creature says:")
    creature.speak()



