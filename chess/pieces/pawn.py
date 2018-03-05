from chess.pieces.piece import Piece


class Pawn(Piece):

    def is_valid_move(self, origin, destination):
        d_x, d_y = self._distance_between_coordinates(origin, destination)

        if origin is 'b7':
            return 1 <= d_y <= 2 and abs(d_x) == 0

        if self.color == 'black':
            return d_y == 1 and abs(d_x) == 0
        return d_y == -1 and abs(d_x) == 0

    def __str__(self):
        return '\u2659' if self.color == 'white' else '\u265F'
