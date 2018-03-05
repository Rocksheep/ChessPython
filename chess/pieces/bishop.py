import math

from chess.pieces.piece import Piece
from chess.player.color import Color


class Bishop(Piece):

    def is_valid_move(self, origin, destination):
        d_x, d_y = self._distance_between_coordinates(origin, destination)

        return abs(d_x) == abs(d_y)

    def __str__(self):
        return '\u2657' if self.color == Color.WHITE else '\u265D'
