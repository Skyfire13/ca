# Life-like CA generator that generates cellular automata through rulestrings
# A rulestring is the notation symbolizing which cells will be born, which
# cells will survive, and which cells will die moving into the next iteration.
#
# Rulestring Format(Birth/Survival Notation):
#
# B23S15
#
# Any numbers following the "B" represent the amount of neighbors an empty
# cell must have for the cell to turn active in the next generation
# Any numbers following the "S" represent the amount of neighbors a living
# cell must have to survive to the next generation
# Any cell that is covered by the birth/survival notation dies moving into
# the next generation.


import numpy as np
import random
import keyboard
import time
from os import system


# Add a parser so you can just throw a text file into this program instead of
# typing everything by hand. Possibly yaml
#
# Inputs:
# Board width
# Board height
# Random soup or specified input
# Rulestring



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


