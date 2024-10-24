def order(product: str, amount: float):
    if product == 'coffee':
        return amount * 1.50
    if product == 'coke':
        return amount * 1.40
    if product == 'water':
        return amount * 1.00
    if product == 'snacks':
        return amount * 2.00


product = input()
amount = int(input())
result = order(product, amount)
print(f'{result:.2f}')
