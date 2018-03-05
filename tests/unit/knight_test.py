import unittest

from chess.pieces.knight import Knight
from chess.player.color import Color


class KnightTest(unittest.TestCase):

    def test_it_can_be_instantiated(self):
        knight = Knight(Color.BLACK)
        self.assertIsInstance(knight, Knight)

    def test_it_can_validate_moves(self):
        knight = Knight(Color.BLACK)
        self.assertTrue(knight.is_valid_move('c4', 'd6'))
        self.assertTrue(knight.is_valid_move('c4', 'e5'))
        self.assertTrue(knight.is_valid_move('c4', 'e3'))
        self.assertTrue(knight.is_valid_move('c4', 'd2'))
        self.assertTrue(knight.is_valid_move('c4', 'b2'))
        self.assertTrue(knight.is_valid_move('c4', 'a3'))
        self.assertTrue(knight.is_valid_move('c4', 'a5'))
        self.assertTrue(knight.is_valid_move('c4', 'b6'))
        self.assertFalse(knight.is_valid_move('c4', 'b1'))
        self.assertFalse(knight.is_valid_move('c4', 'a2'))
        self.assertFalse(knight.is_valid_move('c4', 'a4'))
        self.assertFalse(knight.is_valid_move('c4', 'g6'))

    def test_it_has_the_proper_strong_representation_for_its_color(self):
        b_knight = Knight(Color.BLACK)
        self.assertEqual(str(b_knight), '\u265E')
        w_knight = Knight(Color.WHITE)
        self.assertEqual(str(w_knight), '\u2658')
