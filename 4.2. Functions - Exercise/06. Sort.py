def sort_numbers():
    numbers = input()
    numbers_list = list(map(int, numbers.split()))
    sorted_numbers = sorted(numbers_list)

    print(sorted_numbers)


sort_numbers()
