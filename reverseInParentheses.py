def solution(s):
    start = 0
    for i in range(len(s)):
        if s[i] == "(":
            start = i
        if s[i] == ")":
            end = i
            return solution(s[:start] + s[start + 1:end][::-1] + s[end + 1:])
    return s


print(solution("(bar)"))
# Expected Output: "rab"

print(solution("foo(bar)baz"))
# Expected Output: "foorabbaz"


print(solution("foo(bar)baz(blim)"))
# Expected Output: "foorabbazmilb"

print(solution("foo(bar(baz))blim"))
# Expected Output: "foobazrabblim"

print(solution(""))
# Expected Output: ""


print(solution("()"))
# Expected Output: ""


# Write a function that reverses characters in (possibly nested) parentheses in the input string.

# Input strings will always be well-formed with matching ()s.

# Example

    # For inputString = "(bar)", the output should be
    # solution(inputString) = "rab";
    # For inputString = "foo(bar)baz", the output should be
    # solution(inputString) = "foorabbaz";
    # For inputString = "foo(bar)baz(blim)", the output should be
    # solution(inputString) = "foorabbazmilb";
    # For inputString = "foo(bar(baz))blim", the output should be
    # solution(inputString) = "foobazrabblim".
    # Because "foo(bar(baz))blim" becomes "foo(barzab)blim" and then "foobazrabblim".

# Input/Output

    # [execution time limit] 4 seconds (py3)

    # [input] string inputString

    # A string consisting of lowercase English letters and the characters ( and ). It is guaranteed that all parentheses in inputString form a regular bracket sequence.

    # Guaranteed constraints:
    # 0 ≤ inputString.length ≤ 50.

    # [output] string

    # Return inputString, with all the characters that were in parentheses reversed.