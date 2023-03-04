def solution(s):
    char_order = []
    save = {}
    for c in s:
        if c in save:
            save[c] += 1
        else:
            save[c] = 1
            char_order.append(c)
    for c in char_order:
        if save[c] == 1:
            return c
    return '_'

# def solution(s):
#     for c in s:
#         if s.index(c) == s.rindex(c):
#             return c
#     return '_'


print(solution('abacabad'))
# Expected Output: "c"

# print(solution('abacabaabacaba'))
# _

# print(solution('bcccccccb'))
# _





# Given a string s consisting of small English letters, find and return the
# first instance of a non-repeating character in it. If there is no such character, return '_'.

# Example

    # For s = "abacabad", the output should be
    # solution(s) = 'c'.

    # There are 2 non-repeating characters in the string: 'c' and 'd'. Return c since
    # it appears in the string first.

    # For s = "abacabaabacaba", the output should be
    # solution(s) = '_'.

    # There are no characters in this string that do not repeat.

# Input/Output

    # [execution time limit] 4 seconds (py)

    # [input] string s

    # A string that contains only lowercase English letters.

    # Guaranteed constraints:
    # 1 ≤ s.length ≤ 105.

    # [output] char

    # The first non-repeating character in s, or '_' if there are no characters that do not repeat.