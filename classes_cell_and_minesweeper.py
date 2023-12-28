import tkinter as tk
import global_variables_file
import thread_time
import start_game


class Cell:
    def __init__(self, root, row, column, class_attached_to):
        self.root = root
        self.row = row
        self.column = column
        self.flag = False
        self.is_revealed = False
        self.button = tk.Button(self.root, text="", width=3, height=1, command=self.click, bg="grey")
        self.button.grid(row=row + 1, column=column + 1)

        self.class_attached_to = class_attached_to

    def click(self):
        if thread_time.winning_or_losing == 0:
            # we have the flag on
            if not global_variables_file.is_looking_for_bombs:
                self.flag_function()
            # we work with bombs
            else:
                self.bomb_function()
            # after each click -> checking winning case
            self.class_attached_to.check_winning_game()

    def flag_function(self):
        if not self.is_revealed:
            if self.flag:
                self.flag = False
                self.button.config(bg="grey")
                # back to unknown cell
                self.class_attached_to.user[self.row][self.column] = -2
            else:
                self.flag = True
                self.button.config(bg="red")
                # flags -1; easier to compare solution with user var
                self.class_attached_to.user[self.row][self.column] = -1

    def bomb_function(self):
        # we check if it has a flag!!
        if not self.flag:
            # we have a bomb
            if self.class_attached_to.solution[self.row][self.column] == -1:
                self.class_attached_to.game_ended(False)
                # when losing, showing the solution to the user :D, but later
            # is a number
            elif self.class_attached_to.solution[self.row][self.column] > 0:
                self.is_revealed = True
                self.class_attached_to.user[self.row][self.column] = self.class_attached_to.solution[self.row][
                    self.column]
                self.button.config(text=self.class_attached_to.user[self.row][self.column], bg="white")
            # is empty space
            else:
                self.button.config(text=0, bg='white')
                self.class_attached_to.showing_neighbors(self.row, self.column)


class Minesweeper:
    def __init__(self, root, solution, user):
        self.root = root
        self.rows = global_variables_file.height
        self.cols = global_variables_file.width
        self.cells = [[Cell(root, i, j, self) for j in range(self.cols)] for i in range(self.rows)]
        self.solution = solution
        print(self.solution)
        self.user = user

    def game_ended(self, condition: bool):
        if condition:
            print("won the game")
            thread_time.winning_or_losing = 1
        else:
            print("lost the game")
            thread_time.winning_or_losing = -1

    def showing_neighbors(self, row, col):
        start_game.getting_empty_space_solution(self.solution, self.user, [[row, col]], self.rows, self.cols)
        for row in self.cells:
            for cell in row:
                if self.user[cell.row][cell.column] > -1:
                    cell.button.config(text=self.user[cell.row][cell.column], bg='white')
                    cell.is_revealed = True

    def check_winning_game(self):
        is_finished = True
        for row in range(self.rows):
            for col in range(self.cols):
                if self.user[row][col] != self.solution[row][col]:
                    is_finished = False
            if not is_finished:
                break
        if is_finished:
            self.game_ended(True)
