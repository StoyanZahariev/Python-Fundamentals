orders_numbers = int(input())


total = 0


for i in range(orders_numbers  ):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())

    if price_per_capsule < 0.01 or price_per_capsule > 100:
        continue
    elif days < 1 or days > 31:
        continue
    elif capsules_per_day < 1 or capsules_per_day > 2000:
        continue

    price_of_coffee = price_per_capsule * days * capsules_per_day
    total += price_of_coffee

    print(f"The price for the coffee is: ${price_of_coffee:0.2f}")

print(f"Total: ${total:0.2f}")

