from chess.pieces.bishop import Bishop
from chess.pieces.king import King
from chess.pieces.knight import Knight
from chess.pieces.queen import Queen
from chess.pieces.rook import Rook


class Board:

    def __init__(self):
        self.width = 8
        self.height = 8
        self.squares = []
        for row in range(self.height):
            self.squares.append([])
            for square in range(self.width):
                self.squares[row].append(None)

        self._place_pieces()

    def _place_pieces(self):
        self.squares[0][0] = Rook('black')
        self.squares[0][1] = Knight('black')
        self.squares[0][2] = Bishop('black')
        self.squares[0][3] = Queen('black')
        self.squares[0][4] = King('black')
        self.squares[0][5] = Bishop('black')
        self.squares[0][6] = Knight('black')
        self.squares[0][7] = Rook('black')

        self.squares[7][0] = Rook('white')
        self.squares[7][1] = Knight('white')
        self.squares[7][2] = Bishop('white')
        self.squares[7][3] = Queen('white')
        self.squares[7][4] = King('white')
        self.squares[7][5] = Bishop('white')
        self.squares[7][6] = Knight('white')
        self.squares[7][7] = Rook('white')

    def get_piece_on_coordinates(self, coordinates):
        col = ord(coordinates[0]) - ord('a')
        row = self.width - int(coordinates[1])

        return self.squares[row][col]
