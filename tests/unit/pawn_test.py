import unittest

from chess.pieces.pawn import Pawn
from chess.pieces.piece import Piece


class PawnTest(unittest.TestCase):

    def test_it_can_be_instantiated(self):
        pawn = Pawn('black')
        self.assertIsInstance(pawn, Pawn)

    def test_it_can_validate_moves(self):
        b_pawn = Pawn('black')
        self.assertTrue(b_pawn.is_valid_move('b7', 'b6'))
        self.assertTrue(b_pawn.is_valid_move('b7', 'b5'))
        self.assertFalse(b_pawn.is_valid_move('b7', 'b4'))
        self.assertFalse(b_pawn.is_valid_move('b6', 'b4'))
        self.assertFalse(b_pawn.is_valid_move('b7', 'b1'))
        self.assertFalse(b_pawn.is_valid_move('a7', 'b1'))
        self.assertFalse(b_pawn.is_valid_move('b7', 'a8'))
        self.assertFalse(b_pawn.is_valid_move('b7', 'b8'))
        self.assertFalse(b_pawn.is_valid_move('b7', 'c8'))
        self.assertFalse(b_pawn.is_valid_move('b7', 'c7'))

        w_pawn = Pawn('white')
        self.assertTrue(True)