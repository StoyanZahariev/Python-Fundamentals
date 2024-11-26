students_grades_amount = int(input())

students_average_grades = {}

for _ in range(students_grades_amount):
    name = input()
    grade = float(input())

    if name not in students_average_grades:
        students_average_grades[name] = []

    students_average_grades[name].append(grade)

for name, grades in students_average_grades.items():
    average_grade = sum(grades) / len(grades)
    if average_grade >= 4.50:
        print(f"{name} -> {average_grade:.2f}")


