# def count_letters(word):
#     letter_count = {}
#
#     for letter in word:
#         if letter != ' ':
#             if letter in letter_count:
#                 letter_count[letter] += 1
#             else:
#                 letter_count[letter] = 1
#
#     return letter_count
#
#
# word = input()
# letter_counts = count_letters(word)
#
#
# for letter, count in letter_counts.items():
#     print(f"{letter} -> {count}

my_dictionary = {'t': 2, 'e': 1, 'x': 1}

for key, value in my_dictionary.items():
    print(f'{key} -> {value}')
