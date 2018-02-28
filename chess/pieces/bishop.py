import math

from chess.pieces.piece import Piece


class Bishop(Piece):

    def is_valid_move(self, origin, destination):
        d_x, d_y = self._distance_between_coordinates(origin, destination)

        return d_x == d_y

    def __str__(self):
        return '\u2657' if self.color == 'white' else '\u265D'
