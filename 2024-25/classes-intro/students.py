class Student:
    name = 'Michelle'
    module = 'OO Programming'

    def print_name(self):
        return self.name

    def set_name(self, name):
        self.name = name


if __name__ == '__main__':
    person = Student()
    print(person.print_name())
    person.set_name('Mikey')
    print(person.print_name())
