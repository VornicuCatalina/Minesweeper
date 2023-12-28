import tkinter as tk
import global_variables_file


class Cell:
    def __init__(self, root, row, column):
        self.root = root
        self.row = row
        self.column = column
        self.flag = False
        self.is_revealed = False
        self.button = tk.Button(self.root, text="", width=3, height=1, command=self.click, bg="grey")
        self.button.grid(row=row + 1, column=column + 1)

    def click(self):
        if not global_variables_file.is_looking_for_bombs and not self.is_revealed:
            self.flag = True
            self.button.config(bg="red")
        print("i was clicked")
        print(self.row)


class Minesweeper:
    def __init__(self, root):
        self.root = root
        self.rows = global_variables_file.height
        self.cols = global_variables_file.width
        self.cells = [[Cell(root, i, j) for j in range(self.cols)] for i in range(self.rows)]
