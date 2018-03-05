from chess.pieces.piece import Piece
from chess.player.color import Color


class King(Piece):

    def is_valid_move(self, origin, destination):
        d_x, d_y = self._distance_between_coordinates(origin, destination)

        return max(abs(d_x), abs(d_y)) == 1

    def __str__(self):
        return '\u2654' if self.color == Color.WHITE else '\u265A'
