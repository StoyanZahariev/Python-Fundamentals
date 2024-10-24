def odd_even_sums(number: str):
    sum_of_odd_digits = 0
    sum_of_even_digits = 0
    for digits in number:
        if int(digits) % 2 == 0:
            sum_of_even_digits += int(digits)
        else:
            sum_of_odd_digits += int(digits)

    return f'Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}'


some_number = input()
print(odd_even_sums(some_number))
