list_of_strings = input().split()
absolute_list_of_numbers = []

for element in list_of_strings:
    absolute_list_of_numbers.append(abs(float(element)))
print(absolute_list_of_numbers)

