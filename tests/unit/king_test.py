import unittest

from chess.pieces.king import King
from chess.player.color import Color


class KingTest(unittest.TestCase):

    def test_it_can_be_instantiated(self):
        king = King(Color.BLACK)
        self.assertIsInstance(king, King)

    def test_it_can_validate_moves(self):
        king = King(Color.BLACK)
        self.assertTrue(king.is_valid_move('c4', 'c5'))
        self.assertTrue(king.is_valid_move('c4', 'd5'))
        self.assertTrue(king.is_valid_move('c4', 'd4'))
        self.assertTrue(king.is_valid_move('c4', 'd3'))
        self.assertTrue(king.is_valid_move('c4', 'c3'))
        self.assertTrue(king.is_valid_move('c4', 'b3'))
        self.assertTrue(king.is_valid_move('c4', 'b4'))
        self.assertTrue(king.is_valid_move('c4', 'b5'))
        self.assertFalse(king.is_valid_move('c4', 'a6'))
        self.assertFalse(king.is_valid_move('c4', 'h8'))
        self.assertFalse(king.is_valid_move('c4', 'a8'))
        self.assertFalse(king.is_valid_move('c4', 'h1'))
        self.assertFalse(king.is_valid_move('c4', 'b8'))
        self.assertFalse(king.is_valid_move('c4', 'h2'))
        self.assertFalse(king.is_valid_move('c4', "c2"))

    def test_it_has_the_proper_strong_representation_for_its_color(self):
        b_king = King(Color.BLACK)
        self.assertEqual(str(b_king), '\u265A')
        w_king = King(Color.WHITE)
        self.assertEqual(str(w_king), '\u2654')
