import re


def solution(text):
    return max(re.split('[^a-zA-Z]', text), key=len)


# print(solution("ABCd"))
# Expected Output: "ABCd"

print(solution("To be or not to be"))
# Expected Output: "not"


print(solution("Ready, steady, go!"))
# # Expected Output: "steady"


print(solution("Ready[[[, steady, go!"))
# # Expected Output: "steady"


# Define a word as a sequence of consecutive English letters. Find the longest word from the given string.

# Example

    # For text = "Ready, steady, go!", the output should be
    # solution(text) = "steady".

# Input/Output

    # [execution time limit] 4 seconds (py3)

    # [input] string text

    # Guaranteed constraints:
    # 4 ≤ text.length ≤ 50.

    # [output] string

    # The longest word from text. It's guaranteed that there is a unique output.


