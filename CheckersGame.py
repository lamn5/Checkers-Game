# portfolio-project
# Author: Noddy Lam
# GitHub username: lamn5
# Date: 03/19/2023
# Description: 

class OutofTurnError(Exception):
    """Error raised when a player attempts to move out of turn"""
    pass

class InvalidSquareError(Exception):
    """Error raised when a player does not own the square or the location does not exist"""
    pass

class InvalidPlayerError(Exception):
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
                       ["White", None, "White", None, "White", None, "White", None,],
                       [None, "White", None, "White", None, "White", None, "White"],
                       [None, None, None, None, None, None, None, None],
                       [None, None, None, None, None, None, None, None],
                       ["Black", None, "Black", None, "Black", None, "Black", None],
                       [None, "Black", None, "Black", None, "Black", None, "Black"],
                       ["Black", None, "Black", None, "Black", None, "Black", None]]

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
        return Player()
        

    def play_game(self, player_name, starting_square_location, destination_square_location):
        """
        Takes three parameters:
        player_name - represents the name of the player in the player object
        starting_square_location - the square location at the start of turn, represented by a tuple (x,y)
        destination_square_location - the square location at the end of turn, represented by a tuple (x,y)

        Purpose of this method is to let the player choose where to move their checker piece so the game can be played.

        Returns the number of captured pieces.
        """
        pass

    def get_checker_details(self, square_location):
        """
        Takes one parameter:
        square_location - represents the location that the player want to check

        Purpose of this method is to get the details of the location.

        Returns what piece is at the square location.
        """
        row_num = int(square_location[0])
        col_num = int(square_location[1])
        if row_num > len(self._board) - 1 or col_num > len(self._board) - 1:
            raise InvalidSquareError
        else:
            return self._board[row_num][col_num]
        
        

    def print_board(self):
        """
        Prints out the current board as a form of array.
        Purpose of this method is to see what the board looks like at the moment.
        """
        print(self._board)
        return 

    def game_winner(self):
        """
        Represents the game winner of the checkers game.
        Returns the name of player who has won the game.
        """
        pass

class Player:
    """
    Player class to represent each player that is playing the game. Contains information such as the player's name and its piece color. Used by the Checkers class.
    """
    def __init_(self):
        """
        Constructor for Player class. Takes no parameters. Initializes the player's name and piece color. All data members are private.
        """
        # self._player = [self._player_name, self._piece_color]
        self._player_name = ()
        self._piece_color = ()


    def get_player_name(self):
        return self._player_name
    
    def get_piece_color(self):
        return self._piece_color
    
    def get_king_count(self):
        """
        Gets total amount of king pieces that the player have on the board. 
        """
        pass

    def get_triple_king_count(self):
        """
        Gets total amount of triple king pieces that the player have on the board. 
        """
        pass

    def captured_pieces_count(self):
        """
        Gets total amount of captured pieces that the player have done. 
        """
        pass


if __name__ == '__main__':

    game = Checkers()
    game.print_board()
    Player1 = game.create_player("Adam", "White")
    print(Player1)
    print(game.get_checker_details((1,6)))