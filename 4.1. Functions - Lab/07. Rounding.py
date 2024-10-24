# float_numbers_as_string = input()
#
# float_numbers_as_numbers = [float(num) for num in float_numbers_as_string.split()]
#
# rounded_numbers = [round(num) for num in float_numbers_as_numbers]
#
# print(rounded_numbers)

def round_numbers(float_list):
    return [round(num) for num in float_list]


numbers_as_string = input()
numbers_as_float = [float(num) for num in numbers_as_string.split()]
rounded_list = round_numbers(numbers_as_float)

print(rounded_list)
