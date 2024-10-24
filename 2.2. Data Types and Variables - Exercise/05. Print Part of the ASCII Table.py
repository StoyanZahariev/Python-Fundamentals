num1 = int(input())
num2 = int(input())

for symbol in range(num1, num2 + 1):
    digit = chr(symbol)
    print(digit, end=' ')

