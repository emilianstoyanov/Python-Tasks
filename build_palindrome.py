# def solution(st):
#     for i in range(0, len(st)):
#         if st[i:len(st)] == st[i:len(st)][::-1]:
#             return st[0:i] + st[i:len(st)] + st[0:i][::-1]


# print(solution('abcdc'))


def solution(st):
    string_list = list(st)
    i = 0
    while string_list != string_list[::-1]:
        string_list.insert(len(st), st[i])
        i += 1
    return "".join(string_list)


print(solution('abcdc'))
# abcdcba


print(solution('ababab'))
# abababa

print(solution('abba'))
# abba

# Given a string, find the shortest possible string which can be achieved by adding characters
# to the end of initial string to make it a palindrome.

# Example

    # For st = "abcdc", the output should be
    # solution(st) = "abcdcba".

# Input/Output

    # [execution time limit] 4 seconds (py3)

    # [input] string st

    # A string consisting of lowercase English letters.

    # Guaranteed constraints:
    # 3 ≤ st.length ≤ 10.

    # [output] string