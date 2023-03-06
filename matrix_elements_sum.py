def solution(matrix):
    col = len(matrix[0])
    row = len(matrix)
    total = 0

    for c in range(col):
        for r in range(row):

            current_mat = matrix[r][c]

            if current_mat != 0:
                total += matrix[r][c]
            else:
                break

    return total

# https://app.codesignal.com/arcade/intro/level-2/xskq4ZxLyqQMCLshr
print(solution([[1, 1, 1],
                [2, 2, 2],
                [3, 3, 3]]))  # 18

print(solution([[0, 1, 1, 2],
                [0, 5, 0, 0],
                [2, 0, 3, 3]]))  # 9

print(solution([[1, 1, 1, 0],
                [0, 5, 0, 1],
                [2, 1, 3, 10]]))  # 9

print(solution([[1, 1, 1, 0],
                [0, 5, 0, 1],
                [2, 1, 3, 10]]))  # 9
