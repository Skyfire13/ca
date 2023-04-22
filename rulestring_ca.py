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



def newBoard(rows: int, cols: int) -> list:
    board = np.zeros((rows, cols), dtype=int)
    return board


def printBoard(board: list) -> None:
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                print("  ", end="")
            else:
                print("X ", end="")
        print()


def randomizeBoard(board: list) -> list:
    tempBoard = board

    half_size = int(len(board) / 2)
    center_buffer = int(len(board) / 4)
    
    for i in range(half_size):
        for j in range(half_size):
            tempBoard[i + center_buffer][j + center_buffer] = random.choice([0,1])
    return tempBoard


def fillBoard(board: list) -> list:
    tempBoard = board
    half = int(len(board)) / 2
    
    for i in range(len(board) / 2):
        for j in range(len(board) / 2):
            tempBoard[i + half][j + half] = 1
    return tempBoard


def countNeighbors(board: list, rows: int, cols: int) -> int:
    count = 0
    for i in range(rows - 1, rows + 2):
        for j in range(cols - 1, cols + 2):
            if (i < 0 or j < 0)\
                    or (i > len(board) - 1\
                    or j > len(board[0]) - 1)\
                    or (i == rows and j == cols):
                continue
            if board[i][j] == 1:
                count +=1
    return count


def processRulestring(rulestring: str) -> str | str:
    born = False;
    survive = False;

    # Arrays of numbers for each action
    #born_values = rulestring[:rulestring.find('s')].strip('b')
    #survive_values = rulestring[rulestring.find('s'):].strip('s')

    born_values = rulestring[:rulestring.find(':')]
    survive_values = rulestring[rulestring.find(':'):].strip(':')

    return born_values, survive_values

    

# Remember to use matplotlib.animate
def iterate(board: list, rulestring: str) -> list:

    born, survive = processRulestring(rulestring)

    tempBoard = newBoard(len(board),len(board[0]))
    for i in range(len(board)):
        for j in range(len(board[i])):
            num_neighbors = str(countNeighbors(board, i, j))
            if board[i][j] == 0 and num_neighbors in born:
                tempBoard[i][j] = 1
            elif board[i][j] == 1 and num_neighbors in survive:
                tempBoard[i][j] = 1
            else:
                tempBoard[i][j] = 0
    return tempBoard
   

def main() -> None:
    #rows = int(input("Number of rows: "))
    #cols = int(input("Number of columns: "))

    rows = 100
    cols = 100
    iterations = 0
    # rulestring = '5:23457'
    #rulestring = '45:23457'
    #rulestring = '345:23457'
    #rulestring = '345:5'
    rulestring = '3456:5'
    # rulestring = '28:012345678' <- Frost
    rulestring = '18:345678'

    # No rulestring with birth values exclusively lower than 4
    # cannot grow. There would need to be an empty cell at the
    # edge of the spawn radius that four neighbors, which is
    # impossible on edges

    board = newBoard(rows, cols)
    board = randomizeBoard(board)

    #main game loop
    while True:
        system('printf "\033c"')
        printBoard(board)
        print("\n Iterations: " + str(iterations))
        board = iterate(board, rulestring)
        iterations += 1
        #time.sleep(0.025)

       # if keyboard.is_pressed("q"):
       #     print("Exiting...")
       #     break


main()


