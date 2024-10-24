def loot(chest, items):
    for item in items:
        if item not in chest:
            chest.insert(0, item)

def drop(chest, index):
    if 0 <= index < len(chest):
        item = chest.pop(index)
        chest.append(item)

def steal(chest, count):
    stolen_items = chest[-count:]
    del chest[-count:]
    print(", ".join(stolen_items))
    return stolen_items

def average_treasure_gain(chest):
    if chest:
        total_length = sum(len(item) for item in chest)
        average = total_length / len(chest)
        print(f"Average treasure gain: {average:.2f} pirate credits.")
    else:
        print("Failed treasure hunt.")

def main():
    chest = input().split("|")

    while True:
        command = input()

        if command == "Yohoho!":
            break

        command_parts = command.split()

        if command_parts[0] == "Loot":
            items = command_parts[1:]
            loot(chest, items)

        elif command_parts[0] == "Drop":
            index = int(command_parts[1])
            drop(chest, index)

        elif command_parts[0] == "Steal":
            count = int(command_parts[1])
            steal(chest, count)

    average_treasure_gain(chest)

if __name__ == "__main__":
    main()
