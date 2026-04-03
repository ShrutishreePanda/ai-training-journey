#Inheritance

class Person:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Name: {self.name}")


class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

    def display_student(self):
        self.display()
        print(f"Grade: {self.grade}")

name = input("Enter student name: ")
grade = input("Enter grade: ")

s = Student(name, grade)
s.display_student()