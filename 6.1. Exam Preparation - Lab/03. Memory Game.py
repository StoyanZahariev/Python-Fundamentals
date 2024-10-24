sequence_data = input().split()

moves = 0

while True:
    command = input()

    if command == 'end':
        break
    index1, index2 = map(int, command.split())
    moves += 1

    if index1 == index2 or not (0 <= index1 < len(sequence_data)) or not (0 < index2 < len(sequence_data)):
        middle_index = len(sequence_data) // 2
        