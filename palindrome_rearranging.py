def solution(inputString):
    count = [0] * 256
    for i in inputString:
        count[ord(i)] += 1

    odd = 0
    for i in range(256):
        if count[i] & 1 == 1:
            odd += 1

    if odd > 1:
        return False
    else:
        return True


print(solution('aabb'))
# Expected Output: true

print(solution('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaabc'))
# # Expected Output: false

# # print(solution('abbcabb'))
# # # Expected Output: true

# print(solution('zyyzzzzz'))
# # # # Expected Output: true


# Given a string, find out if its characters can be rearranged to form a palindrome.

# Example

# For inputString = "aabb", the output should be
# solution(inputString) = true.

# We can rearrange "aabb" to make "abba", which is a palindrome.

# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] string inputString

# A string consisting of lowercase English letters.

# Guaranteed constraints:
# 1 ≤ inputString.length ≤ 50.

# [output] boolean

# true if the characters of the inputString can be rearranged to form a palindrome, false otherwise.
