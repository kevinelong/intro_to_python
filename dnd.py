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


p = Player("Conan")

m = Monster("Zombie", health=50, strength=6)
m.get(Sword())

fight(p, m)
