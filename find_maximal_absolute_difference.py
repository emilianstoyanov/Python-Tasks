def solution(inputArray):
    max_abs = 0

    for idx in range(len(inputArray) - 1):

        if abs(inputArray[idx] - inputArray[idx + 1]) > max_abs:
            max_abs = abs(inputArray[idx] - inputArray[idx + 1])

    return max_abs


print(solution([2, 4, 1, 0]))
# 3
