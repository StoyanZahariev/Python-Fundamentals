data = {}
things = input()

while things != 'stop':

    things_quantity = int(input())
    if things not in data.keys():
        data[things] = 0
    data[things] += things_quantity

    things = input()

for things, things_quantity in data.items():
    print(f'{things} -> {things_quantity}')
    