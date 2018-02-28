class Tile:

    def __init__(self, piece):
        self._piece = piece

    @property
    def piece(self):
        return self._piece

    @piece.setter
    def piece(self, piece):
        self._piece = piece

    def is_empty(self):
        return self._piece is None

    def is_not_empty(self):
        return self._piece is not None
