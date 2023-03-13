# def solution(cell):
#     r = 0
#     c = [ord(cell[0]) - 96, int(cell[1])]
#
#     m = [[1, 2], [2, 1], [1, -2], [-2, 1], [-1, 2], [2, -1], [-1, -2], [-2, -1]]
#
#     for i in m:
#         if 0 < c[0] + i[0] < 9 and 0 < c[1] + i[1] < 9:
#             r += 1
#     return r
#
#
#
# print(solution('a1'))


def solution(ce):
    c = 0
    if ord(ce[0]) - 96 + 2 < 9:
        if int(ce[1]) - 1 > 0 and int(ce[1]) + 1 < 9:
            c += 2
        elif int(ce[1]) - 1 > 0 or int(ce[1]) + 1 < 9:
            c += 1
    if ord(ce[0]) - 96 + 1 < 9:
        if int(ce[1]) - 2 > 0 and int(ce[1]) + 2 < 9:
            c += 2
        elif int(ce[1]) - 2 > 0 or int(ce[1]) + 2 < 9:
            c += 1
    if ord(ce[0]) - 96 - 2 > 0:
        if int(ce[1]) - 1 > 0 and int(ce[1]) + 1 < 9:
            c += 2
        elif int(ce[1]) - 1 > 0 or int(ce[1]) + 1 < 9:
            c += 1
    if ord(ce[0]) - 96 - 1 > 0:
        if int(ce[1]) - 2 > 0 and int(ce[1]) + 2 < 9:
            c += 2
        elif int(ce[1]) - 2 > 0 or int(ce[1]) + 2 < 9:
            c += 1
    return c

# Given a position of a knight on the standard chessboard, find the number of different
# moves the knight can perform.

# The knight can move to a square that is two squares horizontally and one square vertically,
# or two squares vertically and one square horizontally away from it. The complete move therefore
# looks like the letter L. Check out the image below to see all valid moves for a knight piece that
# is placed on one of the central squares.


# Input/Output

    # [execution time limit] 4 seconds (py3)

    # [input] string cell

    # String consisting of 2 letters - coordinates of the knight on an 8 × 8 chessboard in chess notation.

    # Guaranteed constraints:
    # cell.length = 2,
    # 'a' ≤ cell[0] ≤ 'h',
    # 1 ≤ cell[1] ≤ 8.

# [output] integer

