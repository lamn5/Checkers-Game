# How to Play Checkers

Welcome to the Checkers Game! This guide will help you understand the rules and how to play.

## Game Overview

Checkers is a two-player strategy board game played on an 8x8 board. One player controls **Black** pieces, and the other controls **White** pieces. The goal is to capture all of your opponent's pieces.

## Setup

The game board is set up with:

-   **White pieces** on rows 0-2 (top of the board)
-   **Black pieces** on rows 5-7 (bottom of the board)
-   Pieces are placed on alternating squares (checkerboard pattern)
-   **Black always moves first**

## Board Coordinates

The board uses coordinate system (row, column) where:

-   Rows and columns are numbered 0-7
-   Example: `(5, 0)` means row 5, column 0
-   Top-left corner is `(0, 0)`
-   Bottom-right corner is `(7, 7)`

```
   0   1   2   3   4   5   6   7
0  -   W   -   W   -   W   -   W
1  W   -   W   -   W   -   W   -
2  -   W   -   W   -   W   -   W
3  -   -   -   -   -   -   -   -
4  -   -   -   -   -   -   -   -
5  B   -   B   -   B   -   B   -
6  -   B   -   B   -   B   -   B
7  B   -   B   -   B   -   B   -

W = White piece
B = Black piece
- = Empty square
```

## Basic Rules

### 1. **Taking Turns**

-   Black player moves first
-   Players alternate turns
-   You cannot move twice in a row

### 2. **Regular Piece Movement**

-   Regular pieces move **diagonally forward** one square
-   Black pieces move toward row 0 (upward)
-   White pieces move toward row 7 (downward)
-   You can only move to empty squares

### 3. **Capturing Pieces**

-   Jump over an opponent's piece diagonally to capture it
-   The jumped piece is removed from the board
-   Captures move 2 rows diagonally (skipping the opponent's piece)
-   You can capture left or right diagonally

**Example Capture:**

```
Black at (4, 1) can capture White at (3, 2) by jumping to (2, 3)
```

### 4. **King Pieces**

When a piece reaches the opposite end of the board:

-   **Black piece reaching row 0** → becomes a **King**
-   **White piece reaching row 7** → becomes a **King**

Kings have special abilities (can move in different directions).

### 5. **Triple King Pieces**

If a piece crosses back to its original side:

-   **Black King reaching row 7** → becomes a **Triple King**
-   **White King reaching row 0** → becomes a **Triple King**

Triple Kings have even more powerful abilities.

### 6. **Winning the Game**

The first player to **capture 12 opponent pieces wins** the game!

## How to Play (Code Example)

### Step 1: Create a Game and Players

```python
from CheckersGame import Checkers

# Create a new game
game = Checkers()

# Create two players
player1 = game.create_player("Alice", "Black")
player2 = game.create_player("Bob", "White")
```

### Step 2: Make Moves

```python
# Black player moves first
# Move piece from (5, 0) to (4, 1)
captured = game.play_game("Alice", (5, 0), (4, 1))
print(f"Alice captured {captured} pieces")

# White player's turn
captured = game.play_game("Bob", (2, 1), (3, 0))
print(f"Bob captured {captured} pieces")
```

### Step 3: View the Board

```python
# Print the current board state
game.print_board()
```

### Step 4: Check Square Details

```python
# Check what's at a specific square
piece = game.get_checker_details((4, 1))
print(f"Square (4,1) has: {piece}")
# Returns: "Black", "White", "Black_king", "White_king",
#          "Black_Triple_King", "White_Triple_King", or None
```

### Step 5: Check Player Statistics

```python
# Get player statistics
captured = player1.get_captured_pieces_count()
kings = player1.get_king_count()
triple_kings = player1.get_triple_king_count()

print(f"Alice has captured {captured} pieces")
print(f"Alice has {kings} kings")
print(f"Alice has {triple_kings} triple kings")
```

### Step 6: Check for a Winner

```python
# Check if there's a winner
winner = game.game_winner()
print(f"Winner: {winner}")
# Returns player name or "Game has not ended"
```

## Complete Game Example

```python
from CheckersGame import Checkers

# Setup
game = Checkers()
alice = game.create_player("Alice", "Black")
bob = game.create_player("Bob", "White")

print("=== Starting Checkers Game ===\n")

# Turn 1: Black moves
game.play_game("Alice", (5, 0), (4, 1))
print("Turn 1: Alice moved (5,0) → (4,1)")
game.print_board()

# Turn 2: White moves
game.play_game("Bob", (2, 3), (3, 2))
print("\nTurn 2: Bob moved (2,3) → (3,2)")
game.print_board()

# Turn 3: Black captures White
captured = game.play_game("Alice", (4, 1), (2, 3))
print(f"\nTurn 3: Alice captured a piece! Total captures: {captured}")
game.print_board()

# Check statistics
print(f"\nAlice's captures: {alice.get_captured_pieces_count()}")
print(f"Bob's captures: {bob.get_captured_pieces_count()}")

# Check winner
print(f"Game status: {game.game_winner()}")
```

## Common Errors

### OutofTurn

**Error:** A player tries to move when it's not their turn

```python
game.play_game("Alice", (5, 0), (4, 1))
game.play_game("Alice", (5, 2), (4, 3))  # ERROR: Alice just moved!
```

### InvalidPlayer

**Error:** Player name doesn't exist

```python
game.play_game("Charlie", (5, 0), (4, 1))  # ERROR: Charlie not created!
```

### InvalidSquare

**Error:** Invalid move attempted

-   Moving from an empty square
-   Moving an opponent's piece
-   Moving to an occupied square
-   Moving outside the board (coordinates > 7 or < 0)

```python
game.play_game("Alice", (3, 3), (4, 4))  # ERROR: No piece at (3,3)
game.play_game("Alice", (2, 1), (3, 0))  # ERROR: (2,1) has White piece, not Black
```

## Tips for Playing

1. **Plan your moves** - Think ahead about captures and promotions
2. **Protect your pieces** - Don't leave pieces vulnerable to capture
3. **Aim for kings** - Kings are more powerful pieces
4. **Control the center** - Center squares give you more movement options
5. **Force captures** - Set up situations where your opponent must move into danger

## Game Variations (This Implementation)

This version has modified rules from standard Checkers:

-   Kings are created when reaching the opponent's end
-   Triple Kings are created when crossing back to your side
-   Game ends when one player captures 12 pieces
-   Movement rules may differ from traditional Checkers

## Future Improvements

-   Missing negative index validation - Doesn't check for negative coordinates
-   No movement rules validation - Doesn't enforce diagonal movement or proper direction
