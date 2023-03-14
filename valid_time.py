def solution(time):
    # spl = time.split(":")
    # first = spl[0]
    # second = spl[1]
    #
    # if int(first) <= 23 and int(second) <= 59:
    #     return True
    # else:
    #     return False

    return int(time.split(":")[0]) <= 23 and int(time.split(":")[1]) <= 59


print(solution("13:58"))
# Expected Output: true


print(solution("25:51"))
# Expected Output: false


print(solution("02:76"))
# Expected Output: false

print(solution("24:00"))
# Expected Output: false

print(solution("02:61"))
# Expected Output: false


# Check if the given string is a correct time representation of the 24-hour clock.

# Example

    # For time = "13:58", the output should be
    # solution(time) = true;
    # For time = "25:51", the output should be
    # solution(time) = false;
    # For time = "02:76", the output should be
    # solution(time) = false.

# Input/Output

    # [execution time limit] 4 seconds (py3)

    # [input] string time

    # A string representing time in HH:MM format. It is guaranteed that the first two characters, as well as the last two characters, are digits.

    # [output] boolean

    # true if the given representation is correct, false otherwise.
