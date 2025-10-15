import unittest
from CheckersGame import Checkers, InvalidSquareError, OutofTurn, InvalidPlayer

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
        self.assertEqual(game.get_checker_details((3,0)),"White")

    def test_game_winner(self):
        """tests that the correct game winner is returned"""
        game = Checkers()
        Player1 = game.create_player("Adam", "White")
        Player2 = game.create_player("Lucy", "Black" )
        self.assertEqual(game.game_winner(), "Game has not ended")

    def test_out_of_turn_exception(self):
        """tests that OutofTurn exception is raised when a player moves twice"""
        game = Checkers()
        Player1 = game.create_player("Alice", "Black")
        Player2 = game.create_player("Bob", "White")
        game.play_game("Alice", (5, 0), (4, 1))
        with self.assertRaises(OutofTurn):
            game.play_game("Alice", (5, 2), (4, 3))

    def test_invalid_player_exception(self):
        """tests that InvalidPlayer exception is raised for non-existent player"""
        game = Checkers()
        Player1 = game.create_player("Alice", "Black")
        with self.assertRaises(InvalidPlayer):
            game.play_game("Charlie", (5, 0), (4, 1))

    def test_black_player_moves_first(self):
        """tests that Black player can move first"""
        game = Checkers()
        Player1 = game.create_player("Alice", "Black")
        Player2 = game.create_player("Bob", "White")
        captured = game.play_game("Alice", (5, 0), (4, 1))
        self.assertEqual(captured, 0)
        self.assertEqual(game.get_checker_details((4, 1)), "Black")

    def test_capture_piece_successfully(self):
        """tests that a piece can be captured and removed from board"""
        game = Checkers()
        Player1 = game.create_player("Alice", "Black")
        Player2 = game.create_player("Bob", "White")
        game.play_game("Alice", (5, 0), (4, 1))
        game.play_game("Bob", (2, 3), (3, 2))
        captured = game.play_game("Alice", (4, 1), (2, 3))
        self.assertEqual(captured, 1)
        self.assertIsNone(game.get_checker_details((3, 2)))

    def test_captured_pieces_count(self):
        """tests that player's captured pieces count is tracked correctly"""
        game = Checkers()
        Player1 = game.create_player("Alice", "Black")
        Player2 = game.create_player("Bob", "White")
        game.play_game("Alice", (5, 0), (4, 1))
        game.play_game("Bob", (2, 3), (3, 2))
        game.play_game("Alice", (4, 1), (2, 3))
        self.assertEqual(Player1.get_captured_pieces_count(), 1)
        self.assertEqual(Player2.get_captured_pieces_count(), 0)

    def test_black_becomes_king_at_row_zero(self):
        """tests that Black piece becomes a king when reaching row 0"""
        game = Checkers()
        Player1 = game.create_player("Alice", "Black")
        Player2 = game.create_player("Bob", "White")
        # Manually place Black piece near row 0
        game._board[1][0] = "Black"
        game._board[0][1] = None
        game.play_game("Alice", (1, 0), (0, 1))
        self.assertEqual(game.get_checker_details((0, 1)), "Black_king")
        self.assertEqual(Player1.get_king_count(), 1)

    def test_white_becomes_king_at_row_seven(self):
        """tests that White piece becomes a king when reaching row 7"""
        game = Checkers()
        Player1 = game.create_player("Bob", "White")
        Player2 = game.create_player("Alice", "Black")
        # Manually place White piece near row 7
        game._board[6][0] = "White"
        game._board[7][1] = None
        game.play_game("Bob", (6, 0), (7, 1))
        self.assertEqual(game.get_checker_details((7, 1)), "White_king")
        self.assertEqual(Player1.get_king_count(), 1)

    def test_black_becomes_triple_king_at_row_seven(self):
        """tests that Black piece becomes triple king when reaching row 7"""
        game = Checkers()
        Player1 = game.create_player("Alice", "Black")
        Player2 = game.create_player("Bob", "White")
        # Manually place Black piece near row 7
        game._board[6][2] = "Black"
        game._board[7][3] = None
        game.play_game("Alice", (6, 2), (7, 3))
        self.assertEqual(game.get_checker_details((7, 3)), "Black_Triple_King")
        self.assertEqual(Player1.get_triple_king_count(), 1)

    def test_white_becomes_triple_king_at_row_zero(self):
        """tests that White piece becomes triple king when reaching row 0"""
        game = Checkers()
        Player1 = game.create_player("Bob", "White")
        Player2 = game.create_player("Alice", "Black")
        # Manually place White piece near row 0
        game._board[1][2] = "White"
        game._board[0][3] = None
        game.play_game("Bob", (1, 2), (0, 3))
        self.assertEqual(game.get_checker_details((0, 3)), "White_Triple_King")
        self.assertEqual(Player1.get_triple_king_count(), 1)

    def test_king_piece_can_move(self):
        """tests that a king piece can still move after promotion"""
        game = Checkers()
        Player1 = game.create_player("Alice", "Black")
        Player2 = game.create_player("Bob", "White")
        # Create a king manually
        game._board[0][1] = "Black_king"
        game._board[1][0] = None
        game.play_game("Alice", (0, 1), (1, 0))
        self.assertEqual(game.get_checker_details((1, 0)), "Black_king")

    def test_empty_square_returns_none(self):
        """tests that get_checker_details returns None for empty squares"""
        game = Checkers()
        self.assertIsNone(game.get_checker_details((3, 3)))
        self.assertIsNone(game.get_checker_details((4, 4)))

    def test_winner_declared_after_12_captures(self):
        """tests that winner is declared when player captures 12 pieces"""
        game = Checkers()
        Player1 = game.create_player("Alice", "Black")
        Player2 = game.create_player("Bob", "White")
        # Manually set captured pieces to 12
        game._captured_pieces_dict["Alice"] = 12
        game._winner = "Alice"
        self.assertEqual(game.game_winner(), "Alice")

    def test_invalid_square_out_of_bounds(self):
        """tests that InvalidSquareError is raised for out of bounds coordinates"""
        game = Checkers()
        Player1 = game.create_player("Alice", "Black")
        with self.assertRaises(InvalidSquareError):
            game.play_game("Alice", (5, 0), (10, 10))

    def test_moving_empty_square_raises_error(self):
        """tests that InvalidSquareError is raised when trying to move from empty square"""
        game = Checkers()
        Player1 = game.create_player("Alice", "Black")
        with self.assertRaises(InvalidSquareError):
            game.play_game("Alice", (3, 3), (4, 4))

    def test_moving_opponent_piece_raises_error(self):
        """tests that InvalidSquareError is raised when trying to move opponent's piece"""
        game = Checkers()
        Player1 = game.create_player("Alice", "Black")
        Player2 = game.create_player("Bob", "White")
        with self.assertRaises(InvalidSquareError):
            game.play_game("Alice", (2, 1), (3, 0))

    def test_moving_to_occupied_square_raises_error(self):
        """tests that InvalidSquareError is raised when destination is occupied"""
        game = Checkers()
        Player1 = game.create_player("Alice", "Black")
        Player2 = game.create_player("Bob", "White")
        with self.assertRaises(InvalidSquareError):
            game.play_game("Alice", (5, 0), (6, 1))

    def test_get_player_name(self):
        """tests that get_player_name returns correct player name"""
        game = Checkers()
        Player1 = game.create_player("Alice", "Black")
        self.assertEqual(game.get_player_name(Player1), "Alice")

    def test_get_piece_color(self):
        """tests that get_piece_color returns correct piece color"""
        game = Checkers()
        Player1 = game.create_player("Alice", "Black")
        self.assertEqual(game.get_piece_color(Player1), "Black")

if __name__ == '__main__':
    unittest.main()