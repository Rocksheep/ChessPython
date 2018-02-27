import unittest

from chess.pieces.knight import Knight


class KnightTest(unittest.TestCase):

    def test_it_can_be_instantiated(self):
        knight = Knight('black')
        self.assertIsInstance(knight, Knight)

    def test_it_can_validate_moves(self):
        knight = Knight('black')
        self.assertTrue(knight.is_valid_move('a1', 'c2'))
        self.assertTrue(knight.is_valid_move('a1', 'b3'))
        self.assertFalse(knight.is_valid_move('a1', 'b2'))
        self.assertFalse(knight.is_valid_move('a1', 'b1'))
        self.assertFalse(knight.is_valid_move('a1', 'a2'))
        self.assertFalse(knight.is_valid_move('a1', 'a3'))