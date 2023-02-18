def solution(n):
    st = str(n)

    c = int(len(st) / 2)
    left = st[:c]
    right = st[c:]

    sum_left = sum([int(el)for el in left])
    sum_right = sum([int(el)for el in right])

    return sum_left == sum_right


print(solution(1230))



# Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.

# Given a ticket number n, determine if it's lucky or not.

# Example

    # For n = 1230, the output should be
    # solution(n) = true;
    # For n = 239017, the output should be
    # solution(n) = false.

# Input/Output

    # [execution time limit] 4 seconds (py3)
    #
    # [input] integer n
    #
    # A ticket number represented as a positive integer with an even number of digits.
    #
    # Guaranteed constraints:
    # 10 ≤ n < 106.
    #
    # [output] boolean
    #
    # true if n is a lucky ticket number, false otherwise.