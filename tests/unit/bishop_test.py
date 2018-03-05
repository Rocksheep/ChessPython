import unittest

from chess.pieces.bishop import Bishop
from chess.player.color import Color


class BishopTest(unittest.TestCase):

    def test_it_can_be_initialised(self):
        bishop = Bishop(Color.BLACK)
        self.assertIsInstance(bishop, Bishop)

    def test_it_validates_the_move(self):
        bishop = Bishop(Color.BLACK)
        self.assertTrue(bishop.is_valid_move('c4', 'f7'))
        self.assertTrue(bishop.is_valid_move('c4', 'e2'))
        self.assertTrue(bishop.is_valid_move('c4', 'b3'))
        self.assertTrue(bishop.is_valid_move('c4', 'a6'))
        self.assertFalse(bishop.is_valid_move('c4', 'd4'))
        self.assertFalse(bishop.is_valid_move('c4', 'c7'))
        self.assertFalse(bishop.is_valid_move('c4', 'a4'))
        self.assertFalse(bishop.is_valid_move('c4', 'c1'))
