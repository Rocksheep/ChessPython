import unittest

from chess.pieces.rook import Rook


class RookTest(unittest.TestCase):

    def test_it_can_be_instantiated(self):
        piece = Rook('black')
        self.assertIsInstance(piece, Rook)

    def test_it_validates_the_move(self):
        piece = Rook('black')

        self.assertTrue(piece.is_valid_move('a1', 'a8'))
        self.assertFalse(piece.is_valid_move('a1', 'b8'))
        self.assertTrue(piece.is_valid_move('a1', 'h1'))
        self.assertFalse(piece.is_valid_move('a1', 'h2'))
