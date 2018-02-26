import unittest

from chess.pieces.bishop import Bishop


class BishopTest(unittest.TestCase):

    def test_it_can_be_initialised(self):
        bishop = Bishop('a1')
        self.assertIsInstance(bishop, Bishop)

    def test_it_validates_the_move(self):
        bishop = Bishop('a1')
        self.assertTrue(bishop.is_valid_move('h8'))
        self.assertFalse(bishop.is_valid_move('d5'))
        pass