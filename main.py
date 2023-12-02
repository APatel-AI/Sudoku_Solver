import tkinter as tk
from random import sample

class SudokuSolverGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")

        self.board = [[tk.StringVar() for _ in range(9)] for _ in range(9)]

        self.create_board_frame()
        self.create_controls_frame()

    def create_board_frame(self):
        self.board_frame = tk.Frame(self.root)
        self.board_frame.grid(row=0, column=0, padx=10, pady=10)

        for i in range(9):
            for j in range(9):
                entry = tk.Entry(self.board_frame, width=3, font=('Helvetica', 16), textvariable=self.board[i][j])
                entry.grid(row=i, column=j)
                entry.bind('<FocusIn>', lambda event, i=i, j=j: self.on_entry_click(i, j))

    def create_controls_frame(self):
        self.controls_frame = tk.Frame(self.root)
        self.controls_frame.grid(row=0, column=1, padx=10, pady=10)

        tk.Button(self.controls_frame, text="Fill Random", command=self.fill_random).grid(row=0, column=0, pady=5)
        tk.Button(self.controls_frame, text="Solve", command=self.solve).grid(row=1, column=0, pady=5)

    def on_entry_click(self, i, j):
        # Clear the entry when clicked
        self.board[i][j].set('')

    def fill_random(self):
        # Clear the board
        for i in range(9):
            for j in range(9):
                self.board[i][j].set('')

        # Generate a random Sudoku puzzle
        puzzle = sample(range(1, 10), 9)
        for i in range(9):
            for j in range(9):
                self.board[i][j].set(puzzle[(i + j) % 9])

    def is_valid_move(self, row, col, num):
        # Check if the number is not in the current row, column, and 3x3 grid
        for i in range(9):
            if self.board[row][i].get() == num or self.board[i][col].get() == num or \
                    self.board[row - row % 3 + i // 3][col - col % 3 + i % 3].get() == num:
                return False
        return True

    def solve(self):
        if self.solve_sudoku():
            print("Sudoku solved successfully!")
        else:
            print("No solution exists!")

    def solve_sudoku(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j].get() == '':
                    for num in map(str, range(1, 10)):
                        if self.is_valid_move(i, j, num):
                            self.board[i][j].set(num)
                            if self.solve_sudoku():
                                return True
                            self.board[i][j].set('')
                    return False
        return True


if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuSolverGUI(root)
    root.mainloop()
