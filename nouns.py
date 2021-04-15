"""
NOUNS - People Places or things - Classes
    Myself
    Kids
    Dog
    Furniture

What are the adjectives -> Attributes/Properties
What are the verbs action words (what do they do) -> Functions/Methods
"""


class Person:
    def __init__(self):
        self.has_class = False
        self.hydration = 100

    def walk(self):
        self.hydration -= 10


class Doctor(Person):
    def __init__(self, major="internal medicine"):
        super().__init__()
        self.phd = major


class Kid(Person):
    def __init__(self):
        super().__init__()
        self.energy = 100

    def make_noise(self):
        self.energy -= 5


class Pet:
    def __init__(self):
        self.fur = 200
        self.hydration = 100

    def shed(self):
        self.fur -= 20
        return 20

    def lick(self):
        self.hydration -= 1


class Fish(Pet):
    def __init__(self):
        super().__init__()
        self.scales = 10000

    def shed(self):
        self.scales -= 200
        return 200


class Furniture:
    def __init__(self, legs=0):
        self.storage_capacity_cft = 8
        self.stress = 0
        self.legs = legs

    def sit(self):
        self.stress += 5


class Table(Furniture):
    def __init__(self):
        super().__init__(legs=4)


class Software:
    def __init__(self, name, version=1):
        self.version = version
        self.name = name

    def describe(self):
        print(self.name + " " + self.version)


class OS(Software):
    def __init__(self, name="Ubuntu", version="Precise Pangolin"):
        super().__init__(name, version)

    def flavor(self):
        return self.name


generic = OS()
print(generic.flavor())

w = OS(name="Windows", version=10)
print(w.flavor())

my_os = OS()
my_os.describe()
