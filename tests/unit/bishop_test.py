import unittest

from chess.pieces.bishop import Bishop


class BishopTest(unittest.TestCase):

    def test_it_can_be_initialised(self):
        bishop = Bishop('black')
        self.assertIsInstance(bishop, Bishop)

    def test_it_validates_the_move(self):
        bishop = Bishop('black')
        self.assertTrue(bishop.is_valid_move('a1', 'h8'))
        self.assertFalse(bishop.is_valid_move('a1', 'd5'))
