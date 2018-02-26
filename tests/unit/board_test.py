import unittest

from chess.board import Board


class BoardTest(unittest.TestCase):

    def test_it_can_create_an_instance(self):
        board = Board()
        self.assertIsInstance(board, Board)

    def test_it_has_pieces(self):
        board = Board()
        self.assertTrue(board.pieces)
        pass

    def test_it_returns_a_piece_by_coordinates(self):
        board = Board()
        piece = board.pieces[0]
        retrieved_piece = board.get_piece_on_coordinates(piece.coordinates)

        self.assertEqual(piece, retrieved_piece)

        piece = board.pieces[1]
        retrieved_piece = board.get_piece_on_coordinates(piece.coordinates)
        self.assertEqual(piece, retrieved_piece)

