import unittest

from chess.pieces.knight import Knight


class KnightTest(unittest.TestCase):

    def test_it_can_be_instantiated(self):
        knight = Knight("A1")
        self.assertIsInstance(knight, Knight)

    def test_it_can_validate_moves(self):
        knight = Knight("A1")
        self.assertTrue(knight.is_valid_move("C2"))
        self.assertTrue(knight.is_valid_move("B3"))
        self.assertFalse(knight.is_valid_move("B2"))
        self.assertFalse(knight.is_valid_move("B1"))
        self.assertFalse(knight.is_valid_move("A2"))
        self.assertFalse(knight.is_valid_move("A3"))