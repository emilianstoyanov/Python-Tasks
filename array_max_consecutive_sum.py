def solution(inputArray, k):
    c = m = sum(inputArray[:k])

    for i in range(len(inputArray) - k):
        c = c + inputArray[i + k] - inputArray[i]
        m = max(c, m)

    return m

    # total = 0

    # for idx in range(len(inputArray)):
    #
    #     if sum(inputArray[idx:k + idx]) > total:
    #         total = sum(inputArray[idx:k + idx])
    #     else:
    #         continue
    # return total

    # max_sum = 0
    # for i in range(0, len(inputArray) - k + 1):
    #     temp = 0
    #     for j in range(i, i + k):
    #         temp += inputArray[j]
    #
    #     if temp > max_sum:
    #         max_sum = temp
    #
    # return max_sum


print(solution([2, 3, 5, 1, 6], 2))
# 8

print(solution([1, 3, 4, 2, 4, 2, 4], 4))
# 13


# Given array of integers, find the maximal possible sum of some of its k consecutive elements.

# Example

# For inputArray = [2, 3, 5, 1, 6] and k = 2, the output should be
# solution(inputArray, k) = 8.
# All possible sums of 2 consecutive elements are:

    # 2 + 3 = 5;
    # 3 + 5 = 8;
    # 5 + 1 = 6;
    # 1 + 6 = 7.
    # Thus, the answer is 8.

# Input/Output

    # [execution time limit] 4 seconds (py3)

    # [input] array.integer inputArray

    # Array of positive integers.

    # Guaranteed constraints:
    # 3 ≤ inputArray.length ≤ 105,
    # 1 ≤ inputArray[i] ≤ 1000.

    # [input] integer k

    # An integer (not greater than the length of inputArray).

    # Guaranteed constraints:
    # 1 ≤ k ≤ inputArray.length.

    # [output] integer

    # The maximal possible sum.
