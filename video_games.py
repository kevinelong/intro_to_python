"""
sokoban - push warehouse boxes - pengo
pac-man
pong
asteroids
space invaders - shooting
"""

"""
The game is played on a board of squares, 
where each square is a floor or a wall. 
Some floor squares contain boxes, 
and some floor squares are marked as storage locations.

The player is confined to the board and may move horizontally or vertically onto empty squares 
(never through walls or boxes). 
The player can move a box by walking up to it and push it to the square beyond. 
Boxes cannot be pulled, and they cannot be pushed to squares with walls or other boxes. 
The number of boxes equals the number of storage locations. 
The puzzle is solved when all boxes are placed at storage locations.
"""

"""
NOUNS(person place or thing)
    Game, Player, Board, Box, Floor, Square, StorageLocation(target)
    
VERBS(action words)
    play
    move(left, right, up, down)
    push
    
ADJECTIVES(attributes/properties)
    marked
    direction
    square_type (e.g. floor or wall)
    contains (Box or nothing?)
    is_empty
    is_square_beyond_empty(does beyond have wall or box)
    number_of_boxes/storage_locations
    is_puzzle_solved? (all boxes on storage locations)
    

"""


class Direction:
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


class Location:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def move(self, direction: Direction):
        if direction == Direction.UP:
            self.y -= 1
        if direction == Direction.RIGHT:
            self.x += 1
        if direction == Direction.DOWN:
            self.y += 1
        if direction == Direction.LEFT:
            self.x -= 1


class Piece:
    symbol = "."

    def __init__(self, location: Location):
        self.location = location

    def __str__(self):
        return self.symbol


class Wall(Piece):
    symbol = "#"


class Floor(Piece):
    symbol = "."


class Box(Piece):
    symbol = "X"


class Target(Piece):
    symbol = "o"


class Player(Piece):
    symbol = "@"

    def __init__(self, name, location: Location):
        super().__init__(location)
        self.name = name
        self.moves = 0

    def move(self, direction: Direction):
        self.moves += 1
        self.location.move(direction)


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.rows = []
        for row_index in range(height):
            row = []
            for column_index in range(width):
                row.append(Floor(Location(column_index, row_index)))
            self.rows.append(row)


class Interface:
    def __init__(self, game):
        self.game = game

    @staticmethod
    def get_user_input():
        print("Move which direction? ('wasd' or 'hjkl' keys)")
        value = input().strip().lower()
        if value in ['w', 'k']:
            return Direction.UP

        if value in ['d', 'l']:
            return Direction.RIGHT

        if value in ['s', 'j']:
            return Direction.DOWN

        if value in ['a', 'h']:
            return Direction.LEFT

    def __str__(self):
        output = f"MOVES: {self.game.player.moves}\n"
        for row_index in range(self.game.board.height):
            for column_index in range(self.game.board.width):
                output += " " + str(self.game.board.rows[row_index][column_index])
            output += "\n"
        return output

    def show(self):
        print(self)


class Game:
    def __init__(self):
        self.playing = True
        self.board_width = 19
        self.board_height = 11
        self.player = Player("BOB", Location(self.board_width + 1 // 2, self.board_height + 1 // 2))
        self.board = Board(self.board_width, self.board_height)
        self.piece_list = []
        self.user_input = ""
        self.populate()
        self.interface = Interface(self)  # can be replaced after game is created to override default text interface

    def place_piece(self, p: Piece):
        # TODO verify space is empty
        self.piece_list.append(p)

    def move_piece(self, piece, destination: Location):
        pass
        # TODO validate destination

    def populate(self):
        piece_map = {
            " ": Floor,
            "#": Wall,
            "$": Box,
            ".": Target,
            "@": Player
        }
        data = """
    #####
    #   #
    #$  #
  ###  $##
  #  $ $ #
### # ## #   ######
#   # ## #####  ..#
# $  $          ..#
##### ### #@##  ..#
    #     #########
    #######
"""
        row_index = 0
        for line in data.split("\n"):
            if 0 == len(line.strip()):
                continue
            column_index = 0
            for c in line:
                location = Location(column_index, row_index)
                if c == "@":
                    self.player.location = location
                    self.place_piece(self.player)
                elif c != ' ':
                    kind = piece_map[c]
                    self.place_piece(kind(location))
                column_index += 1
            row_index += 1
        self.update_board()

    def update_board(self):
        self.board = Board(self.board_width, self.board_height)

        for p in self.piece_list:
            if p.location != self.player.location:
                self.board.rows[p.location.y][p.location.x] = p
        self.board.rows[self.player.location.y][self.player.location.x] = self.player

    @staticmethod
    def is_solved() -> bool:
        return False

    def display_state(self):
        self.interface.show()

    def update_state(self, move):
        self.player.move(move)
        self.update_board()

    def play(self):
        # game loop - infinite
        while self.playing:
            self.display_state()
            move = self.interface.get_user_input()
            self.update_state(move)


g = Game()
g.play()
