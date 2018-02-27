
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
