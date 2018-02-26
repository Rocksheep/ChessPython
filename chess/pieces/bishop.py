import math

from chess.pieces.piece import Piece


class Bishop(Piece):

    def is_valid_move(self, move):
        col = ord(self.coordinates[0]) - ord('a')
        row = int(self.coordinates[1]) - 1

        target_col = ord(move[0]) - ord('a')
        target_row = int(move[1]) - 1

        d_x = target_col - col
        d_y = target_row - row

        return abs(d_x / d_y) == 1
