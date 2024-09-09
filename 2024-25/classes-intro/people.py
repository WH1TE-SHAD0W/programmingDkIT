class Person:
    def __init__(self, first_name: str, last_name: str, age: int, left_handed: bool):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.left_handed = left_handed


p1 = Person('Marek', 'Culak', 20, True)


class Student(Person):
    name = ''


s1 = Student('Marek', 'Culak', 20, True)
print(s1.last_name)
