# current_string = input()
#
# while current_string != "End":
#     if current_string != "SoftUni":
#         for character in current_string:
#             print(character*2, end="")
#         print()
#     current_string = input()

current_string = input()

while current_string != "End":
    if current_string != "SoftUni":
        new_string = ""
        for character in current_string:
            new_string += character*2
        print(new_string)
        print()
    current_string = input()
