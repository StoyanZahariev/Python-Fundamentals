products = {}

while True:
    command = input()

    if command == "buy":
        break

    name, price, quantity = command.split()
    price = float(price)
    quantity = int(quantity)

    if name in products:
        current_price, current_quantity = products[name]
        products[name] = (price, current_quantity + quantity)
    else:
        products[name] = (price, quantity)

for name, (price, quantity) in products.items():
    total_price = price * quantity
    print(f"{name} -> {total_price:.2f}")
