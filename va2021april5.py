def get_average(numbers):
    running_total = 0
    # loop
    for n in numbers:
        # add each item to the running total
        running_total = running_total + n
        # running_total += n
    count = len(numbers)
    average = running_total / count
    return average


# Sample Data
data = [123, 597, 631, 61, 93, 509]

# Test function
result = get_average(data)
print(result)

print(get_average([123, 597, 631, 61, 93, 509]))


class Human:
    # Constructor
    def __init__(self, first, last):
        # PROPERTIES - variables in a class/object
        self.first = first
        self.last = last

    # METHODS - function defined inside of a class/object
    def full_name(self):
        return f"{self.last}, {self.first}"


h = Human("Kevin", "Long")
print(h.full_name())
print(h.full_name())

s = Human("Kay", "Long")
print(s.full_name())
print(s.full_name())



class Animal:
    def __init__(self, noise):
        self.noise = noise

    def speak(self):
        print(f"Animal goes '{self.noise}'.")

# INHERITANCE - IS A KIND OF...


class Pet(Animal): #A PET IS A KIND OF ANIMAL
    def __init__(self, name, noise):
        self.name=name
        super(Pet, self).__init__(noise)

    # def speak(self):
    #     print(f"{self.name} goes '{self.noise}'.")

a = Animal("Grrr")
a.speak()

b = Animal("cluck")
b.speak()

p = Pet("Bianca", "Meow")
p.speak()
