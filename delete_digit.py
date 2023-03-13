def solution(n):

    return max(int(str(n)[:i] + str(n)[i+1:]) for i in range(len(str(n))))


# def solution(n):
#     save = 0
#     m = 0
#
#     lisT = list(str(n))
#     for idx in range(len(lisT)):
#         save = int(lisT.pop(idx))
#
#         n = int("".join(lisT))
#         if m < n:
#             m = n
#             lisT.insert(idx, str(save))
#         else:
#             lisT.insert(idx, str(save))
#
#     return m




print(solution(152))
# 52


print(solution(1001))
# 101

print(solution(10))
# 1


# Given some integer, find the maximal number you can obtain by deleting exactly
# one digit of the given number.

# Example

    # For n = 152, the output should be
    # solution(n) = 52;
    # For n = 1001, the output should be
    # solution(n) = 101.

# Input/Output

    # [execution time limit] 4 seconds (py3)

    # [input] integer n

    # Guaranteed constraints:
    # 10 ≤ n ≤ 106.

    # [output] integer
