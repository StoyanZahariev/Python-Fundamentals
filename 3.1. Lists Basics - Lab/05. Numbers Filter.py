iterations = int(input())
num = []
filtered = []

for i in range(iterations):
    current_num = int(input())
    num.append(current_num)

command = input()
if command == "even":
    for num in num:
        if num % 2 == 0:
            filtered.append(num)
elif command == "odd":
    for num in num:
        if num % 2 != 0:
            filtered.append(num)
elif command == "positive":
    for num in num:
        if num >= 0:
            filtered.append(num)
elif command == "negative":
    for num in num:
        if num < 0:
            filtered.append(num)
print(filtered)
