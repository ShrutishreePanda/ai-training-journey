#class & objetcs

class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display(self):
        print(f"ID: {self.emp_id}, Name: {self.name}, Salary: {self.salary}")


emp_id = int(input("Enter Employee ID: "))
name = input("Enter Name: ")
salary = float(input("Enter Salary: "))

e = Employee(emp_id, name, salary)
e.display()