import os
import time
import numpy as np
from cell import Cell

class MemoryGame():
    """Mempry Game"""
    def __init__(self):
        self.__board = None
        self.__size = 0
        self.__win_case = 0

    def __input_size(self):
        """Prompt the user for a valid board size."""
        while True:
            try:
                size = int(input("Enter the grid size (e.g., 4 for 4x4): "))
                if size % 2 == 0 and size >= 2:
                    self.__size = size
                    self.__win_case = (size ** 2) // 2
                    break
                print("Size must be even and greater than 1.")
            except ValueError:
                print("Invalid input! Please enter an integer.")

    def __init_board(self):
        """Initialize and shuffle the game board with pairs of matching cells."""
        cells = np.array([*[Cell(i) for i in range(1 , self.__size ** 2 // 2 + 1)],
                          *[Cell(i) for i in range(1 , self.__size ** 2 // 2 + 1)]])
        np.random.shuffle(cells)
        self.__board = cells.reshape(self.__size, self.__size)

    def __check_cords(self):
        """Get and validate coordinates from the user."""
        while True:
            cords = input("Flip the first card (row col):").split()
            try:
                if len(cords) == 2:
                    x, y = map(int, cords)
                    self.__board[x][y]
                    if x >= 0 and y >= 0 and self.__board[x][y].founded == False:
                        return x, y
                print("Invalid coordinates or cell already revealed!")
            except ValueError:
                print("Invalid input! Please enter row and column numbers.")

    def __check_win(self) -> bool:
        """Check if the player has matched all pairs."""
        return self.__win_case == 0

    def __reveal_and_check_match(self, x1, y1, x2, y2):
        """Reveal cells and check for a match."""
        if self.__board[x1][y1] == self.__board[x2][y2]:
            print("It's a match!")
            time.sleep(1)
            self.__win_case -= 1
            return True
        print("No match! Hiding cards again...")
        _ = [print("." * n, end='\r') or time.sleep(0.2) for n in range(20)]
        self.__board[x1][y1].founded = False
        self.__board[x2][y2].founded = False
        return False

    def run(self):
        """Run the game loop."""
        self.__input_size()
        self.__init_board()
        while not self.__check_win():
            self.__print_board()
            x1, y1 = self.__check_cords()
            self.__board[x1][y1].founded = True
            self.__print_board()
            x2, y2 = self.__check_cords()
            self.__board[x2][y2].founded = True
            self.__print_board()
            if self.__reveal_and_check_match(x1, y1, x2, y2) and self.__check_win():
                print("Congratulations! You've matched all pairs.")
                break

    def __print_board(self):
        """Display the game board, revealing only the matched cells."""
        os.system("clear")
        for row in self.__board:
            print(" ".join(str(cell) if cell.founded else "*" for cell in row))
