# Given a string, find the first non-repeating character in it and return its index.
# If it doesn't exist, return -1. # Note: all the input strings are already lowercase.


# def solution(inp):
#     save = {}
#     save_alph = []
#     for el in inp:
#         if el not in save:
#             save[el] = 1
#             save_alph.append(el)
#         elif el in save:
#             save[el] += 1

#     for i in save:
#         if save[i] == 1 and i in save_alph:
#             return inp.index(i)
#     return -1


# print(solution('alphabet'))
# print(solution('barbados'))
# print(solution('crunchy'))

# Output:
# # 1
# # 2
# # 1

# Approach 2
import collections


def solution(s):
    # build hash map : character and how often it appears
    count = collections.Counter(s)  # <-- gives back a dictionary with words occurrence count
    # Counter({'l': 1, 'e': 3, 't': 1, 'c': 1, 'o': 1, 'd': 1})
    # find the index
    for idx, ch in enumerate(s):
        if count[ch] == 1:
            return idx
    return -1


print(solution('alphabet'))
print(solution('barbados'))
print(solution('crunchy'))

# Output:
# 1
# 2
# 1