// Create elementary cellular automata given a rule number
package main

import (
	"fmt"
)

// Currently, this function prints the board to 
// the console. Modify it to use a graphics library
func printBoard(board []int) {
	for i := 0; i < len(board); i++ {
		fmt.Printf("%d", board[i])
	}
	fmt.Println()
}


func decimalToBinary(n int) int {
	// convert a decimal number to binary
	// return the binary number

	dec := n 
}




// return the left, center, and right cells
// for a given cell in the board
//	// if the cell is on the edge of the board, 
//	// the edge cells wrap around to the other side of the board
func neighborhood(board []int, position int) (int, int, int) {

	switch board[position - 1 : position + 2] {
		case [0, 0, 0]:
			return 7
		case [0, 0, 1]:
			return 6
		case [0, 1, 0]:
			return 5
		case [0, 1, 1]:
			return 4
		case [1, 0, 0]:
			return 3
		case [1, 0, 1]:
			return 2
		case [1, 1, 0]:
			return 1
		case [1, 1, 1]:			
	}
}

	// create a 1D slice of 0s and 1s
	// for each cell in the slice, apply the rule to the cell and its neighbors
	// print the slice

	// create a slice of 0s and 1s
	// for each cell in the slice, apply the rule to the cell and its neighbors
	// print the slice

func generation(board []int, rule int) []int {
	// create a new slice of the same length as the board
	// for each cell in the slice, apply the rule to the cell and its neighbors
	// return the new slice

	newBoard := make([]int, len(board))
	for i := 0; i < len(board); i++ {
		newBoard[i] = neighborhood(board, i)
	}
}


func createCa(int rule, int length){
	board := make([]int, length)
	for i := 0; i < length; i++ {
		board[i] = 0
	}

	// set the middle cell to 1
	board[length/2] = 1

	printBoard(board)

	for i := 0; i < length; i++ {
		// apply the rule to the cell and its neighbors
		// print the slice
	}



}

func main() {

}
