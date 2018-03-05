from chess.pieces.piece import Piece
from chess.player.color import Color


class Knight(Piece):

    def is_valid_move(self, origin, destination):
        d_x, d_y = self._distance_between_coordinates(origin, destination)
        d_x = abs(d_x)
        d_y = abs(d_y)
        return (d_x == 1 and d_y == 2) or (d_x == 2 and d_y == 1)

    def __str__(self):
        return '\u2658' if self.color == Color.WHITE else '\u265E'
