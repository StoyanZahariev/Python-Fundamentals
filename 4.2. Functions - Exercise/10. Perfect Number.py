def is_perfect_number(num):
    if num < 1:
        return "It's not so perfect."

    divisors_sum = sum(i for i in range(1, num) if num % i == 0)

    if divisors_sum == num:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


number = int(input())
print(is_perfect_number(number))
