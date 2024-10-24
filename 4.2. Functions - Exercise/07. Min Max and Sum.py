def min_and_max_sum():
    num = input()
    num_list = list(map(int, num.split()))

    minimum_number = min(num_list)
    maximum_number = max(num_list)
    sum_number = sum(num_list)

    print(f'The minimum number is {minimum_number}')
    print(f'The maximum number is {maximum_number}')
    print(f'The sum number is: {sum_number}')


min_and_max_sum()
