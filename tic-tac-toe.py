# how can we print every value of every column in every row of a list of lists?

data = [
    ['O', 'X', 'O'],
    ['X', 'X', 'O'],
    ['X', 'O', '.'],
]

# L1 How can we place a letter at the empty bottom right position?

data[2][2] = "X"

for row in data:
    for column in row:
        print(column, end=" ")
    print("")
print("")


# L2 How can we make the above into a function we can re-use?

def print_board(data):
    for row in data:
        for column in row:
            print(column, end=" ")
        print("")
    print("")


print_board(data)


# L3 How can we combine the data and the function into a Board class?


class Board:
    def __init__(self, data = None):
        self.boardview = data if data is not None else [
            ['X', 'X', 'O'],
            ['X', 'X', 'O'],
            ['X', 'O', 'X'],
        ]

    def print_board(self):
        for row in self.boardview:
            for column in row:
                print(column, end=" ")
            print("")
        print("")

    def make_move(self, x, y, value):
        self.x = x
        self.y = y
        self.boardview[x][y] = value


current_game=Board(data)
current_game.make_move(2, 2, "X")
current_game.print_board()


# L4 How can we say if X, O, or no-one has won? Can we put this in a Game class that uses the Board class?

class Game:
    def __init__(self):
        self.board = Board()

    def who_has_won(self):

        symbols = ["X", "O"]

        for symbol in symbols:
            for row in self.board.boardview:
                if row[0] == symbol and row[1] == symbol and row[2] == symbol:
                    return symbol

            for index in range(3):
                count = 0
                for row in self.board.boardview:
                    if row[index] == symbol:
                        count += 1
                if count == 3:
                    return symbol

            if self.board.boardview[0][0] == symbol and self.board.boardview[1][1] == symbol and \
                    self.board.boardview[2][2] == symbol:
                return symbol

            if self.board.boardview[0][2] == symbol and self.board.boardview[1][1] == symbol and \
                    self.board.boardview[2][0] == symbol:
                return symbol

        return None


newgame = Game()
newgame.board.print_board()
print(newgame.who_has_won())
