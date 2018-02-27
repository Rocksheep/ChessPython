from chess.pieces.piece import Piece


class Queen(Piece):

    def is_valid_move(self, origin, destination):
        col = ord(origin[0]) - ord('a')
        row = int(origin[1]) - 1

        target_col = ord(destination[0]) - ord('a')
        target_row = int(destination[1]) - 1

        d_x = target_col - col
        d_y = target_row - row

        if d_x == 0 or d_y == 0:
            return True

        return abs(d_x) == abs(d_y)

    def __str__(self):
        return '\u2655' if self.color == 'white' else '\u265B'
