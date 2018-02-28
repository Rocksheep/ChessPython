from chess.pieces.piece import Piece


class Knight(Piece):

    def is_valid_move(self, origin, destination):
        d_x, d_y = self._distance_between_coordinates(origin, destination)

        if (d_x == 1 and d_y == 2) or (d_x == 2 and d_y == 1):
            return True

        return False

    def __str__(self):
        return '\u2658' if self.color == 'white' else '\u265E'
