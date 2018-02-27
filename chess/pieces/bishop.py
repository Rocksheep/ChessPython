import math

from chess.pieces.piece import Piece


class Bishop(Piece):

    def is_valid_move(self, origin, destination):
        col = ord(origin[0]) - ord('a')
        row = int(origin[1]) - 1

        target_col = ord(destination[0]) - ord('a')
        target_row = int(destination[1]) - 1

        d_x = abs(target_col - col)
        d_y = abs(target_row - row)

        return d_x == d_y

    def __str__(self):
        return '\u2657' if self.color == 'white' else '\u265D'
