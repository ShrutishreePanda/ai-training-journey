import numpy as np

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter elements for Matrix A:")
A = []
for i in range(rows):
    row = list(map(int, input().split()))
    A.append(row)

print("Enter elements for Matrix B:")
B = []
for i in range(rows):
    row = list(map(int, input().split()))
    B.append(row)

A = np.array(A)
B = np.array(B)

print("\nMatrix A:\n", A)
print("Matrix B:\n", B)

print("\nAddition:\n", A + B)
print("Multiplication:\n", np.dot(A, B))
print("Transpose of A:\n", A.T)