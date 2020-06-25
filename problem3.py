# REQUIREMENT:
# create a class Game
# with a score attribute
# an increment method
# a decrement method
# a display method
#
# so as the following code will execute

# TODO - DEFINE CLASS


class Game:
    def __init__(self):
        self.score = 0

    def increment(self):
        self.score = self.score + 1

    def decrement(self):
        self.score -= 1

    def display(self):
        print(self.score)


g = Game()
g.increment()
g.increment()
g.increment()
g.display()
g.decrement()
g.decrement()
g.decrement()
g.display()

# this will display 1 and then 0
