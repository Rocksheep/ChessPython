import unittest

from chess.pieces.rook import Rook


class RookTest(unittest.TestCase):

    def test_it_can_be_instantiated(self):
        piece = Rook('A1')
        self.assertIsInstance(piece, Rook)

    def test_it_validates_the_move(self):
        piece = Rook('A1')

        self.assertTrue(piece.is_valid_move('A8'))
        self.assertFalse(piece.is_valid_move('B8'))
        self.assertTrue(piece.is_valid_move('H1'))
        self.assertFalse(piece.is_valid_move('H2'))
