def solution(inputArray):
    all = []

    if len(inputArray) == 1:
        return inputArray

    str_max_length = max(inputArray, key=len)

    s = inputArray.index(str_max_length)
    all.append(str_max_length)
    inputArray.pop(s)

    [all.append(el) for el in inputArray if len(el) == len(str_max_length)]
    return all


print(solution(["aba", "aa", "ad", "vcd", "aba"]))

# Input: ["aba", "aa", "ad", "vcd", "aba"]
# Output ["aba", "vcd", "aba"]

# Input: ["aa"]
# Output ["aa"]


# Input: ["abc", "eeee", "abcd", "dcd"]
# Output ["eeee", "abcd"]


# Given an array of strings, return another array containing all of its longest strings.

# Example

    # For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
    # solution(inputArray) = ["aba", "vcd", "aba"].

# Input/Output

    # [execution time limit] 4 seconds (py3)
    #
    # [input] array.string inputArray
    #
    # A non-empty array.
    #
    # Guaranteed constraints:
    # 1 ≤ inputArray.length ≤ 10,
    # 1 ≤ inputArray[i].length ≤ 10.
    #
    # [output] array.string
    #
    # Array of the longest strings, stored in the same order as in the inputArray.
