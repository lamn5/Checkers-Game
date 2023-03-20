import unittest
from CheckersGame import Checkers, Player

class TestCheckersGame(unittest.TestCase):

    def test_1(self):
        game = Checkers()
        self.assertIs(game.print_board(),None)

    def test_checker_details_returns_white_successfully(self):
        """tests that the get_checker_details function returns the correct piece detail at the correct location"""
        game = Checkers()
        self.assertEqual(game.get_checker_details((1,6)), 'White')


if __name__ == '__main__':
    unittest.main()