import unittest

from chess.pieces.king import King


class KingTest(unittest.TestCase):

    def test_it_can_be_instantiated(self):
        king = King('black')
        self.assertIsInstance(king, King)

    def test_it_can_validate_moves(self):
        king = King('black')
        self.assertTrue(king.is_valid_move('a1', 'a2'))
        self.assertTrue(king.is_valid_move('a1', 'b1'))
        self.assertTrue(king.is_valid_move('a1', 'b2'))
        self.assertFalse(king.is_valid_move('a1', 'h8'))
        self.assertFalse(king.is_valid_move('a1', 'a8'))
        self.assertFalse(king.is_valid_move('a1', 'h1'))
        self.assertFalse(king.is_valid_move('a1', 'd5'))
        self.assertFalse(king.is_valid_move('a1', 'b8'))
        self.assertFalse(king.is_valid_move('a1', 'h2'))
        self.assertFalse(king.is_valid_move('a1', "c2"))