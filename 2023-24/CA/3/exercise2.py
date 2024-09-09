# importing random for input generating for testing
# import random

# plain employee information table created for 10 people manually
employee_information: list[list, list, list, list, list, list, list, list, list, list] = [[], [], [], [], [], [], [],
                                                                                          [], [], []]

# loop which implements the data into that table either from the user or randomly generated via random library for
# testing purpose. At first, it creates temporary variables for all details then it appends them into one element of
# that table (relatively, every detail is a column in one row, the row is one employee).
for employee in range(10):
    name: str = str(input(f"write down name of your {employee + 1} employee"))
    salary: int = int(input("write down his / her salary"))
    day_offs: int = int(input("write down count of his leave days"))
    # name: str = f"name{employee}"
    # salary: int = random.randint(1000, 2000)
    # day_offs: int = random.randint(10, 20)
    employee_information[employee].append(name)
    employee_information[employee].append(salary)
    employee_information[employee].append(day_offs)

# creating empty tables for employees who got the lowest leave days count and longest name, it is a table containing
# all details of a creating employee. The reason why is it a table (two dimensioned list) is due the possibility
# there are employees with the same attributes
lowest_leave_days: list = []
longest_name_employee: list = []

# just a default number of the recorded lowest leave days for further comparing and a number of the count of
# characters of the longest name
lowest_leave_days_count: int = employee_information[0][2]
longest_name_chr_count: int = len(employee_information[0][0])

# loop cycle for finding the highest number of count of characters used for a employee name and finding the lowest
# number of employee leave days taken
for employee in employee_information:
    if len(employee[0]) > longest_name_chr_count:
        lowest_leave_days_count: int = len(employee[0])
    if employee[2] < lowest_leave_days_count:
        lowest_leave_days_count: int = employee[2]

# adding certain employee with such information to those tables created, it's comparing certain details and adding
# them the whole employee data into that table
#
# this could be easily than in database through referencing ids of rows in any table

for employee in employee_information:
    if employee[2] == lowest_leave_days_count:
        lowest_leave_days.append(employee)
    if len(employee[0]) == longest_name_chr_count:
        longest_name_employee.append(employee)

# displaying sentences of details about employee who had the lowest leave days recorded if he is one than it's a
# different sentence than if they were more
if len(lowest_leave_days) == 1:
    print(f"The name of the employee with lowest leave days: {lowest_leave_days[0][0]}, his salary: "
          f"{lowest_leave_days[0][1]}, and the number of leave days he took: {lowest_leave_days[0][2]}")
else:
    for employee_with_lowest_leave_days in lowest_leave_days:
        print(f"The name of one of employees with lowest leave days: {employee_with_lowest_leave_days[0]}, his salary:"
              f"{employee_with_lowest_leave_days[1]}, and the number of leave days he took: "
              f"{employee_with_lowest_leave_days[2]}")

# doing the same thing as if statement just before but for the longest name
if len(longest_name_employee) == 1:
    print(f"The name of the employee with longest name: {longest_name_employee[0][0]}, his salary: "
          f"{longest_name_employee[0][1]}, and the number of leave days he took: {longest_name_employee[0][2]}")
else:
    for employee_with_longest_name in longest_name_employee:
        print(f"The name of one of employees with the longest name: {employee_with_longest_name[0]}, his salary:"
              f"{employee_with_longest_name[1]}, and the number of leave days he took: "
              f"{employee_with_longest_name[2]}")

# loop is multiplying the data of salary  of each of those employees with the lowest leave days taken. In each table,
# the main and the separate table made for these people who have the lowest number of leave days. There it should
# also do such thing for the table of the longest name if the same employee is there, well yeah this is the point
# where referencing is needed as the database would allow me to do such things. But I know that these employees
# salaries are not going to be used anywhere else, so I just didn't implement it there
for employee in range(len(employee_information)):
    for i in range(len(lowest_leave_days)):
        if employee_information[employee][0] == lowest_leave_days[i][0]:
            employee_information[employee][1] = round(employee_information[employee][1] * 1.1)
            lowest_leave_days[i][1] = round(lowest_leave_days[i][1] * 1.1)

# displaying all that data whose salaries have been raised
if len(lowest_leave_days) == 1:
    print(f"The name of the employee with lowest leave days: {lowest_leave_days[0][0]}, his salary after raise: "
          f"{lowest_leave_days[0][1]}, and the number of leave days he took: {lowest_leave_days[0][2]}")
else:
    for employee_with_lowest_leave_days in lowest_leave_days:
        print(f"The name of one of employees with lowest leave days: {employee_with_lowest_leave_days[0]}, his salary "
              f"after raise: {employee_with_lowest_leave_days[1]}, and the number of leave days he took: "
              f"{employee_with_lowest_leave_days[2]}")

# just displaying the main table
# for employee in employee_information:
#     print(employee)

# general note: optimal thing would be to make a class of 'employee' with functions
