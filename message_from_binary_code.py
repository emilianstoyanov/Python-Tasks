def solution(code):
    output = [chr(int(code[i:i + 8], 2)) for i in range(0, len(code), 8)]

    return ''.join(output)


print(solution('010010000110010101101100011011000110111100100001'))
# Expected Output: "Hello!"


print(solution(
    '010011010110000101111001001000000111010001101000011001010010000001000110011011110111001001100011011'
    '00101001000000110001001100101001000000111011101101001011101000110100000100000011110010110111101110101'))
# # Expected Output: "May the Force be with you"


print(solution(
    '01000101011011000110010101101101011001010110111001110100011000010111001001111001001011000010000001101101'
    '0111100100100000011001000110010101100001011100100010000001010111011000010111010001110011011011110110111000100001'))
# # Expected Output: "Elementary, my dear Watson!"



# You are taking part in an Escape Room challenge designed specifically for programmers.
# In your efforts to find a clue, you've found a binary code written on the wall behind a vase,
# and realized that it must be an encrypted message. After some thought, your first guess is that
# each consecutive 8 bits of the code stand for the character with the corresponding extended ASCII code.

# Assuming that your hunch is correct, decode the message.

# Example

    # For code = "010010000110010101101100011011000110111100100001", the output should be
    # solution(code) = "Hello!".

    # The first 8 characters of the code are 01001000, which is 72 in the binary numeral system. 72 stands
    # for H in the ASCII-table, so the first letter is H.
    # Other letters can be obtained in the same manner.

# Input/Output

    # [execution time limit] 4 seconds (py3)

    # [input] string code

    # A string, the encrypted message consisting of characters '0' and '1'.

    # Guaranteed constraints:
    # 0 < code.length < 800.

    # [output] string

    # The decrypted message.