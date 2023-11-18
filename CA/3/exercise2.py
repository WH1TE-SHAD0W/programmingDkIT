import random

employee_information = [[], [], [], [], [], [], [], [], [], []]

for employee in range(10):
    # name = str(input(f"write down name of your {employee + 1} employee"))
    # salary = int(input("write down his / her salary"))
    # day_offs = int(input("write down count of his leave days"))
    name = f"name{employee}"
    salary = random.randint(1000, 2000)
    day_offs = random.randint(10, 20)
    employee_information[employee].append(name)
    employee_information[employee].append(salary)
    employee_information[employee].append(day_offs)

lowest_leave_days = []
longest_name_employee = []
lowest_leave_days_count = employee_information[0][2]

for detail in range(3):
    longest_name_employee.append(employee_information[0][detail])

# lowest leave days the lowest number
for employee in employee_information:
    if employee[2] < lowest_leave_days_count:
        lowest_leave_days_count = employee[2]

# lowest leave days assigning
for employee in employee_information:
    if employee[2] == lowest_leave_days_count:
        lowest_leave_days.append(employee)

if len(lowest_leave_days) == 1:
    print(f"The name of the employee with lowest leave days: {lowest_leave_days[0][0]}, his salary: "
          f"{lowest_leave_days[0][1]}, and the number of leave days he took: {lowest_leave_days[0][2]}")
else:
    for employee_with_lowest_leave_days in lowest_leave_days:
        print(f"The name of one of employees with lowest leave days: {employee_with_lowest_leave_days[0]}, his salary:"
              f"{employee_with_lowest_leave_days[1]}, and the number of leave days he took: "
              f"{employee_with_lowest_leave_days[2]}")

# longest name
for employee in employee_information:
    if len(longest_name_employee[0]) > len(employee[0]):
        for detail in range(3):
            longest_name_employee[detail] = employee[detail]

print(f"The name of the employee with longest name: {longest_name_employee[0]}, his salary: "
      f"{longest_name_employee[1]}, and the number of leave days he took: {longest_name_employee[1]}")

# raise salary
for employee in range(len(employee_information)):
    for i in range(len(lowest_leave_days)):
        if employee_information[employee][0] == lowest_leave_days[i][0]:
            employee_information[employee][1] = round(employee_information[employee][1] * 1.1)
            lowest_leave_days[i][1] = round(lowest_leave_days[i][1] * 1.1)
            if lowest_leave_days[i][0] == longest_name_employee[0]:
                longest_name_employee[1] = round(longest_name_employee[1] * 1.1)

if len(lowest_leave_days) == 1:
    print(f"The name of the employee with lowest leave days: {lowest_leave_days[0][0]}, his salary after raise: "
          f"{lowest_leave_days[0][1]}, and the number of leave days he took: {lowest_leave_days[0][2]}")
else:
    for employee_with_lowest_leave_days in lowest_leave_days:
        print(f"The name of one of employees with lowest leave days: {employee_with_lowest_leave_days[0]}, his salary "
              f"after raise: {employee_with_lowest_leave_days[1]}, and the number of leave days he took: "
              f"{employee_with_lowest_leave_days[2]}")

