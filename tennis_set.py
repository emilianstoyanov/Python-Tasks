def solution(score1, score2):
    if score1 > score2:
        score1, score2 = score2, score1

    if score1 < 5 and score2 == 6:
        return True

    if score1 in [5, 6] and score2 == 7:
        return True

    return False


print(solution(3, 6))
# Expected Output: true

print(solution(6, 4))
# Expected Output: true


print(solution(7, 5))
# Expected Output: true

print(solution(7, 6))
# Expected Output: true

# print(solution(8, 5))
# # Expected Output: false
#
#
print(solution(6, 5))
# # Expected Output: false
#
print(solution(7, 8))
# # Expected Output: false
#
#
print(solution(7, 2))
# # Expected Output: false



# In tennis, the winner of a set is based on how many games each player wins. The first player to win
# 6 games is declared the winner unless their opponent had already won 5 games, in which case the set
# continues until one of the players has won 7 games.


# Given two integers score1 and score2, your task is to determine if it is possible for a tennis set to
# be finished with a final score of score1 : score2.

# Example

    # For score1 = 3 and score2 = 6, the output should be
    # solution(score1, score2) = true.
    #
    # Since player 1 hadn't reached 5 wins, the set ends once player 2 has won 6 games.
    #
    # For score1 = 8 and score2 = 5, the output should be
    # solution(score1, score2) = false.
    #
    # Since both players won at least 5 games, the set would've ended once one of them won the 7th one.
    #
    # For score1 = 6 and score2 = 5, the output should be
    # solution(score1, score2) = false.
    #
    # This set will continue until one of these players wins their 7th game, so this can't be the final score.

# Input/Output

    # [execution time limit] 4 seconds (js)

    # [input] integer score1

    # Number of games won by the 1st player, non-negative integer.

    # Guaranteed constraints:
    # 0 ≤ score1 ≤ 10.

    # [input] integer score2

    # Number of games won by the 2nd player, non-negative integer.

    # Guaranteed constraints:
    # 0 ≤ score2 ≤ 10.

    # [output] boolean

    # true if score1 : score2 represents a possible score for an ended set, false otherwise.