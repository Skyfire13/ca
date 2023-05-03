use rand::Rng;
use std::{thread, time};
 
// Creates a 2D vector filled with 1s and 0s
fn random_board(size: i32) -> Vec<Vec<i8>> {
    let mut board: Vec<Vec<i8>> = vec![vec![0; size as usize]; size as usize];
 
    for row_iter in &mut board {
        for element in row_iter {
            let mut rng = rand::thread_rng();
            *element = rng.gen_range(0..2);
        }
    }
 
    board
}
 
// Print the passed 2D vector
fn print_board(board: &Vec<Vec<i8>>) {
    for row_iter in board {
        for element in row_iter {
            match *element {
            // match *element {
                1 => print!("██"),
                _ => print!("  "),
            }
        }
        println!();
    }
}
 
fn count_neighbors(board: &Vec<Vec<i8>>, row: i32, col: i32) -> i32{
    let mut count: i32 = 0;
    // let pos = board[row as usize][col as usize];
    // board.len()
    for row_iter in row-1..row+2 {
        for element in col-1..col+2 {
            if row_iter < 0 ||
                element < 0 ||
                row_iter >= board.len() as i32 ||
                element >= board.len() as i32 ||
                (row_iter == row && element == col) {
                    continue;
                }
            match board[row_iter as usize][element as usize] {
                1 => count += 1,
                _ => continue,
            }
        }
    }
    count
}

fn iterate(board: &Vec<Vec<i8>>) -> Vec<Vec<i8>> {
    let mut new_board: Vec<Vec<i8>> = vec![vec![0; board.len()]; board.len()];
    for row_iter in 0..board.len() {
        for element in 0..board.len() {
            let count = count_neighbors(&board, row_iter as i32, element as i32);
            match board[row_iter][element] {
                1 => {
                    if count < 2 || count > 3 {
                        new_board[row_iter][element] = 0;
                    } else {
                        new_board[row_iter][element] = 1;
                    }
                },
                _ => {
                    if count == 3 {
                        new_board[row_iter][element] = 1;
                    } else {
                        new_board[row_iter][element] = 0;
                    }
                },
            }
        }
    }
    new_board
}

fn main() {
    let mut vec = random_board(25);
    print_board(&vec);

    let ten_millis = time::Duration::from_millis(50);

    for _ in 0..50 {
        thread::sleep(ten_millis);
        vec = iterate(&vec);
        print_board(&vec);
        print!("{}[2J", 27 as char);
    }
}



