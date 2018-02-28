import unittest

from chess.Tile import Tile
from chess.board import Board


class BoardTest(unittest.TestCase):

    def test_it_can_create_an_instance(self):
        board = Board()
        self.assertIsInstance(board, Board)

    def test_it_has_tiles(self):
        board = Board()
        self.assertEqual(len(board.tiles), board.height)
        for row in board.tiles:
            self.assertEqual(len(row), board.width)

        tile = board.tiles[0][0]
        self.assertIsInstance(tile, Tile)

    def test_it_returns_a_piece_by_coordinates(self):
        board = Board()
        piece = board.tiles[0][0].piece
        retrieved_piece = board.get_piece_on_coordinates('a8')

        self.assertEqual(piece, retrieved_piece)

        piece = board.tiles[0][1].piece
        retrieved_piece = board.get_piece_on_coordinates('b8')
        self.assertEqual(piece, retrieved_piece)

        self.assertIsNone(board.get_piece_on_coordinates('c5'))
