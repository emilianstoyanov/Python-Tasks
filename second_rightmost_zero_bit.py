def solution(n):
    return ((((n + 1) | n) + 1) | n) - n


# def solution(n):
#     return 2**([i for i, ltr in enumerate(bin(n)[:1:-1]) if ltr == '0'])[1];


print(solution(37))
# Input: n: 37
# Expected Output: 8


print(solution(1073741824))
# Input: n: 1073741824
# Expected Output: 2

print(solution(83748))
# Input: n: 83748
# Expected Output: 2

# Presented with the integer n, find the 0-based position of the second rightmost
# zero bit in its binary representation (it is guaranteed that such a bit exists),
# counting from right to left.

# Return the value of 2position_of_the_found_bit.

# Example

# For n = 37, the output should be
# solution(n) = 8.

# 3710 = 1001012. The second rightmost zero bit is at position 3 (0-based) from the
# right in the binary representation of n.
# Thus, the answer is 23 = 8.

# Input/Output

    # [execution time limit] 4 seconds (py3)

    # [input] integer n

    # Guaranteed constraints:
    # 4 ≤ n ≤ 230.

    # [output] integer