import numpy as np

n = int(input("Enter number of students: "))

marks = []

for i in range(n):
    m = float(input(f"Enter marks for student {i+1}: "))
    marks.append(m)

marks_array = np.array(marks)

print("\nMarks:", marks_array)

print("Average marks:", np.mean(marks_array))
print("Highest marks:", np.max(marks_array))
print("Lowest marks:", np.min(marks_array))

result = np.where(marks_array >= 40, "Pass", "Fail")
print("Results:", result)