import unittest

from chess.board import Board


class BoardTest(unittest.TestCase):

    def test_it_can_create_an_instance(self):
        board = Board()
        self.assertIsInstance(board, Board)

    def test_it_returns_a_piece_by_coordinates(self):
        board = Board()
        piece = board.squares[0][0]
        retrieved_piece = board.get_piece_on_coordinates('a8')

        self.assertEqual(piece, retrieved_piece)

        piece = board.squares[0][1]
        retrieved_piece = board.get_piece_on_coordinates('b8')
        self.assertEqual(piece, retrieved_piece)

        self.assertIsNone(board.get_piece_on_coordinates('c5'))
