event = input()
coffee_counter = 0

event_to_lower = ['coding', 'movie', 'dog', 'cat']
event_to_upper = ['CODING', 'MOVIE', 'DOG', 'CAT']

while event != 'END':
    if event in event_to_upper:
        coffee_counter += 2
    elif event in event_to_lower:
        coffee_counter += 1

    event = input()

if event == 'END':
    if coffee_counter > 5:
        print("You need extra sleep")
    else:
        print(coffee_counter)

# action = input()
#
# coffees = 0
#
# action_to_lower = ['coding', 'movie', 'dog', 'cat']
# action_to_upper = ['CODING', 'MOVIE', 'DOG', 'CAT']
#
# while action != 'END':
#
#     if action in action_to_lower:
#         coffees += 1
#     elif action in action_to_upper:
#         coffees += 2
#
#     action = input()
#
#     if action == 'END':
#         if coffees > 5:
#             print('You need extra sleep')
#         else:
#             print(coffees)