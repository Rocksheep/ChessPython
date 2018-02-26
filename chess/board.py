from chess.pieces.piece import Piece


class Board:

    def __init__(self):
        self.width = 8
        self.height = 8
        self.pieces = []
        self._place_pieces()

    def _place_pieces(self):
        self.pieces.append(Piece('A1'))
        self.pieces.append(Piece('A2'))

    def get_piece_on_coordinates(self, coordinates):
        for piece in self.pieces:
            if piece.coordinates == coordinates:
                return piece
        return
