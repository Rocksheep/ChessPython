from chess.pieces.piece import Piece


class King(Piece):

    def is_valid_move(self, origin, destination):
        d_x, d_y = self._distance_between_coordinates(origin, destination)

        return max(d_x, d_y) == 1

    def __str__(self):
        return '\u2654' if self.color == 'white' else '\u265A'
