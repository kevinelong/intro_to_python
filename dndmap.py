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
        if self.orientation == Orientation.NORTH:
            self.position.y -= 1
        if self.orientation == Orientation.EAST:
            self.position.x += 1
        if self.orientation == Orientation.SOUTH:
            self.position.y += 1
        if self.orientation == Orientation.WEST:
            self.position.x -= 1

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


s = Sprite()


while True:
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


print("Thanks for playing!")
