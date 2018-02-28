
class Piece:

    def __init__(self, color):
        self.color = color

    def is_valid_move(self, origin, destination):
        """
        Do a check to see if the move can be done according to
        the piece's rules
        :param origin:
        :param destination:
        """
        raise NotImplementedError("Please implement this method")

    def _distance_between_coordinates(self, origin, destination):
        col = ord(origin[0]) - ord('a')
        row = int(origin[1]) - 1

        target_col = ord(destination[0]) - ord('a')
        target_row = int(destination[1]) - 1

        d_x = abs(target_col - col)
        d_y = abs(target_row - row)

        return d_x, d_y
