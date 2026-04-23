def add_student():
    students = []
    n = int(input("Enter number of students: "))

    for i in range(n):
        name = input("Enter name: ")
        marks = int(input("Enter marks: "))
        students.append({"name": name, "marks": marks})

    return students


def display_students(students):
    print("\nStudent List:")
    for s in students:
        print(f"{s['name']} - {s['marks']}")


def find_topper(students):
    topper = max(students, key=lambda x: x["marks"])
    print(f"\nTopper: {topper['name']} - {topper['marks']}")


students = add_student()
display_students(students)
find_topper(students)