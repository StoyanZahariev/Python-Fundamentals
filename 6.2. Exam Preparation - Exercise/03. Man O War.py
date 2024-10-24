def fire(warship, index, damage):
    if 0 <= index < len(warship):
        warship[index] -= damage
        if warship[index] <= 0:
            print("You won! The enemy ship has sunken.")
            return True
    return False

def defend(pirate_ship, start_index, end_index, damage):
    if 0 <= start_index < len(pirate_ship) and 0 <= end_index < len(pirate_ship):
        for i in range(start_index, end_index + 1):
            pirate_ship[i] -= damage
            if pirate_ship[i] <= 0:
                print("You lost! The pirate ship has sunken.")
                return True
    return False

def repair(pirate_ship, index, health, max_health):
    if 0 <= index < len(pirate_ship):
        pirate_ship[index] = min(pirate_ship[index] + health, max_health)

def status(pirate_ship, max_health):
    count = sum(1 for section in pirate_ship if section < max_health * 0.2)
    print(f"{count} sections need repair.")

def main():
    # Input for ships and maximum health capacity
    pirate_ship = list(map(int, input().split(">")))
    warship = list(map(int, input().split(">")))
    max_health = int(input())

    while True:
        command = input()

        if command == "Retire":
            break

        command_parts = command.split()

        if command_parts[0] == "Fire":
            index = int(command_parts[1])
            damage = int(command_parts[2])
            if fire(warship, index, damage):
                return  # The game ends if the warship is sunk

        elif command_parts[0] == "Defend":
            start_index = int(command_parts[1])
            end_index = int(command_parts[2])
            damage = int(command_parts[3])
            if defend(pirate_ship, start_index, end_index, damage):
                return  # The game ends if the pirate ship is sunk

        elif command_parts[0] == "Repair":
            index = int(command_parts[1])
            health = int(command_parts[2])
            repair(pirate_ship, index, health, max_health)

        elif command_parts[0] == "Status":
            status(pirate_ship, max_health)

    # If the game reaches here, it's a stalemate
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(warship)}")

if __name__ == "__main__":
    main()
