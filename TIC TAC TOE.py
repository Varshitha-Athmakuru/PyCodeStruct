import random

board = ["-" for _ in range(9)]
CurrentPlayer = "X"
GameRunning = True

# Print the board
def printBoard(board):
    for i in range(0, 9, 3):
        print(board[i] + " | " + board[i + 1] + " | " + board[i + 2])
    print()

# Take player input
def playerInput(board):
    while True:
        position = int(input("Select a spot (1-9): ")) - 1
        if 0 <= position < 9 and board[position] == "-":
            board[position] = CurrentPlayer
            break
        else:
            print("Invalid move. Please try again.")

# Check for win
def checkWin(board):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if board[win[0]] == board[win[1]] == board[win[2]] != "-":
            return True
    return False

# Check if the board is full
def checkTie(board):
    if "-" not in board:
        return True
    else:
        return False

# Switch player
def SwitchPlayer():
    global CurrentPlayer
    if CurrentPlayer == "X" :
        CurrentPlayer = "O"
    else :
        CurrentPlayer="X"

# Computer's turn
def computerMove(board):
    availableSpots = [i for i, spot in enumerate(board) if spot == "-"]
    position = random.choice(availableSpots)
    board[position] = CurrentPlayer

# Main game loop
def playGame():
    global GameRunning

    print("Welcome to Tic Tac Toe!")
    printBoard(board)

    while GameRunning:
        if CurrentPlayer == "X":
            playerInput(board)
        else:
            computerMove(board)

        printBoard(board)

        if checkWin(board):
            print("Player " + CurrentPlayer + " wins!")
            GameRunning = False
        elif checkTie(board):
            print("It's a tie!")
            GameRunning = False
        else:
            SwitchPlayer()

# Start the game
playGame()
