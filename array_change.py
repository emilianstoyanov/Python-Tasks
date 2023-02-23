def solution(inputArray):
    count = 0
    for idx in range(len(inputArray) - 1):

        if inputArray[idx] >= inputArray[idx + 1]:
            count += (inputArray[idx] - inputArray[idx + 1]) + 1
            inputArray[idx + 1] += (inputArray[idx] - inputArray[idx + 1]) + 1

    return count

print(solution([2, 1, 10, 1]))
# Expected Output: 12


# print(solution([1, 1, 1]))
# Expected Output: 3


print(solution([2, 3, 3, 5, 5, 5, 4, 12, 12, 10, 15]))
# Expected Output: 13


print(solution([2, 1, 10, 1]))
# Expected Output: 12


print(solution([-1000, 0, -2, 0]))
# Expected Output: 5



# You are given an array of integers. On each move you are allowed to increase
# exactly one of its element by one. Find the minimal number of moves required
# to obtain a strictly increasing sequence from the input.

# Example

    # For inputArray = [1, 1, 1], the output should be
    # solution(inputArray) = 3.

# Input/Output

    # [execution time limit] 4 seconds (py3)

    # [input] array.integer inputArray

    # Guaranteed constraints:
    # 3 ≤ inputArray.length ≤ 105,
    # -105 ≤ inputArray[i] ≤ 105.

    # [output] integer

    # The minimal number of moves needed to obtain a strictly increasing sequence from inputArray.
    # It's guaranteed that for the given test cases the answer always fits signed 32-bit integer type.
