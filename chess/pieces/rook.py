from chess.pieces.piece import Piece


class Rook(Piece):

    def is_valid_move(self, origin, destination):
        d_x, d_y = self._distance_between_coordinates(origin, destination)

        return min(d_x, d_y) == 0

    def __str__(self):
        return '\u2656' if self.color == 'white' else '\u265C'
