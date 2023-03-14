def solution(p):
    if p == 0:
        return 10
    for i in range(3600):
        a = 1
        for j in str(i):
            a *= int(j)
        if a == p:
            return i
    return -1


print(solution(12))
# Expected Output: 26

# print(solution(243))
# # Expected Output: 399
#
# print(solution(19))
# # Expected Output: -1
#
# print(solution(450))
# # Expected Output: 2559
#
#
# print(solution(0))
# # Expected Output: 10
#
# print(solution(13))
# # Expected Output: -1
#
# print(solution(1))
# # Expected Output: 1

# Given an integer product, find the smallest positive (i.e. greater than 0)
# integer the product of whose digits is equal to product. If there is no such
# integer, return -1 instead.

# Example

    # For product = 12, the output should be
    # solution(product) = 26;
    # For product = 19, the output should be
    # solution(product) = -1.

# Input/Output

    # [execution time limit] 4 seconds (py3)

    # [input] integer product

    # Guaranteed constraints:
    # 0 ≤ product ≤ 600.

    # [output] integer