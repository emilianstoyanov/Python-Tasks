def solution(a, b):
    if a > b:
        return True

    while a < b:
        a += 1
        b -= 1

        if a > b:
            return True

    return False


print(solution(3, 1))
# Expected Output: true


# print(solution(2, 6))
# Expected Output: false

# print(solution(2, 10))
# Expected Output: false

# print(solution(0, 1))
# Expected Output: true

# Given integers a and b, determine whether the following pseudocode results in an infinite loop

# while a is not equal to b do
#   increase a by 1
#   decrease b by 1
# Assume that the program is executed on a virtual machine which can store arbitrary long numbers and execute forever.

# Example

    # For a = 2 and b = 6, the output should be
    # solution(a, b) = false;
    # For a = 2 and b = 3, the output should be
    # solution(a, b) = true.

# Input/Output

    # [execution time limit] 4 seconds (rb)

    # [input] integer a

    # Guaranteed constraints:
    # 0 ≤ a ≤ 20.

    # [input] integer b

    # Guaranteed constraints:
    # 0 ≤ b ≤ 20.

    # [output] boolean

    # true if the pseudocode will never stop, false otherwise.