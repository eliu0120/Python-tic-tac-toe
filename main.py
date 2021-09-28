# global variables
board = []
player = 1

# Create board
def create_board():
    global board
    board = [list(" | | "), list(" | | "), list(" | | ")]

# print board
def print_board():
    print("")
    for i in range(len(board)):
        for j in board[i]:
            print(j, end="")
        print("")

# check if game has been won or board is full
def check_board():
    winStatus = 2
    # check for horizontals
    for i in range(len(board)):
        if board[i][0] == board[i][2] and board[i][0] == board[i][4] and board[i][0] != ' ':
            winStatus = 1
            return winStatus
        elif board[i][0] == ' ' or  board[i][2] == ' ' or  board[i][4] == ' ':
            winStatus = 0
    
    # check for verticals
    for i in range(0, len(board[0]), 2):
        if board[0][i] == board[1][i] and board[0][i] == board[2][i] and board[0][i] != ' ':
            winStatus = 1
            return winStatus
        elif board[0][i] == ' ' or  board[1][i] == ' ' or  board[2][i] == ' ':
            winStatus = 0

    # check for diagonals
    if (board[0][0] == board[1][2] and board[0][0] == board[2][4] and board[0][0] != ' ') or (board[0][4] == board[1][2] and board[0][4] == board[2][0] and board[0][4] != ' '):
        winStatus = 1
    return winStatus

# Opening menu
print("Tic-Tac-Toe!!!\n\n")
response = input("Play? (Y/N)\n")

# Game
if response == "y" or response == "Y" or response == "yes" or response == "Yes":
    create_board()

    # Loop for player interaction
    while check_board() == 0:
        print_board()
        print("\nPlayer " + str(player) + "'s turn")
        row = input("Input row:\n0) Row 1\n1) Row 2\n2) Row 3\n")
        column = input("\nInput column:\n0) Column 1\n1) Column 2\n2) Column 3\n")
        if player == 1 and board[int(row)][int(column) * 2] == ' ':
            board[int(row)][int(column) * 2] = 'X'
            player = 2
        elif player == 2 and board[int(row)][int(column) * 2] == ' ':
            board[int(row)][int(column) * 2] = 'O'
            player = 1
        else:
            response = input("There is already a piece on that position, please input something to try again\n")
    
    # Determine winner
    print_board()
    if (player == 1 and check_board() == 1):
        print("Player 2 wins!")
    elif (player == 2 and check_board() == 1):
        print("Player 1 wins!")
    else:
        print("Tie!")