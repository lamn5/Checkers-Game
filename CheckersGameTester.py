import unittest
from CheckersGame import Checkers, Player, InvalidSquareError

class TestCheckersGame(unittest.TestCase):

    def test_1(self):
        game = Checkers()
        self.assertIs(game.print_board(),None)

    def test_checker_details_returns_white_successfully(self):
        """tests that the get_checker_details function returns the correct piece detail at the correct location"""
        game = Checkers()
        self.assertEqual(game.get_checker_details((1,6)), 'White')
    
    def test_invalid_square_raises_successfully(self):
        """tests to verify InvalidSquareError is raised"""
        game = Checkers()
        with self.assertRaises(InvalidSquareError):
            game.get_checker_details((8,6))



if __name__ == '__main__':
    unittest.main()