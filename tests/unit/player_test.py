import unittest

from chess.player.color import Color
from chess.player.player import Player


class PlayerTest(unittest.TestCase):

    def test_it_can_be_instantiated(self):
        player = Player(Color.WHITE)
        self.assertIsInstance(player, Player)
