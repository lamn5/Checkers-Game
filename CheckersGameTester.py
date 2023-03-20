import unittest
from CheckersGame import Checkers, Player, InvalidSquareError

class TestCheckersGame(unittest.TestCase):

    def test_print_board_successfully(self):
        """check the the first value of the print board method is None to make sure it's set up properly"""
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

    def test_player_piece_moved_to_destination_successfully(self):
        """tests that the checker piece has moved to its destination correctly"""
        game = Checkers()
        Player1 = game.create_player("Adam", "White")
        game.play_game("Adam", (2,1),(3,0))
        self.assertEqual(game.get_checker_details((3,0)),'White')

    def test_game_winner(self):
        """tests that the correct game winner is returned"""
        

if __name__ == '__main__':
    unittest.main()