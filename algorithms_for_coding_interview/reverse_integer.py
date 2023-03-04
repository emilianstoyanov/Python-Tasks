# Given an integer, return the integer with reversed digits.
# Note: The integer could be either positive or negative.
def solution(n):
    s = str(n)

    if s[0] == '-':
        # return int('-' + s[:0:-1])
        return int('-' + s[1:][::-1])

    return int(s[::-1])


print(solution(-123))
# -321

print(solution(12345))
# 54321
