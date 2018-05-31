""" """

# Instructions for the game. 
print("Hello!")
print("Welcome to Battleship! Your objective is to guess my ship's location on a 5x5 grid (starting at 0). My ship takes up only 1 space. You have 4 guesses. Your guesses will show up as X's on the board. Here is the board. Good luck! ")
# Import things and set up variables. 
from random import randint
board = []

# Create the board 
for x in range(5):
  board.append(["O"] * 5)
def print_board(board):
  for row in board:
    print(" ".join(row))
print_board(board)

# Pick the ship\'s location
def random_row(board):
  return randint(0, len(board) - 1)
def random_col(board):
  return randint(0, len(board[0]) - 1)
ship_row = random_row(board)
ship_col = random_col(board)

"""These were test print(values to de-bug the program. 
print(ship_row
print(ship_col
"""


# Running the game - user guessing and comparissons. 
for turn in range(4): 
  print("Turn " + str(turn + 1))
  guess_row = int(input("Guess Row: "))
  guess_col = int(input("Guess Col: "))
  if guess_row == ship_row and guess_col == ship_col:
    print("Congratulations! You sunk my battleship!")
    break
  else: 
    if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4): 
      print("Oops, that's not even in the ocean.")
    elif(board[guess_row][guess_col] == "X"):
      print("You guessed that one already.")
    else: 
      print("You missed my battleship!")
      board[guess_row][guess_col] = "X"
  # print((turn + 1) here!
      print_board(board)
    if turn >= 3: 
      print("Game Over.")

