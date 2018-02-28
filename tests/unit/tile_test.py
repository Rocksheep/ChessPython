import unittest

from chess.Tile import Tile
from chess.pieces.rook import Rook


class TileTest(unittest.TestCase):

    def test_it_can_be_instantiated(self):
        tile = Tile(None)
        self.assertIsInstance(tile, Tile)

    def test_it_can_be_empty(self):
        tile = Tile(None)
        self.assertTrue(tile.is_empty())
        self.assertFalse(tile.is_not_empty())

    def test_it_can_be_occupied(self):
        tile = Tile(Rook('white'))
        self.assertTrue(tile.is_not_empty())
        self.assertFalse(tile.is_empty())
