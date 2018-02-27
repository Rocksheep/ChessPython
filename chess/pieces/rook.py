from chess.pieces.piece import Piece


class Rook(Piece):

    def is_valid_move(self, origin, destination):
        col = ord(origin[0]) - ord('A')
        row = int(origin[1]) - 1

        target_col = ord(destination[0]) - ord('A')
        target_row = int(destination[1]) - 1

        if row == target_row or col == target_col:
            return True

        return False

    def __str__(self):
        return '\u2656' if self.color == 'white' else '\u265C'
