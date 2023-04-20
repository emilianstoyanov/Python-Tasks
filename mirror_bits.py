def solution(a):
    x = bin(a).replace("0b", "")[::-1]
    return eval('0b' + x)


print(solution(97))
# 67

print(solution(8))
# 1


# Reverse the order of the bits in a given integer.

# Example

    # For a = 97, the output should be
    # solution(a) = 67.

    # 97 equals to 1100001 in binary, which is 1000011 after mirroring, and that is 67 in base 10.

    # For a = 8, the output should be
    # solution(a) = 1.

# Input/Output

    # [execution time limit] 4 seconds (py3)

    # [input] integer a

    # Guaranteed constraints:
    # 5 ≤ a ≤ 105.

    # [output] integer