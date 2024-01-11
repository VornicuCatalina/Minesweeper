import tkinter as tk
import global_variables_file
import thread_time
import start_game


# the cell in the minesweeper game
class Cell:
    # class_attached_to = the main class that connects them as a matrix
    def __init__(self, root, row, column, class_attached_to):
        """
        Initialisation of the Cell class and creating the cell in the GUI

        :param root: it is the root of the tkinter library
        :param row: the position of the row in the matrix
        :param column: the position of the column in the matrix
        :param class_attached_to: the main class Minesweeper, for being able to call its functions easier
        """
        self.root = root
        self.row = row
        self.column = column
        self.flag = False
        self.is_revealed = False
        self.button = tk.Button(self.root, text="", width=3, height=1, command=self.click, bg="grey")
        self.button.grid(row=row + 1, column=column + 1)

        self.class_attached_to = class_attached_to

    # when the cell is clicked
    def click(self):
        """
        It checks whenever the cell was clicked by the user and checks if the game was won after each click

        :return: nothing (void function)
        """
        if thread_time.winning_or_losing == 0:
            # we have the flag on
            if not global_variables_file.is_looking_for_bombs:
                self.flag_function()
            # we work with bombs
            else:
                self.bomb_function()
            # after each click -> checking winning case
            self.class_attached_to.check_winning_game()
        elif thread_time.time_seconds_for_this_game == 0:
            self.class_attached_to.show_solution()

    def flag_function(self):
        """
        Modifies the attributes of the specific cell by modifying its colour and values in function of the fact that
        it was clicked before or not with the flag on

        :return: nothing (void function)
        """
        # if the cell is already shown to the user
        if not self.is_revealed:
            # if it has a flag on
            if self.flag:
                self.flag = False
                self.button.config(bg="grey")
                # back to unknown cell
                self.class_attached_to.user[self.row][self.column] = -2
            # otherwise
            else:
                self.flag = True
                self.button.config(bg="red")
                # flags -1; easier to compare solution with user var
                self.class_attached_to.user[self.row][self.column] = -1

    def bomb_function(self):
        """
        It checks if the current clicked cell is a bomb or not, if it is then ends the game, otherwise, reveals the cells
        if an empty cell was clicked or the current value if the number is greater than 0

        :return: nothing (void function)
        """
        # we check if it has a flag!!
        if not self.flag:
            # we have a bomb
            if self.class_attached_to.solution[self.row][self.column] == -1:
                self.class_attached_to.game_ended(False)
                # showing the correct solution to the user
                self.class_attached_to.show_solution()
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
        """
        The initialisation of the class and the creation of each Cell visually

        :param root: it is the root of the tkinter library
        :param solution: the solution of the game, the one which was initialised before
        :param user: the user's matrix, the matrix that has the current moves of the user
        """
        self.root = root
        self.rows = global_variables_file.height
        self.cols = global_variables_file.width
        self.cells = [[Cell(root, i, j, self) for j in range(self.cols)] for i in range(self.rows)]
        self.solution = solution
        self.user = user

    # if the player won or lost
    @staticmethod
    def game_ended(condition: bool):
        """
        Just tells the thread if the user won or lost the game

        :param condition: a variable to say if the game was won or lost
        :return: nothing (void function)
        """
        if condition:
            print("won the game")
            thread_time.winning_or_losing = 1
        else:
            print("lost the game")
            thread_time.winning_or_losing = -1

    # calls the function to show neighbors in user matrix
    def showing_neighbors(self, row, col):
        """
        This function reveals the neighbours of the cell recursively (if they have 0 value) and also displays them
        visually, not only the BE

        :param row: the row of the specific cell
        :param col: the column of the specific cell
        :return: nothing (void function)
        """
        start_game.getting_empty_space_solution(self.solution, self.user, [[row, col]], self.rows, self.cols)
        # then shows this graphically
        for row in self.cells:
            for cell in row:
                if self.user[cell.row][cell.column] > -1:
                    cell.button.config(text=self.user[cell.row][cell.column], bg='white')
                    cell.is_revealed = True

    # checks if the matrices are identical user & solution
    def check_winning_game(self):
        """
        this function checks if the matrices user matrix and solution matrix are equal to one another to tell the thread
        if the player finished the game or not

        :return: nothing (void function)
        """
        is_finished = True
        for row in range(self.rows):
            for col in range(self.cols):
                if self.user[row][col] != self.solution[row][col]:
                    is_finished = False
            if not is_finished:
                break
        if is_finished:
            self.game_ended(True)

    # showing the correct solution if the player loses
    def show_solution(self):
        """
        Whenever we lose the game (via clicking on a bomb or the time ended) this function will display the solution
        in the GUI using the cells from the user matrix that are different to the solution matrix.
        It uses light colours for catching the attention of the player and crosses via 'X' when the flag was put wrongly

        :return: nothing (void function)
        """
        for rows in self.cells:
            for cell in rows:
                row = cell.row
                col = cell.column
                if self.user[row][col] != self.solution[row][col]:
                    # should have flagged it as a bomb
                    if self.solution[row][col] == -1:
                        cell.button.config(text='B', bg='red')
                    # flagged it as a bomb when it is not
                    elif self.user[row][col] == -1:
                        cell.button.config(text='X', bg='orange')
                    # shows the rest
                    else:
                        cell.button.config(text=self.solution[row][col], bg='yellow')
