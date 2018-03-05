from chess.pieces.piece import Piece


class Queen(Piece):

    def is_valid_move(self, origin, destination):
        d_x, d_y = self._distance_between_coordinates(origin, destination)

        d_x = abs(d_x)
        d_y = abs(d_y)

        return d_x == d_y or min(d_x, d_y) == 0

    def __str__(self):
        return '\u2655' if self.color == 'white' else '\u265B'
