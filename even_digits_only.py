def solution(n):
    c = [False if False in [False if int(i) % 2 != 0 else True for i in str(n)] else True]

    return c[0]


print(solution(248622))


# def solution(n):
#     for i in str(n):
#         if int(i) % 2 != 0:
#             return False
#     return True

# def solution(n):
#     c = [False if int(i) % 2 != 0 else True for i in str(n)]
#     b = [False if False in c else True]

#     return b[0]




# Check if all digits of the given integer are even.

# Example

    # For n = 248622, the output should be
    # solution(n) = true;
    # For n = 642386, the output should be
    # solution(n) = false.

# Input/Output

    # [execution time limit] 4 seconds (py3)

    # [input] integer n

    # Guaranteed constraints:
    # 1 ≤ n ≤ 109.

    # [output] boolean

    # true if all digits of n are even, false otherwise.