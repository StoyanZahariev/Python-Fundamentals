number_of_characters = int(input())
sum_symbols = 0

for symbol in range(1, number_of_characters + 1):
    letter = ord(input())

    sum_symbols += letter

print(f"The sum equals: {sum_symbols}")
