employee_data = {}

while True:
    command = input()

    if command == "End":
        break

    company_name, employee_id = command.split(" -> ")

    if company_name not in employee_data:
        employee_data[company_name] = []

    if employee_id not in employee_data[company_name]:
        employee_data[company_name].append(employee_id)

for company, students in employee_data.items():
    print(f"{company}")
    for employee in students:
        print(f"-- {employee}")

