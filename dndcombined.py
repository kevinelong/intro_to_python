"""
CLASSES - NOUNS PEOPLE PLACES THINGS


Player - Wizard, Fighter, Paladin (Heath/hit-points, inventory(weapons, potions)

Monsters - Troll, Zombie, Dragon

FUNCTION/METHODS - VERBS- ACTION WORDS (Attack, Grab)

VARIABLES/PROPERTY/ATTRIBUTES - ADJECTIVES - ( player-class, strength, dexterity, health)
"""

from random import randint


class Item:
    def __init__(self, name):
        self.name = name


class Weapon(Item):
    def __init__(self, name, damage):
        self.damage = damage
        super().__init__(name)


class Sword(Weapon):
    def __init__(self):
        super().__init__("Sword", 12)


class Entity:
    def __init__(self, name, health=100, strength=9, dexterity=9, wisdom=9, intelligence=9, entity_class="Fighter"):
        self.name = name
        self.health = health
        self.strength = strength
        self.dexterity = dexterity
        self.wisdom = wisdom
        self.intelligence = intelligence
        self.entity_class = entity_class
        self.inventory = []

    def get(self, item):
        self.inventory.append(item)


class Monster(Entity):
    pass


class Player(Entity):
    pass


def attack_success(attacker: Entity, defender: Entity):
    base = 20
    base += attacker.dexterity
    base -= defender.dexterity
    roll = randint(0, 99)
    return roll > base


def attack(attacker, defender):
    if attack_success(attacker, defender):
        damage = randint(0, attacker.strength)
        defender.health -= damage
        print(f"{attacker.name} attacks {defender.name} and does {damage} damage. Only {defender.health} health left.")


def death(attacker, defender):
    if defender.health <= 0:
        print(f"{defender.name} has died.")
        for item in defender.inventory:
            attacker.get(item)
            defender.inventory.remove(item)
            print(f"{attacker.name} gets a {item.name} from {defender.name}.")


def fight(e1, e2):
    while e1.health > 0 and e2.health > 0:
        attack(e1, e2)
        attack(e2, e1)
        death(e1, e2)
        death(e2, e1)


"""
map od territory with open spaces walls or floor tile/square
end up grid of rows and columns

player - orientation/direction ^>v< move_forward turn(left or right)
"""

game_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, ],
    [1, 0, 0, 0, 0, 0, 0, 1, ],
    [1, 0, 0, 0, 0, 0, 0, 1, ],
    [1, 0, 0, 0, 0, 0, 0, 1, ],
    [1, 0, 0, 0, 0, 0, 0, 1, ],
    [1, 0, 0, 0, 0, 0, 0, 1, ],
    [1, 0, 0, 0, 0, 0, 0, 1, ],
    [1, 1, 1, 1, 1, 1, 1, 1, ],
]


# 1.  create a function to print the map out
def draw(game_map):
    for row in game_map:
        for column in row:
            if 1 == column:
                print("#", end=" ")
            elif 10 == column:
                print("^", end=" ")
            elif 11 == column:
                print(">", end=" ")
            elif 12 == column:
                print("v", end=" ")
            elif 13 == column:
                print("<", end=" ")
            elif 20 == column:
                print("Z", end=" ")
            elif 30 == column:
                print("+", end=" ")
            else:
                print(" ", end=" ")
        print("")


expected_output = """
########
#......#
#......#
#......#
#......#
#......#
#......#
########
"""


# create a class to store an x and y
class Position:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Direction:
    LEFT = 0
    RIGHT = 1


class Orientation:
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


class Sprite:
    def __init__(self):
        self.position = Position(4, 4)
        self.orientation = Orientation.NORTH

    def move_forward(self):
        next_position = Position(self.position.x,self.position.y)
        if self.orientation == Orientation.NORTH:
            next_position.y -= 1
        if self.orientation == Orientation.EAST:
            next_position.x += 1
        if self.orientation == Orientation.SOUTH:
            next_position.y += 1
        if self.orientation == Orientation.WEST:
            next_position.x -= 1

        if 1 != game_map[next_position.y][next_position.x]:
            self.position = next_position
        else:
            print("You bumped into a wall")

    def turn(self, direction):
        if direction == Direction.RIGHT:
            if self.orientation < Orientation.WEST:
                self.orientation += 1
            else:
                self.orientation = Orientation.NORTH
        if direction == Direction.LEFT:
            if self.orientation > Orientation.NORTH:
                self.orientation -= 1
            else:
                self.orientation = Orientation.WEST


def place_random(sprite):
    value = game_map[sprite.position.y][sprite.position.x]

    while value != 0:
        sprite.position = Position(randint(1, 6), randint(1, 6))
        value = game_map[sprite.position.y][sprite.position.x]


s = Sprite()
p = Player("Conan")
game_map[s.position.y][s.position.x] = 10 + s.orientation

m = Monster("Zombie", health=50, strength=6)
m.get(Sword())
ms = Sprite()
place_random(ms)

h = Entity("Health")
hs = Sprite()
place_random(hs)

while True:
    if m.health <= 0:
        # RESPAWN
        place_random(ms)
        game_map[ms.position.y][ms.position.x] = 0
        m.health = 100
    game_map[ms.position.y][ms.position.x] = 20
    game_map[hs.position.y][hs.position.x] = 30
    game_map[s.position.y][s.position.x] = 10 + s.orientation

    draw(game_map)

    print("Enter 'l' for left, 'r' for right, f for 'forward', 'q' for quit.")
    text = input()
    game_map[s.position.y][s.position.x] = 0

    if text == 'l':
        s.turn(Direction.LEFT)
    if text == 'r':
        s.turn(Direction.RIGHT)
    if text == 'f':
        s.move_forward()
    if text == 'q':
        break

    # collision detection
    if s.position.x == ms.position.x and s.position.y == ms.position.y:
        fight(p, m)
    if s.position.x == hs.position.x and s.position.y == hs.position.y:
        p.health = 100
        place_random(hs)


print("Thanks for playing!")
