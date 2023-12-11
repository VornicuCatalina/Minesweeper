import random
import numpy as np
import threading


def placing_the_numbers(bombs_number_height, bombs_number_width, matrix):
    # looks for the bombs and then adds 1 to its neighbours
    for row in range(bombs_number_height):
        for column in range(bombs_number_width):
            # if it is a bomb
            if matrix[row][column] == -1:
                # verify neighbors
                for checker_row in range(3):
                    # it does not get over the limits
                    checked_row = row - 1 + checker_row
                    if 0 <= checked_row < bombs_number_width:
                        for checker_column in range(3):
                            checked_column = column - 1 + checker_column
                            if 0 <= checked_column < bombs_number_height:
                                if matrix[checked_row][checked_column] != -1:
                                    # increases the neighbors by 1 (one more bomb is close to them)
                                    matrix[checked_row][checked_column] += 1


def creating_the_used_matrices_behind(bombs_number_height, bombs_number_width, bombs_number):
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


"""def thread_above_row(matrix_solution, matrix_user, col_start, col_finish, row):
    if col_start != col_finish or row == 0:
        return
    new_col_start = col_start
    for item_column in range(col_start, col_finish + 1):
        if new_col_start == col_start and matrix_solution[row][item_column] == 0:
            new_col_start = item_column - 1
        matrix_user[row][item_column] = matrix_solution[row][item_column]"""


def getting_empty_space_solution(matrix_solution, matrix_user, clicked_row, clicked_column):
    col_start = 0
    col_finish = len(matrix_solution) - 1
    for item_column in range(clicked_column - 1, -1, -1):
        if matrix_solution[clicked_row][item_column] == 0:
            matrix_user[clicked_row][item_column] = 0
        else:
            matrix_user[clicked_row][item_column] = matrix_solution[clicked_row][item_column]
            col_start = item_column
            break
    for item_column in range(clicked_column + 1, len(matrix_solution)):
        if matrix_solution[clicked_row][item_column] == 0:
            matrix_user[clicked_row][item_column] = 0
        else:
            matrix_user[clicked_row][item_column] = matrix_solution[clicked_row][item_column]
            col_finish = item_column
            break


# [user,solution] = creating_the_used_matrices_behind(10, 10, 10)
getting_empty_space_solution(
    [[0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
     [0, 1, -1, 2, 1, 0, 1, 1, 1, 0],
     [1, 2, 2, -1, 2, 1, 1, -1, 1, 0],
     [-1, 1, 1, 2, -1, 1, 2, 2, 2, 0],
     [1, 1, 1, 2, 2, 1, 1, -1, 1, 0],
     [0, 0, 1, -1, 1, 0, 1, 1, 1, 0],
     [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
     [0, 0, 0, 0, 0, 1, -1, 2, 1, 0],
     [0, 0, 0, 0, 0, 1, 2, -1, 2, 1],
     [0, 0, 0, 0, 0, 0, 1, 1, 2, -1]],
    [[-2, -2, -2, -2, -2, -2, -2, -2, -2, -2],
     [-2, -2, -2, -2, -2, -2, -2, -2, -2, -2],
     [-2, -2, -2, -2, -2, -2, -2, -2, -2, -2],
     [-2, -2, -2, -2, -2, -2, -2, -2, -2, -2],
     [-2, -2, -2, -2, -2, -2, -2, -2, -2, -2],
     [-2, -2, -2, -2, -2, -2, -2, -2, -2, -2],
     [-2, -2, -2, -2, -2, -2, -2, -2, -2, -2],
     [-2, -2, -2, -2, -2, -2, -2, -2, -2, -2],
     [-2, -2, -2, -2, -2, -2, -2, -2, -2, -2],
     [-2, -2, -2, -2, -2, -2, -2, -2, -2, -2]],
    0, 4
)
