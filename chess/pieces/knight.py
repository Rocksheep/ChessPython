from chess.pieces.piece import Piece


class Knight(Piece):

    def is_valid_move(self, origin, destination):
        col = ord(origin[0]) - ord('a')
        row = int(origin[1]) - 1

        target_col = ord(destination[0]) - ord('a')
        target_row = int(destination[1]) - 1

        d_x = abs(target_col - col)
        d_y = abs(target_row - row)

        if (d_x == 1 and d_y == 2) or (d_x == 2 and d_y == 1):
            return True

        return False

    def __str__(self):
        return '\u2658' if self.color == 'white' else '\u265E'
