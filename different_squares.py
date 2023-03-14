def solution(matrix):
    row, col = len(matrix), len(matrix[0])

    s = set()
    for r in range(row - 1):
        for c in range(col - 1):
            s.add((matrix[r][c], matrix[r][c + 1], matrix[r + 1][c], matrix[r + 1][c + 1]))
    return len(s)


print(solution([[1, 2, 1],
                [2, 2, 2],
                [2, 2, 2],
                [1, 2, 3],
                [2, 2, 1]]))
# Expected Output: 6


print(solution([[9, 9, 9, 9, 9],
                [9, 9, 9, 9, 9],
                [9, 9, 9, 9, 9],
                [9, 9, 9, 9, 9],
                [9, 9, 9, 9, 9],
                [9, 9, 9, 9, 9]]))
# # Expected Output: 1
#
#
# print(solution([[3]]))
# # Expected Output: 0
#
#
# print(solution([[3, 4, 5, 6, 7, 8, 9]]))
# # Expected Output: 0
#
#
# print(solution([[3],
#                 [4],
#                 [5],
#                 [6],
#                 [7]]))
# # Expected Output: 0ч
#ч
#
print(solution([[2, 5, 3, 4, 3, 1, 3, 2],
                [4, 5, 4, 1, 2, 4, 1, 3],
                [1, 1, 2, 1, 4, 1, 1, 5],
                [1, 3, 4, 2, 3, 4, 2, 4],
                [1, 5, 5, 2, 1, 3, 1, 1],
                [1, 2, 3, 3, 5, 1, 2, 4],
                [3, 1, 4, 4, 4, 1, 5, 5],
                [5, 1, 3, 3, 1, 5, 3, 5],
                [5, 4, 4, 3, 5, 4, 4, 4]]))
# # Expected Output: 54

# print(solution([[1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 9, 9, 9, 2, 3, 9]]))
# # Expected Output: 0


# Given a rectangular matrix containing only digits, calculate the number of different 2 × 2 squares in it.

# Example

    # For

    # matrix = [[1, 2, 1],
    #           [2, 2, 2],
    #           [2, 2, 2],
    #           [1, 2, 3],
    #           [2, 2, 1]]
    # the output should be
    # solution(matrix) = 6.

    # Here are all 6 different 2 × 2 squares:

    # 1 2
    # 2 2
    # 2 1
    # 2 2
    # 2 2
    # 2 2
    # 2 2
    # 1 2
    # 2 2
    # 2 3
    # 2 3
    # 2 1

# Input/Output

    # [execution time limit] 4 seconds (py3)

    # [input] array.array.integer matrix

    # Guaranteed constraints:
    # 1 ≤ matrix.length ≤ 100,
    # 1 ≤ matrix[i].length ≤ 100,
    # 0 ≤ matrix[i][j] ≤ 9.

    # [output] integer

    # The number of different 2 × 2 squares in matrix.