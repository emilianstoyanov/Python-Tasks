def solution(n):
    A = [[0] * n for _ in range(n)]
    i = j = di = 0
    dj = 1
    for A[i][j] in range(1, n ** 2 + 1):
        if A[(i + di) % n][(j + dj) % n]:
            di, dj = dj, -di
        i += di
        j += dj
    return A



print(solution(3))
# Expected Output:
                # [[1,2,3],
                #  [8,9,4],
                #  [7,6,5]]


print(solution(5))
# Expected Output:
                # [[1,2,3,4,5],
                #  [16,17,18,19,6],
                #  [15,24,25,20,7],
                #  [14,23,22,21,8],
                #  [13,12,11,10,9]]




# Construct a square matrix with a size N × N containing integers from 1 to N * N in a spiral order,
# starting from top-left and in clockwise direction.

# Example

    # For n = 3, the output should be

    # solution(n) = [[1, 2, 3],
    #                [8, 9, 4],
    #                [7, 6, 5]]

# Input/Output

    # [execution time limit] 4 seconds (py3)

    # [input] integer n

    # Matrix size, a positive integer.

    # Guaranteed constraints:
    # 3 ≤ n ≤ 100.

    # [output] array.array.integer

