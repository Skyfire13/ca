
import numpy as np
import random
import keyboard
import time
from os import system

def newBoard(rows, cols):
    board = np.zeros((rows, cols), dtype=int)
    return board


def printBoard(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                print("  ", end="")
            else:
                print("🮙 ", end="")
        print()


def randomizeBoard(board):
    tempBoard = board
    for i in range(len(board)):
        for j in range(len(board[i])):
            tempBoard[i][j] = random.choice([0,1])
    return tempBoard


def fillBoard(board):
    tempBoard = board
    for i in range(len(board)):
        for j in range(len(board[i])):
            tempBoard[i][j] = 1
    return tempBoard


def countNeighbors(board, r, c):
    count = 0
    for i in range(r-1, r+2):
        for j in range(c-1, c+2):
            if (i<0 or j<0) or (i>len(board)-1 or j>len(board[0])-1) or (i==r and j==c):
                continue
            if board[i][j] == 1:
                count +=1
    return count


def iterate(board):
    tempBoard = newBoard(len(board),len(board[0]))
    for i in range(len(board)):
        for j in range(len(board[i])):
            c = countNeighbors(board, i, j)
            if ((board[i][j] == 1) and (c < 2)):
                tempBoard[i][j] = 0
            elif ((board[i][j] == 1) and (c > 3)):
                tempBoard[i][j] = 0
            elif ((board[i][j] == 0) and (c == 3)):
                tempBoard[i][j] = 1
            else:
                tempBoard[i][j] = board[i][j]
    return tempBoard


def addGlider(board):
    tempBoard = board
    board[0][1] = 1
    board[1][2] = 1
    board[2][0] = 1
    board[2][1] = 1
    board[2][2] = 1
    return tempBoard


def rTetromino(board):
    # Find middle
    center_x = int(len(board) / 2)
    center_y = int(len(board[0]) / 2)

    board[center_y][center_x] = 1
    board[center_y + 1][center_x] = 1
    board[center_y - 1][center_x] = 1
    board[center_y][center_x - 1] = 1
    board[center_y - 1][center_x + 1] = 1

    return board
    

def main():
    rows = int(input("Number of rows: "))
    cols = int(input("Number of columns: "))
    board = newBoard(rows, cols)
    #board = addGlider(board)
    #board = randomizeBoard(board)
    board = rTetromino(board)


    #main game loop
    while True:
        system('clear')
        printBoard(board)
        board = iterate(board)
        time.sleep(0.025)


main()







