data_by_words = input().split()
separated_words = ""

for word in data_by_words:
    char_amount = len(word)
    separated_words += word*char_amount
print(separated_words)
