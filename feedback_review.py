import textwrap

def solution(feedback, size):
    return textwrap.wrap(feedback, size)


# import re
#
# def solution(feedback, size):
#     return re.compile(r"[^ ].{0," + str(size - 2) + r"}[^ ](?= |\Z)").findall(feedback)




# save = []
#
# for i in range(0, len(feedback), size):
#     save.append(feedback[i: i + size].strip(" "))
#
# return save

print(solution("This is an example feedback", 8))
# ["This is", "an", "example", "feedback"]


print(solution("This is an example feedback", 40))
# Expected Output: ["This is an example feedback"]


print(solution("Dude, do you even review these feedbacks?", 16))
# Expected Output: ["Dude, do you", "even review", "these feedbacks?"]


# Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
# You've launched a revolutionary service not long ago, and were busy improving it for the
# last couple of months. When you finally decided that the service is perfect, you remembered
# that you created a feedbacks page long time ago, which you never checked out since then. Now
# that you have nothing left to do, you would like to have a look at what the community thinks of your service.

# Unfortunately it looks like the feedbacks page is far from perfect: each feedback is displayed
# as a one-line string, and if it's too long there's no way to see what it is about. Naturally,
# this horrible bug should be fixed. Implement a function that, given a feedback and the size of
# the screen, splits the feedback into lines so that:

    # each token (i.e. sequence of non-whitespace characters) belongs to one of the lines entirely;
    # each line is at most size characters long;
    # no line has trailing or leading spaces;
    # each line should have the maximum possible length, assuming that all lines before it were also
    # the longest possible.

# Example

# For feedback = "This is an example feedback" and size = 8,
# the output should be

# solution(feedback, size) = ["This is",
#                             "an",
#                             "example",
#                             "feedback"]
# Input/Output

    # [execution time limit] 4 seconds (py3)

    # [input] string feedback

    # A string containing a feedback. Each feedback is guaranteed to contain only letters,
    # punctuation marks and whitespace characters (' ').

    # Guaranteed constraints:
    # 0 ≤ feedback.length ≤ 100.

    # [input] integer size

    # The size of the screen. It is guaranteed that it is not smaller than the longest token in the feedback.

    # Guaranteed constraints:
    # 1 ≤ size ≤ 100.

    # [output] array.string

    # Lines from the feedback, split as described above
