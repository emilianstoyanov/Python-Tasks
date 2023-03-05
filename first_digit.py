def solution(inputString):
    for el in inputString:
        o = ord(el)

        if 48 <= o <= 57:
            return chr(o)

# def solution(inputString):
#     for i in inputString:
#         if i.isdigit():
#             return i


print(solution('var_1__Int'))
# 1

print(solution('_Aas_23'))
# 2

print(solution('0ss'))
# 0


# Find the leftmost digit that occurs in a given string.

# Example

    # For inputString = "var_1__Int", the output should be
    # solution(inputString) = '1';
    # For inputString = "q2q-q", the output should be
    # solution(inputString) = '2';
    # For inputString = "0ss", the output should be
    # solution(inputString) = '0'.

# Input/Output

    # [execution time limit] 4 seconds (py3)

    # [input] string inputString

    # A string containing at least one digit.

    # Guaranteed constraints:
    # 3 ≤ inputString.length ≤ 10.

    # [output] char