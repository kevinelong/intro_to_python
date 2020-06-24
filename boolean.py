result = 9 > 6

age = 21
is_of_age = age >= 21

print(is_of_age)


class Person:
    def __init__(self):
        self.age = 21 # attribute of a person

    def is_of_age(self):
        return self.age > 21


p = Person()

if p.is_of_age():
    print("can drink")
