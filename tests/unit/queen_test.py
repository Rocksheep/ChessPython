import unittest

from chess.pieces.queen import Queen


class QueenTest(unittest.TestCase):

    def test_it_can_be_instantiated(self):
        queen = Queen('black')
        self.assertIsInstance(queen, Queen)

    def test_it_can_validate_moves(self):
        queen = Queen('black')
        self.assertTrue(queen.is_valid_move('a1', 'h8'))
        self.assertTrue(queen.is_valid_move('a1', 'a8'))
        self.assertTrue(queen.is_valid_move('a1', 'h1'))
        self.assertFalse(queen.is_valid_move('a1', 'd5'))
        self.assertFalse(queen.is_valid_move('a1', 'b8'))
        self.assertFalse(queen.is_valid_move('a1', 'h2'))
        self.assertFalse(queen.is_valid_move('a1', 'c2'))
