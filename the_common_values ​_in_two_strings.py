def solution(s1, s2):
    l1 = list(s1)
    l2 = list(s2)

    count = 0
    for c in l1:
        if c in l2:
            count += 1
            l2.remove(c)

    return count


print(solution('aabcc', 'adcaa'))

# Input:
# s1: "zzzz"
# s2: "zzzzzzz"
# Expected Output: 4

# Input:
# s1: "a"
# s2: "aaa"
# Expected Output:1

# Given two strings, find the number of common characters between them.
#
# Example
#
# For s1 = "aabcc" and s2 = "adcaa", the output should be
# solution(s1, s2) = 3.
#
# Strings have 3 common characters - 2 "a"s and 1 "c".
#
# Input/Output
# [execution time limit] 4 seconds (py3)
#
# [input] string s1
#
# A string consisting of lowercase English letters.
#
# Guaranteed constraints:
# 1 ≤ s1.length < 15.
#
# [input] string s2
#
# A string consisting of lowercase English letters.
#
# Guaranteed constraints:
# 1 ≤ s2.length < 15.
#
# [output] integer