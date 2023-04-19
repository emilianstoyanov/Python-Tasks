def solution(a, b):
    all_num = []
    # for i in range(a, b+1):
    #     all_num.append(int(bin(i).replace("0b", "")))

    # total = 0
    # for el in all_num:
    #     total += sum(int(digit) for digit in str(el))


    all_num = [int(bin(i).replace("0b", "")) for i in range(a, b+1)]
    total = sum([int(digit) for el in all_num for digit in str(el)])
    return total


# print(bin(2).replace("0b", ""))

print(solution(2, 7))
# Expected Output: 11

print(solution(0, 1))
# Expected Output: 1

print(solution(1, 10))
# Expected Output: 17



# You are given two numbers a and b where 0 ≤ a ≤ b.
# Imagine you construct an array of all the integers from a to b inclusive.
# You need to count the number of 1s in the binary representations of all the numbers in the array.

# Example

# For a = 2 and b = 7, the output should be
# solution(a, b) = 11.

# Given a = 2 and b = 7 the array is: [2, 3, 4, 5, 6, 7].
# Converting the numbers to binary, we get [10, 11, 100, 101, 110, 111],
# which contains 1 + 2 + 1 + 2 + 2 + 3 = 11 1s.

# Input/Output

    # [execution time limit] 4 seconds (py3)

    # [input] integer a

    # Guaranteed constraints:
    # 0 ≤ a ≤ b.

    # [input] integer b

    # Guaranteed constraints:
    # a ≤ b ≤ 10.

    # [output] integer

