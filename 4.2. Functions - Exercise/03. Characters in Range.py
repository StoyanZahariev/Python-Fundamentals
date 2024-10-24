def characters_in_range(char1, char2):

    letter1 = ord(char1)
    letter2 = ord(char2)

    if letter1 > letter2:
        letter1, letter2 = letter2, letter1

    return [chr(i) for i in range(letter1 + 1, letter2)]


char1 = input()
char2 = input()
print(' '.join(characters_in_range(char1, char2)))
