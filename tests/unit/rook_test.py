import unittest

from chess.pieces.rook import Rook
from chess.player.color import Color


class RookTest(unittest.TestCase):

    def test_it_can_be_instantiated(self):
        piece = Rook(Color.BLACK)
        self.assertIsInstance(piece, Rook)

    def test_it_validates_the_move(self):
        piece = Rook(Color.BLACK)

        self.assertTrue(piece.is_valid_move('c4', 'c8'))
        self.assertTrue(piece.is_valid_move('c4', 'f4'))
        self.assertTrue(piece.is_valid_move('c4', 'c1'))
        self.assertTrue(piece.is_valid_move('c4', 'a4'))
        self.assertFalse(piece.is_valid_move('c4', 'a2'))
        self.assertFalse(piece.is_valid_move('c4', 'h2'))
