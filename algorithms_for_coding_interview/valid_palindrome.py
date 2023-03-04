# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
# The string will only contain lowercase characters a-z.


def solution(inp):
    for idx in range(0, len(inp)):
        t = inp[:idx] + inp[idx + 1:]
        if t == t[::-1]:
            return True


s = 'radkar'
print(solution(s))
# Output: True


# The “Valid Palindrome” problem is a real classic and you will probably find it repeatedly
# under many different flavors. In this case, the task is to check weather by removing at most one
# character, the string matches with its reversed counterpart. When s = ‘radkar’ the function returns
# Trueas by excluding the ‘k’ we obtain the word ‘radar’ that is a palindrome.
