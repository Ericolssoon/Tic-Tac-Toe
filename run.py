board = [["-", "-", "-"],
          ["-", "-", "-"],
          ["-", "-", "-"]]

# print the board


def print_board():
    print(board[0][0] + "  " + board[0][1] + "  " + board[0][2])
    print(board[1][0] + "  " + board[1][1] + "  " + board[1][2])
    print(board[2][0] + "  " + board[2][1] + "  " + board[2][2])

# check for win


def has_winner():
    return False

# check for tie


def is_tie():
    return False

# start game


def play(player_turn):
    print_board()
  while True:
    print("Player " + player_turn + ", your turn.")

    row = input("Choose row: ")
    column = input("Choose column: ")
    row = int(row) - 1
    column = int(column) - 1

    board[row][column] = player_turn

    print_board()

    # check for win or tie
    if has_winner():
      print("Player " + player_turn + " Won!")
      break
    elif is_tie():
      print("It it a tie!.")
      break

    # change player
    if player_turn == "X":
      player_turn = "0"
    else:
      player_turn = "X"

play("X")