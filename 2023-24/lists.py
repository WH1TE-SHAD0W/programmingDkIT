grades = []
for i in range(6):
    while True:
        grade = int(input('enter a grade here'))
        if 0 >= grade <= 100:
            grades.append(grade)
        else:
            break
