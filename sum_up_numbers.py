import re


def solution(inputString):
    b = re.findall(r'\d+', inputString)
    if b:
        return sum([int(e) for e in b])

    return 0


print(solution("2 apples, 12 oranges"))
# Expected Output: 14

print(solution("123450"))
# Expected Output: 123450

print(solution("Your payment method is invalid"))
# Expected Output: 0


print(solution("no digits at all"))
# Expected Output: 0


print(solution("there are some (12) digits 5566 in this 770 string 239"))
# Expected Output: 6587

print(solution("abc abc 4 abc 0 abc"))
# Expected Output: 4

print(solution("abcdefghijklmnopqrstuvwxyz1AbCdEfGhIjKlMnOpqrstuvwxyz23,74 -"))
# Expected Output: 98



# CodeMaster has just returned from shopping.
# He scanned the check of the items he bought and
# gave the resulting string to Ratiorg to figure out
# the total number of purchased items. Since Ratiorg is a
# bot he is definitely going to automate it, so he needs a
# program that sums up all the numbers which appear in the given input.

# Help Ratiorg by writing a function that returns the sum of numbers that
# appear in the given inputString.

# Example

    # For inputString = "2 apples, 12 oranges", the output should be
    # solution(inputString) = 14.

# Input/Output

    # [execution time limit] 4 seconds (py3)

    # [input] string inputString

    # Guaranteed constraints:
    # 0 ≤ inputString.length ≤ 105.

    # [output] integer