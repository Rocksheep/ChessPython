from chess.pieces.piece import Piece


class Knight(Piece):

    def is_valid_move(self, move):
        col = ord(self.coordinates[0]) - ord('a')
        row = int(self.coordinates[1]) - 1

        target_col = ord(move[0]) - ord('a')
        target_row = int(move[1]) - 1

        d_x = target_col - col
        d_y = target_row - row

        if d_x == 0 or d_y == 0:
            return False

        if (d_x / d_y == 0.5 and d_y / d_x == 2) or (d_x / d_y == 2 and d_y / d_x == 0.5):
            return True

        return False
