messages = int(input())

for i in range(1, messages+1):
    number = int(input())

    if number == 88:
        print("Hello")
    elif number == 86:
        print("How are you?")
    elif number == 87 or number < 88:
        print("GREAT!")
    else:
        print("Bye.")
