def sum_numbers(num1, num2):
    return num1 + num2


def subtract_function(result, num3):
    return result - num3


def add_and_subtract(num1, num2, num3):
    sum_result = sum_numbers(num1, num2)
    final_result = subtract_function(sum_result, num3)
    return final_result


a = int(input())
b = int(input())
c = int(input())

print(add_and_subtract(a, b, c))
