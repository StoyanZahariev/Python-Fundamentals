numbers = input().split()
amount_of_number_to_remove = int(input())
count = 0

number_as_integer = []

for number in numbers:
    number_as_integer.append(int(number))
while count != amount_of_number_to_remove:
    for i in number_as_integer:
        if count == amount_of_number_to_remove:
            break
        if int(i) <= min(number_as_integer):
            number_as_integer.remove(i)
            count += 1
print(', '.join(map(str, number_as_integer)))


