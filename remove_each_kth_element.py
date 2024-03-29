def solution(inputArray, k):

    del inputArray[k - 1::k]

    return inputArray


print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))
# Expected Output: [1, 2, 4, 5, 7, 8, 10]

print(solution([[1, 1, 1, 1, 1]], 1))
# Expected Output: []

print(solution([[1, 2, 1, 2, 1, 2, 1, 2]], 2))
# Expected Output: [1, 1, 1, 1]



# Given array of integers, remove each kth element from it.

# Example

# For inputArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] and k = 3, the output should be
# solution(inputArray, k) = [1, 2, 4, 5, 7, 8, 10].

# Input/Output

    # [execution time limit] 4 seconds (py3)

    # [input] array.integer inputArray

    # Guaranteed constraints:
    # 5 ≤ inputArray.length ≤ 15,
    # -20 ≤ inputArray[i] ≤ 20.

    # [input] integer k

    # Guaranteed constraints:
    # 1 ≤ k ≤ 10.

    # [output] array.integer

    # inputArray without elements k - 1, 2k - 1, 3k - 1 etc.