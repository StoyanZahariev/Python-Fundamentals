import math

number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())

max_bonus = 0
max_attendance = 0

for student in range(number_of_students):
    student_attendance = int(input())
    if student_attendance > number_of_lectures:
        student_attendance = number_of_lectures
    if student_attendance >= max_attendance:
        max_attendance = student_attendance
    if number_of_lectures > 0:
        total_bonus = student_attendance / number_of_lectures * (5 + additional_bonus)

        if total_bonus >= max_bonus:
            max_bonus = total_bonus

print(f'Max Bonus: {round(max_bonus)}.')
print(f'The student has attended {max_attendance} lectures.')

