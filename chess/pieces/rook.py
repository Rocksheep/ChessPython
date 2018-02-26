from chess.pieces.piece import Piece


class Rook(Piece):

    def is_valid_move(self, move):
        col = ord(self.coordinates[0]) - ord('A')
        row = int(self.coordinates[1]) - 1

        target_col = ord(move[0]) - ord('A')
        target_row = int(move[1]) - 1

        if row == target_row or col == target_col:
            return True

        return False
