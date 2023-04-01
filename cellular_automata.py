# This script will create Stephen Wolfram's elementary cellular automata
# /home/alan/.local/bin not on path!


import sys
import random
import numpy as np
from PIL import Image


# Returns a numpy array of the given size
# with the middlemost bit turned on
def createBoard(size):
    if size % 2 == 0:
        size += 1
    board = np.zeros(size)
    board[int(len(board)/2)] = 1
    return board



# Prints a slice of the board
def printBoard(board):
    for i in range(len(board)):
        if np.all(board[i], 0):
            print("█", end=' ')
        else:
            print("-", end=' ')
    print()



# Outputs a png image of the full board
def createImage(master):
    img = Image.new('RGB', (len(master), len(master[0])), color = 'white')
    pixels = img.load()
    for i in range(len(master)):
        for j in range(len(master[0])):
            if master[i][j] == 0:
                pixels[i, j] = (0, 0, 0)
            else:
                pixels[i, j] = (255, 255, 255)
    # Needs flipped across the veritcle axis and rotated 90 degrees clockwise
    img = img.transpose(Image.FLIP_TOP_BOTTOM)
    img = img.transpose(Image.ROTATE_270)
    img.save('my.png')
    img.show()



# Defines the type of neighborhood
# and returns a int 0-7
def neighborhood(board, position):
    slice = board[position -1 : position + 2]
    if np.array_equal(slice, np.array([0, 0, 0])):
        return 0
    if np.array_equal(slice, np.array([0, 0, 1])):
        return 1
    if np.array_equal(slice, np.array([0, 1, 0])):
        return 2
    if np.array_equal(slice, np.array([0, 1, 1])):
        return 3
    if np.array_equal(slice, np.array([1, 0, 0])):
        return 4
    if np.array_equal(slice, np.array([1, 0, 1])):
        return 5
    if np.array_equal(slice, np.array([1, 1, 0])):
        return 6
    if np.array_equal(slice, np.array([1, 1, 1])):
        return 7



# Turns a decimal number into an binary representation,
# stores that in an array, and reverses the order
def applyRule(ruleNumber):
    rule = np.binary_repr(ruleNumber)
    rule = rule.zfill(8)
    rule = np.array(list(rule))
    rule = [int(i) for i in rule]
    rule.reverse()
    return rule



# Returns a the next state of the board 
def step(board, rule):
    new_board = createBoard(len(board))
    rule = applyRule(rule)
    for i in range(1, len(board) - 1):
        n = neighborhood(board, i)
        new_board[i] = rule[n]
    return new_board


"""
Primary loop. Appends each slice(type numpy array)
and appends it to the master list. After the given
number of iterations, a full image will be created.
The bottom-most for loop can be used instead of the
createImage function to simply print the full board
to the terminal.
"""
def loop(size, rule, iterations):
    board = createBoard(size)
    master = []
    
    master.append(board)
    printBoard(master)
    for i in range(iterations):
        board = step(board, rule)
        master.append(board)
    #for i in range(len(master)):
    #    printBoard(master[i])
    createImage(master)


"""
Callable from command line
Args  | type | Description
-----------------------------------------------------
@size | int  | How many pixels wide the board will be
@rule | int  | Which rule number to apply, 0-255 valid
"""
def main():
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]

    # Input error handlng
    if rule < 0 or rule > 255:
        print("Error - Rule must be between 0 and 255")
        exit()
    if rule % 1 != 0:
        print("Error - Rule must be an integer")
        exit()

    #size = iterations(2) - 1
    #(size + 1) / 2 = iterations
    size = int(sys.argv[1])
    rule = int(sys.argv[2])
    iterations = round((size + 1) /2)

    loop(size, rule, iterations)


#main()

test = float(sys.argv[1])
print(type(test))






