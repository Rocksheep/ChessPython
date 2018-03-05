from chess.player.color import Color
from chess.tile import Tile
from chess.pieces.bishop import Bishop
from chess.pieces.king import King
from chess.pieces.knight import Knight
from chess.pieces.queen import Queen
from chess.pieces.rook import Rook


class Board:

    def __init__(self):
        self.width = 8
        self.height = 8
        self.tiles = []
        for row in range(self.height):
            self.tiles.append([])
            for square in range(self.width):
                self.tiles[row].append(Tile(None))

        self._place_pieces()

    def _place_pieces(self):
        self.tiles[0][0].piece = Rook(Color.BLACK)
        self.tiles[0][1].piece = Knight(Color.BLACK)
        self.tiles[0][2].piece = Bishop(Color.BLACK)
        self.tiles[0][3].piece = Queen(Color.BLACK)
        self.tiles[0][4].piece = King(Color.BLACK)
        self.tiles[0][5].piece = Bishop(Color.BLACK)
        self.tiles[0][6].piece = Knight(Color.BLACK)
        self.tiles[0][7].piece = Rook(Color.BLACK)

        self.tiles[7][0].piece = Rook(Color.WHITE)
        self.tiles[7][1].piece = Knight(Color.WHITE)
        self.tiles[7][2].piece = Bishop(Color.WHITE)
        self.tiles[7][3].piece = Queen(Color.WHITE)
        self.tiles[7][4].piece = King(Color.WHITE)
        self.tiles[7][5].piece = Bishop(Color.WHITE)
        self.tiles[7][6].piece = Knight(Color.WHITE)
        self.tiles[7][7].piece = Rook(Color.WHITE)

    def get_piece_on_coordinates(self, coordinates):
        col = ord(coordinates[0]) - ord('a')
        row = self.width - int(coordinates[1])

        return self.tiles[row][col].piece
