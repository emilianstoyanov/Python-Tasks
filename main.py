from collections import Counter


def firstNotRepeatingCharacter(s):
    c = Counter(s)
    for i in s:
        if c[i] == 1:
            return i
        return '_'


print(firstNotRepeatingCharacter('234155566'))