def solution(inputArray, elemToReplace, substitutionElem):

    f = [substitutionElem if inputArray[idx] == elemToReplace else inputArray[idx] for idx in range(len(inputArray))]

    return f

# def solution(inputArray, elemToReplace, substitutionElem):
#     for idx in range(len(inputArray)):
#
#         if inputArray[idx] == elemToReplace:
#             inputArray[idx] = substitutionElem
#
#     return inputArray


print(solution([1, 2, 1], 1, 3))
# Expected Output: [3, 2, 3]


# Given an array of integers, replace all the occurrences of elemToReplace with substitutionElem.

# Example

# For inputArray = [1, 2, 1], elemToReplace = 1, and substitutionElem = 3, the output should be
# solution(inputArray, elemToReplace, substitutionElem) = [3, 2, 3].

# Input/Output

    # [execution time limit] 4 seconds (py3)

    # [input] array.integer inputArray

    # Guaranteed constraints:
    # 0 ≤ inputArray.length ≤ 104,
    # 0 ≤ inputArray[i] ≤ 109.

    # [input] integer elemToReplace

    # Guaranteed constraints:
    # 0 ≤ elemToReplace ≤ 109.

    # [input] integer substitutionElem

    # Guaranteed constraints:
    # 0 ≤ substitutionElem ≤ 109.

    # [output] array.integer