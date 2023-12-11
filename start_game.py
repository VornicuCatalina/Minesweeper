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
                    if 0 <= checked_row < bombs_number_height:
                        for checker_column in range(3):
                            checked_column = column - 1 + checker_column
                            if 0 <= checked_column < bombs_number_width:
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


def checking_and_modifying_matrix_user(matrix_solution, matrix_user, col_start, col_finish, row, type_used):
    """if type_used == 1:
        if col_start == col_finish or row == -1:
            print("intra si aii")
            return
    else:
        if col_start == col_finish or row == len(matrix_solution):
            print("intra si isi")
            return
    new_col_start = -1
    is_full_different_zero = True
    for item_column in range(col_start, col_finish + 1):
        matrix_user[row][item_column] = matrix_solution[row][item_column]
        if new_col_start == -1 and matrix_solution[row][item_column] == 0:
            is_full_different_zero = False
            new_col_start = item_column - 1
        if new_col_start != -1 and matrix_solution[row][item_column] != 0:
            print("P1")
            print(matrix_user)
            print("++++++++++++++++++++")
            print(f"row is {row} start is {col_start} and finish {item_column}")
            print("----------------")
            if type_used == 1:
                checking_and_modifying_matrix_user(matrix_solution, matrix_user, new_col_start, item_column, row - 1,
                                                   type_used)

            else:
                checking_and_modifying_matrix_user(matrix_solution, matrix_user, new_col_start, item_column, row + 1,
                                                   type_used)
            new_col_start = -1

    if is_full_different_zero:
        return

    finished_row = False
    if matrix_solution[row][col_finish] == 0:
        for item_column in range(col_finish + 1, len(matrix_solution[0])):
            if matrix_solution[row][col_finish] == 0:
                matrix_user[row][item_column] = 0
            else:
                matrix_user[row][item_column] = matrix_solution[row][item_column]
                print("P2")
                print(matrix_user)
                print("++++++++++++++++++++")

                print(f"row is {row} start is {col_start} and finish {item_column}")
                print("----------------")
                if type_used == 1:
                    checking_and_modifying_matrix_user(matrix_solution, matrix_user, new_col_start, item_column,
                                                       row - 1,
                                                       type_used)
                else:
                    checking_and_modifying_matrix_user(matrix_solution, matrix_user, new_col_start, item_column,
                                                       row + 1,
                                                       type_used)

                finished_row = True
    if not finished_row:
        print("P3")
        print(matrix_user)
        print("++++++++++++++++++++")

        print(f"row is {row} start is {col_start} and finish {len(matrix_solution[0]) - 1}")
        print("----------------")
        if type_used == 1:
            checking_and_modifying_matrix_user(matrix_solution, matrix_user, new_col_start, len(matrix_solution[0]) - 1,
                                               row - 1,
                                               type_used)
        else:
            checking_and_modifying_matrix_user(matrix_solution, matrix_user, new_col_start, len(matrix_solution[0]) - 1,
                                               row + 1,
                                               type_used)"""
    # ITERATIVE MODE
    """checking_and_modifying_matrix_user(matrix_solution, matrix_user, new_col_start, len(matrix_solution[0]) - 1,
                                           row, type_used)"""

    """if not see_zero and matrix_solution[row][item_column] == 0:
        see_zero = True
    matrix_user[row][item_column] = matrix_solution[row][item_column]
    if see_zero and new_col_finish == col_finish and matrix_solution[row][item_column] != 0:
        new_col_finish = item_column

if matrix_solution[row][col_finish] == 0:
    for item_column in range(col_finish + 1, len(matrix_solution[0])):
        if matrix_solution[row][col_finish] == 0:
            matrix_user[row][item_column] = 0
        else:
            matrix_user[row][item_column] = matrix_solution[row][item_column]
            new_col_finish = item_column
            break"""

    # print(new_col_start)
    print("hey")


"""def thread_above_row(matrix_solution, matrix_user, col_start, col_finish, row):  # type 1
    if col_start == col_finish or row == -1:
        return
    checking_and_modifying_matrix_user(matrix_solution, matrix_user, col_start,
                                       col_finish, row, 1)


def thread_below_row(matrix_solution, matrix_user, col_start, col_finish, row):  # type 2
    if col_start == col_finish or row == len(matrix_solution):
        return
    checking_and_modifying_matrix_user(matrix_solution, matrix_user, col_start,
                                       col_finish, row + 1, 2)"""


def getting_empty_space_solution(matrix_solution, matrix_user, clicked_row, clicked_column):
    col_start = 0
    col_finish = len(matrix_solution[0]) - 1
    for item_column in range(clicked_column - 1, -1, -1):
        if matrix_solution[clicked_row][item_column] == 0:
            matrix_user[clicked_row][item_column] = 0
        else:
            matrix_user[clicked_row][item_column] = matrix_solution[clicked_row][item_column]
            col_start = item_column
            break
    for item_column in range(clicked_column + 1, len(matrix_solution[0])):
        if matrix_solution[clicked_row][item_column] == 0:
            matrix_user[clicked_row][item_column] = 0
        else:
            matrix_user[clicked_row][item_column] = matrix_solution[clicked_row][item_column]
            col_finish = item_column
            break
    """thread_above_row(matrix_solution, matrix_user, col_start, col_finish, clicked_row)
    thread_below_row(matrix_solution, matrix_user, col_start, col_finish, clicked_row)"""

    print(np.array(matrix_user))


[user, solution] = creating_the_used_matrices_behind(10, 5, 10)
print(solution)
"""getting_empty_space_solution(
    [[0, 0, 0, 0, 0, 2, -1, 3, 1, 1],
     [0, 0, 0, 0, 0, 2, -1, 3, -1, 1],
     [0, 0, 0, 0, 0, 2, 2, 3, 1, 1],
     [0, 1, 1, 1, 0, 1, -1, 2, 1, 0],
     [0, 1, -1, 1, 1, 2, 3, -1, 1, 0],
     [0, 1, 1, 1, 1, -1, 2, 2, 3, 2],
     [0, 0, 0, 0, 1, 1, 1, 1, -1, -1],
     [1, 1, 0, 0, 0, 0, 0, 1, 2, 2],
     [-1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 1, 0, 0, 0, 0, 0, 0, 0, 0]],
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
    0,0
)"""
"""getting_empty_space_solution(
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
"""
