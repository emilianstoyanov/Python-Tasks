def is_valid_sudoku(grid):
    # Check rows
    for row in grid:
        if not is_valid_unit(row):
            return False

    # Check columns
    for col in range(9):
        column = [grid[row][col] for row in range(9)]
        if not is_valid_unit(column):
            return False

    # Check sub-grids
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            sub_grid = [grid[r][c] for r in range(row, row + 3) for c in range(col, col + 3)]
            if not is_valid_unit(sub_grid):
                return False

    return True


def is_valid_unit(unit):
    # Check if unit contains all numbers from 1 to 9 without repetition
    unit = [num for num in unit if num != '.']
    return len(set(unit)) == len(unit) == 9


print(is_valid_sudoku([[1, 3, 2, 5, 4, 6, 9, 8, 7],
                       [4, 6, 5, 8, 7, 9, 3, 2, 1],
                       [7, 9, 8, 2, 1, 3, 6, 5, 4],
                       [9, 2, 1, 4, 3, 5, 8, 7, 6],
                       [3, 5, 4, 7, 6, 8, 2, 1, 9],
                       [6, 8, 7, 1, 9, 2, 5, 4, 3],
                       [5, 7, 6, 9, 8, 1, 4, 3, 2],
                       [2, 4, 3, 6, 5, 7, 1, 9, 8],
                       [8, 1, 9, 3, 2, 4, 7, 6, 5]]))


# Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with digits so that
# each column, each row, and each of the nine 3 × 3 sub-grids that compose the grid contains all
# of the digits from 1 to 9.

# This algorithm should check if the given grid of numbers represents a correct solution to Sudoku.

# Example

    # For

    # grid = [[1, 3, 2, 5, 4, 6, 9, 8, 7],
    #         [4, 6, 5, 8, 7, 9, 3, 2, 1],
    #         [7, 9, 8, 2, 1, 3, 6, 5, 4],
    #         [9, 2, 1, 4, 3, 5, 8, 7, 6],
    #         [3, 5, 4, 7, 6, 8, 2, 1, 9],
    #         [6, 8, 7, 1, 9, 2, 5, 4, 3],
    #         [5, 7, 6, 9, 8, 1, 4, 3, 2],
    #         [2, 4, 3, 6, 5, 7, 1, 9, 8],
    #         [8, 1, 9, 3, 2, 4, 7, 6, 5]]
    # the output should be
    # solution(grid) = true;

    # For

    # grid = [[8, 3, 6, 5, 3, 6, 7, 2, 9],
    #         [4, 2, 5, 8, 7, 9, 3, 8, 1],
    #         [7, 9, 1, 2, 1, 4, 6, 5, 4],
    #         [9, 2, 1, 4, 3, 5, 8, 7, 6],
    #         [3, 5, 4, 7, 6, 8, 2, 1, 9],
    #         [6, 8, 7, 1, 9, 2, 5, 4, 3],
    #         [5, 7, 6, 9, 8, 1, 4, 3, 2],
    #         [2, 4, 3, 6, 5, 7, 1, 9, 8],
    #         [8, 1, 9, 3, 2, 4, 7, 6, 5]]
    # the output should be
    # solution(grid) = false.

# The output should be false: each of the nine 3 × 3 sub-grids should contain all of the digits from 1 to 9.
# These examples are represented on the image below.


# Input/Output

    # [execution time limit] 4 seconds (py3)

    # [input] array.array.integer grid

    # A matrix representing 9 × 9 grid already filled with numbers from 1 to 9.

    # Guaranteed constraints:
    # grid.length = 9,
    # grid[i].length = 9,
    # 1 ≤ grid[i][j] ≤ 9.

    # [output] boolean

    # true if the given grid represents a correct solution to Sudoku, false otherwise.