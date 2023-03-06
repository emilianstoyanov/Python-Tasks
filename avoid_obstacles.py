# def solution(inputArray):
#     c = 2
#     while True:
#         if sorted([i % c for i in inputArray])[0] > 0:
#             return c
#         c += 1


def solution(inputArray):
    for n in range(1, max(inputArray)):
        if all(i % n for i in inputArray):
            return n
    return max(inputArray) + 1


print(solution([5, 3, 6, 7, 9]))
# 4
