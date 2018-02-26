from chess.pieces.piece import Piece


class Knight(Piece):

    def is_valid_move(self, move):
        col = ord(self.coordinates[0]) - ord('a')
        row = int(self.coordinates[1]) - 1

        target_col = ord(move[0]) - ord('a')
        target_row = int(move[1]) - 1

        d_x = abs(target_col - col)
        d_y = abs(target_row - row)

        if (d_x == 1 and d_y == 2) or (d_x == 2 and d_y == 1):
            return True

        return False
