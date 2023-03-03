def solution(inputString):
    t = [chr(ord(character) - 25) if ord(character) == 122 else chr(ord(character) + 1) for character in inputString]

    return ''.join(t)


print(solution('crazy'))
# dsbaz

# print(solution('z'))
# a


# Given a string, your task is to replace each of its characters by the next one in
# the English alphabet; i.e. replace a with b, replace b with c, etc (z would be replaced by a).

# Example

# For inputString = "crazy", the output should be solution(inputString) = "dsbaz".

# Input/Output

    # [execution time limit] 4 seconds (py3)

    # [input] string inputString

    # A non-empty string consisting of lowercase English characters.

    # Guaranteed constraints:
    # 1 ≤ inputString.length ≤ 1000.

    # [output] string

    # The resulting string after replacing each of its characters.