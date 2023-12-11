import random
import numpy as np

# the possible moves to find all connected empty cells to the current one
# up , up-right , right, down-right, down , down-left, left, up-left
moves = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]


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


def getting_empty_space_solution(matrix_solution, matrix_user, stack_zeros, row_len, col_len):
    # not taking into consideration the initial clicked zone

    # if stack is 0 -> we found all cells that must be shown to the user
    if len(stack_zeros) < 1:
        return

    for move in moves:
        (current_row, current_column) = np.array(move) + stack_zeros[-1]
        if 0 <= current_row < row_len and 0 <= current_column < col_len:
            if matrix_solution[current_row][current_column] == 0 and matrix_user[current_row][current_column] == -2:
                matrix_user[current_row][current_column] = 0
                stack_zeros.append([current_row, current_column])
                getting_empty_space_solution(matrix_solution, matrix_user, stack_zeros, row_len, col_len)
            elif matrix_user[current_row][current_column] == -2:
                matrix_user[current_row][current_column] = matrix_solution[current_row][current_column]
    stack_zeros.pop()


"""[user, solution] = creating_the_used_matrices_behind(10, 5, 10)
print(solution)"""
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
    [[0, 4]], 10, 10
)"""
