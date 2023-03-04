# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.

# Notes:
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.


def solution(n1, n2):
    return str(eval(n1) + eval(n2))


num1 = '200'
num2 = '100'

print(solution(num1, num2))  # 300
