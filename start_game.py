import random
import numpy as np
import global_variables_file

# the possible moves to find all connected empty cells to the current one
# up , up-right , right, down-right, down , down-left, left, up-left
moves = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]


def placing_the_numbers(bombs_number_height, bombs_number_width, matrix):
    """
    It places the values of the cells that are not empty (number between 1-8)

    We travel through the matrix and check if the current cell was marked as being a bomb, then all of its neighbours
    will get a +1 (only if they are not marked as bombs) in its value as we know that the initial matrix was filled
    with default values (0) or -1 when it is a bomb

    :param bombs_number_height: the number of rows of the matrix
    :param bombs_number_width: the number of columns of the matrix
    :param matrix: the one used for the solution of the game
    :return: nothing (void function)
    """
    # looks for the bombs and then adds 1 to its neighbours
    for row in range(bombs_number_height):
        for column in range(bombs_number_width):
            # if it is a bomb
            if matrix[row][column] == -1:
                # verify neighbors
                for checker_row in range(3):
                    # it does not get over the limits
                    checked_row = row - 1 + checker_row
                    if 0 <= checked_row < bombs_number_height:
                        for checker_column in range(3):
                            checked_column = column - 1 + checker_column
                            if 0 <= checked_column < bombs_number_width:
                                if matrix[checked_row][checked_column] != -1:
                                    # increases the neighbors by 1 (one more bomb is close to them)
                                    matrix[checked_row][checked_column] += 1


def creating_the_used_matrices_behind(bombs_number_height, bombs_number_width, bombs_number):
    """
    This function creates the matrices used behind of the game on the BE side. One of them, the solution matrix is used
    to display the solution of the current game : placing the empty values, bombs then the non-empty safe cells, and the
    matrix for the user that is full 0, this one will be used to display the current stage that the user is in during the
    game


    :param bombs_number_height: the number of rows of the matrix
    :param bombs_number_width: the number of columns of the matrix
    :param bombs_number: how many bombs are used for the current game
    :return: the pair made of two matrices - the one for solution and the initialised one for the user (full 0)
    """
    # initialising with zeros the matrix for solution (the block is empty)
    # also -2 for user (the block is by default unknown)
    matrix_solution = np.zeros([bombs_number_height, bombs_number_width], dtype=int)
    matrix_user = np.full([bombs_number_height, bombs_number_width], -2)

    # seeing the matrix as a whole list of height x width and creating a list of bombs positions
    matrix_size = bombs_number_height * bombs_number_width
    bombs = random.sample(range(matrix_size), bombs_number)
    for bomb in bombs:
        matrix_solution[bomb // bombs_number_width][bomb % bombs_number_width] = -1

    # calling the function for numbers
    placing_the_numbers(bombs_number_height, bombs_number_width, matrix_solution)

    return [matrix_user, matrix_solution]


def getting_empty_space_solution(matrix_solution, matrix_user, stack_zeros, row_len, col_len):
    """
    When the cell, that has the value 0 (is empty), is clicked then it shows every single neighbor that is also empty
    recursively using the stack_zeros, and also shows the border that is formed with the neighbors of the empty spaces
    that are not 0es nor bombs.

    :param matrix_solution: the solution of the game, the one which was initialised before
    :param matrix_user: the user's matrix, the matrix that has the current moves of the user
    :param stack_zeros: the stack used to memorise the pairs made of columns and rows of a specific empty position
    :param row_len: the number of rows of the matrix
    :param col_len: the number of columns of the matrix
    :return: nothing (void function)
    """
    # not taking into consideration the initial clicked zone

    # if stack is 0 -> we found all cells that must be shown to the user
    if len(stack_zeros) < 1:
        return

    for move in moves:
        (current_row, current_column) = np.array(move) + stack_zeros[-1]
        if 0 <= current_row < row_len and 0 <= current_column < col_len:
            # if it is an empty space in solution & didn't get checked in user matrix
            if matrix_solution[current_row][current_column] == 0 and matrix_user[current_row][current_column] == -2:
                matrix_user[current_row][current_column] = 0
                stack_zeros.append([current_row, current_column])
                getting_empty_space_solution(matrix_solution, matrix_user, stack_zeros, row_len, col_len)
            # this is for the barriers
            elif matrix_user[current_row][current_column] == -2:
                matrix_user[current_row][current_column] = matrix_solution[current_row][current_column]
    stack_zeros.pop()


# changes the used method of finding the solution
def change_is_bomb(is_bomb: bool, bomb, flag):
    """
    This function changes the variable used in the game for marking cells as flags or just revealing them, also changes
    the colour of the buttons in function of which one is in use

    :param is_bomb: a checker saying if the chosen button represent the one who has the name 'Bomb'
    :param bomb: the label used for the button 'Bomb'
    :param flag: the label used for the button 'Flag'
    :return:
    """
    global_variables_file.is_looking_for_bombs = is_bomb

    if is_bomb:
        bomb.config(bg="orange")
        flag.config(bg="grey")
    else:
        bomb.config(bg="grey")
        flag.config(bg="orange")
