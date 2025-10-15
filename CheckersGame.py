# Checkers Game - CS 162 Project
# Author: Noddy Lam
# GitHub username: lamn5
# Date: 03/19/2023
# Description: The program contains a Checkers game that takes two players and allows them to play the game.

class OutofTurn(Exception):
    """Error raised when a player attempts to move out of turn"""
    pass


class InvalidSquareError(Exception):
    """Error raised when a player does not own the square or the location does not exist"""
    pass


class InvalidPlayer(Exception):
    """Error raised when a player's name is invalid"""
    pass


class Checkers:
    """
    Checkers class to represent the checkers game which contains two players. Player with black checkers always start first. Contains methods that return the number of captured pieces, name of winner, and details of a particular square. Uses the Player class to store information about the player and its pieces.
    """

    def __init__(self):
        """
        Constructor for Checkers class. Takes no parameters. Initializes the board with the checkers in the correct positions. All data members are private.
        """
        self._board = [[None, "White", None, "White", None, "White", None, "White"],
                       ["White", None, "White", None, "White", None, "White", None],
                       [None, "White", None, "White", None, "White", None, "White"],
                       [None, None, None, None, None, None, None, None],
                       [None, None, None, None, None, None, None, None],
                       ["Black", None, "Black", None, "Black", None, "Black", None],
                       [None, "Black", None, "Black", None, "Black", None, "Black"],
                       ["Black", None, "Black", None, "Black", None, "Black", None]]
        self._previous_player = None
        self._players = {}
        self._captured_pieces_dict = {}
        self._king_count_dict = {}
        self._triple_king_count_dict = {}
        self._winner = None

    def create_player(self, player_name, piece_color):
        """
        Takes two parameters:
        player_name - represents the name of the player in the player object
        piece_color - represents the color of the checker piece, either "Black" or "White"

        Purpose of this method is to create a player object so the checkers game can begin

        Returns the player object
        """
        self._player_name = player_name
        self._piece_color = piece_color
        self._players[self._player_name] = self._piece_color
        self._captured_pieces_dict[player_name] = 0
        self._king_count_dict[player_name] = 0
        self._triple_king_count_dict[player_name] = 0
        return Player(self._player_name, self._piece_color, self)

    def play_game(self, player_name, starting_square_location, destination_square_location):
        """
        Takes three parameters:
        player_name - represents the name of the player in the player object
        starting_square_location - the square location at the start of turn, represented by a tuple (x,y)
        destination_square_location - the square location at the end of turn, represented by a tuple (x,y)

        Purpose of this method is to let the player choose where to move their checker piece so the game can be played.

        Returns the number of captured pieces.
        """

        # if player name is not valid, raise error
        for name in self._players:
            if player_name not in self._players:
                raise InvalidPlayer
        # if the previous player is same as player now, raise error
        if self.get_previous_player() == player_name:
            raise OutofTurn
        self.set_previous_player(player_name)

        # if the players piece color does not equal to its starting square location, raise error
        if self._players[player_name] != self.get_checker_details(starting_square_location):
            raise InvalidSquareError
        # if there is something at destination then raise error
        if self.get_checker_details(destination_square_location) != None:
            raise InvalidSquareError
        # if square location doesn't exist, raise error
        start_row_num = int(starting_square_location[0])
        start_col_num = int(starting_square_location[1])
        if start_row_num > len(self._board) - 1 or start_col_num > len(self._board) - 1:
            raise InvalidSquareError
        end_row_num = int(destination_square_location[0])
        end_col_num = int(destination_square_location[1])
        if end_row_num > len(self._board) - 1 or end_col_num > len(self._board) - 1:
            raise InvalidSquareError

        self._board[start_row_num][start_col_num] = None
        self._board[end_row_num][end_col_num] = self._players[player_name]

        if self._players[player_name] == "Black":
            if start_row_num - end_row_num == 2:  # if the piece skipped a row
                if start_col_num - end_col_num == 2:  # left side
                    self._board[start_row_num - 1][start_col_num - 1] = None
                    self._captured_pieces_dict[player_name] += 1
                if start_col_num - end_col_num == - 2:  # right side
                    self._board[start_row_num - 1][start_col_num + 1] = None
                    self._captured_pieces_dict[player_name] += 1
            if end_row_num == 0:        # Turns into king
                self._king_count_dict[player_name] += 1
            if end_row_num == 7:            # Turns into triple king
                self._triple_king_count_dict[player_name] += 1

        if self._players[player_name] == "White":
            if start_row_num - end_row_num == -2:  # if the piece skipped a row
                if start_col_num - end_col_num == -2:  # left side
                    self._board[start_row_num + 1][start_col_num + 1] = None
                    self._captured_pieces_dict[player_name] += 1
                if start_col_num - end_col_num == 2:  # right side
                    self._board[start_row_num + 1][start_col_num - 1] = None
                    self._captured_pieces_dict[player_name] += 1
            if end_row_num == 7:            # Turns into king
                self._king_count_dict[player_name] += 1
            if end_row_num == 0:            # Turns into triple king
                self._triple_king_count_dict[player_name] += 1

        if self._captured_pieces_dict[player_name] == 12:
            self._winner = player_name

        return self._captured_pieces_dict[player_name]

    def set_previous_player(self, player_name):
        self._previous_player = player_name

    def get_previous_player(self):
        return self._previous_player

    def get_checker_details(self, square_location):
        """
        Takes one parameter:
        square_location - represents the location that the player want to check

        Purpose of this method is to get the details of the location.

        Returns what piece is at the square location.
        """
        # ! NEED TO FIX
        row_num = int(square_location[0])
        col_num = int(square_location[1])
        if row_num > len(self._board) - 1 or col_num > len(self._board) - 1:
            raise InvalidSquareError
        else:
            return self._board[row_num][col_num]

    def get_player_name(self, player_object):
        return player_object._player_name

    def get_piece_color(self, player_object):
        return player_object._piece_color

    def print_board(self):
        """
        Prints out the current board as a form of array.
        Purpose of this method is to see what the board looks like at the moment.
        """
        for row in self._board:
            print(row)

    def game_winner(self):
        """
        Represents the game winner of the checkers game.
        Returns the name of player who has won the game.
        """
        if self._winner == None:
            return "Game has not ended"
        else:
            return self._winner


class Player:
    """
    Player class to represent each player that is playing the game. Contains information such as the player's name and its piece color. Used by the Checkers class.
    """

    def __init__(self, player_name, piece_color, game):
        """
        Constructor for Player class. Takes no parameters. Initializes the player's name and piece color. All data members are private.
        """
        self._player_name = player_name
        self._piece_color = piece_color
        self._game = game

    def get_king_count(self):
        """
        Gets total amount of king pieces that the player have on the board. 
        """
        return self._game._king_count_dict[self._player_name]

    def get_triple_king_count(self):
        """
        Gets total amount of triple king pieces that the player have on the board.
        """
        return self._game._triple_king_count_dict[self._player_name]

    def get_captured_pieces_count(self):
        """
        Gets total amount of captured pieces that the player have done.
        """
        return self._game._captured_pieces_dict[self._player_name]


game = Checkers()
Player1 = game.create_player("Noddy", "Black")
Player2 = game.create_player("Bob", "White")
name1 = game.get_player_name(Player1)
name2 = game.get_player_name(Player2)
print(f"Player names: {name1}, {name2}")
# game.print_board()
# game.get_checker_details((3, 1))

# Player1.get_king_count()
# Player1.get_triple_king_count()
captured_pieces = Player1.get_captured_pieces_count()
print(captured_pieces)
king_count = Player1.get_king_count()
print(king_count)
