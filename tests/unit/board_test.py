import unittest

from chess.board import Board


class BoardTest(unittest.TestCase):

    def test_it_can_create_an_instance(self):
        board = Board()
        self.assertIsInstance(board, Board)
