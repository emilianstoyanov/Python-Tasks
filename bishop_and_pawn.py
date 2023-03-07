def solution(bishop, pawn):
    row = abs(ord(bishop[0]) - ord(pawn[0]))
    col = abs(int(bishop[1]) - int(pawn[1]))

    return row == col


print(solution('a1', 'c3'))
# true

print(solution('h1', 'h3'))
# false


# Given the positions of a white bishop and a black pawn on the standard chess board,
# determine whether the bishop can capture the pawn in one move.

# The bishop has no restrictions in distance for each move, but is limited to diagonal movement.
