def get_grades():
    grades = []
    for grade in range(int(input("how many grades do you have"))):
        grades.append(round(float(input("please write down your grade, here: ")), 2))
    return grades


def max_value(array: list):
    maximum = 0
    for i in array:
        if i > maximum:
            maximum = i
    return maximum


def min_value(array: list):
    minimum = max_value(array)
    for i in array:
        if i < minimum:
            minimum = i
    return minimum


def sort_grades(grades: list):
    grades_sorted = []
    for i in range(len(grades)):
        maximum = max_value(grades)
        grades_sorted.append(maximum)
        grades.remove(maximum)
    return grades_sorted


print(sort_grades(get_grades()))
