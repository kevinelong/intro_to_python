"""
REQUIREMENTS:
Have a game where we score points for each player when they collect a treasure.
NOUNS == Classes (Points, Player, Treasure, Game)
VERBS == Methods/Functions ( collect )
ADJ/ADV = attribute/properties ( score? )
"""


class Map:
    def __init__(self):
        self.map = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]


class Treasure:
    def __init__(self, name, points=10):
        self.name = name
        self.points = points


class Player:
    def __init__(self, name):
        self.name = name
        self.avatar_image_path = ""
        self.score = 0

    def collect(self, treasure):
        self.score = self.score + treasure.points


class Game:
    def __init__(self):
        self.players = []
        self.players.append(Player("P1"))
        self.players.append(Player("P2"))

        self.treasures = []
        self.treasures.append(Treasure("Cherry", 100))
        self.treasures.append(Treasure("Pretzel", 200))

        self.players[0].collect(self.treasures[0])
        self.players[0].collect(self.treasures[1])

        print(self.players[0].score)


g = Game()
