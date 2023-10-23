import unittest
from src.game_logic import game


class GameTest(unittest.TestCase):
    def test_game(self):
        # Scenario 1
        g = game.Game(3, 3)
        self.assertFalse(g.finished)

        g.add_submission(2)
        self.assertFalse(g.finished)
        g.add_submission(2)
        self.assertFalse(g.finished)
        g.add_submission(3)

        self.assertTrue(g.finished)
        self.assertEqual(g.winning_number, 2)

        # Scenario 2
        g = game.Game(3, 3)
        self.assertFalse(g.finished)

        g.add_submission(1)
        self.assertFalse(g.finished)
        g.add_submission(2)
        self.assertFalse(g.finished)
        g.add_submission(3)

        self.assertTrue(g.finished)
        self.assertEqual(g.winning_number, 1)

        # Scenario 3
        g = game.Game(5, 5)
        self.assertFalse(g.finished)

        g.add_submission(1)
        self.assertFalse(g.finished)
        g.add_submission(2)
        self.assertFalse(g.finished)
        g.add_submission(3)
        self.assertFalse(g.finished)
        g.add_submission(4)
        self.assertFalse(g.finished)
        g.add_submission(5)

        self.assertTrue(g.finished)
        self.assertEqual(g.winning_number, 1)

        # Scenario 4
        g = game.Game(5, 5)
        self.assertFalse(g.finished)

        g.add_submission(5)
        self.assertFalse(g.finished)
        g.add_submission(5)
        self.assertFalse(g.finished)
        g.add_submission(3)
        self.assertFalse(g.finished)
        g.add_submission(2)
        self.assertFalse(g.finished)
        g.add_submission(1)

        self.assertTrue(g.finished)
        self.assertEqual(g.winning_number, 5)
