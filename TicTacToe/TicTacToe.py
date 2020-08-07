import numpy as np
from random import randint

def CheckWinVertical(win, Opponent):
    if (board[0][0] == board[1][0] == board[2][0] == "X") or (board[0][1] == board[1][1] == board [2][1] == "X") or (board[0][2] == board[1][2] == board[2][2] == "X"):
        print("Player1 won vertically!")
        win = 0
    elif (board[0][0] == board[1][0] == board[2][0] == "O") or (board[0][1] == board[1][1] == board [2][1] == "O") or (board[0][2] == board[1][2] == board[2][2] == "O"):
        if Opponent == "Player2":
            print("Player2 won vertically!")
        else:
            print("Computer won vertically")
        win = 0
    return win

def CheckWinHorizontal(win, Opponent):
    if (board[0][0] == board[0][1] == board[0][2] == "X") or (board[1][0] == board[1][1] == board[1][2] == "X") or (board[2][0] == board[2][1] == board[2][2] == "X"):
        print("Player1 won horizontally!")
        win = 0
    elif (board[0][0] == board[0][1] == board[0][2] == "O") or (board[1][0] == board[1][1] == board[1][2] == "O") or (board[2][0] == board[2][1] == board[2][2] == "O"):
        if Opponent == "Player2":
            print("Player2 won horizontally")
        else:
            print("Computer won horizontally")
        win = 0
    return win

def CheckWinDiagonal(win, Opponent):
    if (board[0][0] == board[1][1] == board[2][2] == "X") or (board[2][0] == board[1][1] == board[0][2] == "X"):
        print("Player1 won diagonally")
        win = 0
    elif (board[0][0] == board[1][1] == board[2][2] == "O") or (board[2][0] == board[1][1] == board[0][2] == "O"):
        if Opponent == "Player2":
            print("Player2 won diagonally!")
        else:
            print("Computer won diagonally")
        win = 0
    return win

def Player1(board):
    player1 = input("Player1 enter your position (row, column): ")
    row = int(player1[0]) - 1
    column = int(player1[2]) - 1
    while board[row][column] == "X" or board[row][column] == "O":
        player1 = input("Invalid input. Player1 enter your position (row, column): ")
        row = int(player1[0]) - 1
        column = int(player1[2]) - 1
    board[row][column] = "X"
    PrintBoard(board)

def Player2(board):
    player2 = input("Player2 enter your position (row, column): ")
    row = int(player2[0]) - 1
    column = int(player2[2]) - 1
    while board[row][column] == "X" or board[row][column] == "O":
        player2 = input("Invalid input. Player2 enter your position (row, column): ")
        row = int(player2[0]) - 1
        column = int(player2[2]) - 1
    board[row][column] = "O"
    PrintBoard(board)

def ComputerPlayer(board):
    row = randint(0,2)
    column = randint(0,2)
    print("Computer enter your position (row,column): " + str(row) + "," + str(column))
    while board[row][column] == "X" or board[row][column] == "O":
        row = randint(0,2)
        column = randint(0,2)
        print("Invalid position. Computer enter your position (row,column): " + str(row) + "," + str(column))
    board[row][column] = "O"
    PrintBoard(board)


def PrintBoard(board):
    print("| " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " |")
    print("| " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " |")
    print("| " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " |")

def PlayGame(c, PlayCount, Opponent):
    while c == 1:
        if Opponent == "Player2":
            Player1(board)
            PlayCount += 1
            c = CheckWinVertical(win, Opponent)
            if c == 0:
                break
            c = CheckWinHorizontal(win, Opponent)
            if c == 0:
                break
            c = CheckWinDiagonal(win, Opponent)
            if c == 0:
                break
            if PlayCount == 9:
                print("It is a tie!")
                break
            Player2(board)
            PlayCount += 1
            c = CheckWinVertical(win, Opponent)
            if c == 0:
                break
            c = CheckWinHorizontal(win, Opponent)
            if c == 0:
                break
            c = CheckWinDiagonal(win, Opponent)
            if c == 0:
                break
        else:
            Player1(board)
            PlayCount += 1
            c = CheckWinVertical(win, Opponent)
            if c == 0:
                break
            c = CheckWinHorizontal(win, Opponent)
            if c == 0:
                break
            c = CheckWinDiagonal(win, Opponent)
            if c == 0:
                break
            if PlayCount == 9:
                print("It is a tie!")
                break
            ComputerPlayer(board)
            PlayCount += 1
            c = CheckWinVertical(win, Opponent)
            if c == 0:
                break
            c = CheckWinHorizontal(win, Opponent)
            if c == 0:
                break
            c = CheckWinDiagonal(win, Opponent)
            if c == 0:
                break
    print("End Game!")

board = np.empty((3,3), dtype= str)
print("-- Here is the initial board --")
print("-- Player1 plays with X, Player2 plays with O --")
PrintBoard(board)


win = 1
c = 1
PlayCount = 0
PlayAgain = 0

while PlayAgain == 0:
    Opponent = input("Would you like to play against the computer or Player2? ")
    PlayGame(c, PlayCount, Opponent)
    answer = input("Would you like to play again? ")
    if answer == "NO" or answer == "no":
        break
    else:
        board = np.empty((3, 3), dtype=str)
        print("-- Here is the initial board --")
        print("-- Player1 plays with X, Player2 plays with O --")
        PrintBoard(board)









