def get_even_numbers():
    numbers = input()

    numbers_list = list(map(int, numbers.split()))

    even_numbers = list(filter(lambda x: x % 2 == 0, numbers_list))

    print(even_numbers)


get_even_numbers()
