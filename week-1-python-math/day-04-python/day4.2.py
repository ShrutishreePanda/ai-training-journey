import numpy as np

def numpy_demo():
    print(" Creating Arrays")
    arr1 = np.array([1, 2, 3, 4])
    arr2 = np.array([5, 6, 7, 8])
    print("Array 1:", arr1)
    print("Array 2:", arr2)

    print("\n Basic Operations")
    print("Addition:", arr1 + arr2)
    print("Multiplication:", arr1 * arr2)

    print("\n Statistical Functions")
    print("Mean:", np.mean(arr1))
    print("Sum:", np.sum(arr1))
    print("Max:", np.max(arr1))

    print("\n Reshaping")
    arr3 = np.arange(1, 10).reshape(3, 3)
    print("3x3 Matrix:\n", arr3)

    print("\n Indexing & Slicing")
    print("First Row:", arr3[0])
    print("Element at (1,1):", arr3[1, 1])

    print("\n Transpose")
    print("Transpose:\n", arr3.T)

    print("\n Dot Product")
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    print("Dot Product:", np.dot(a, b))

    print("\n Random Numbers")
    rand_arr = np.random.randint(1, 10, size=(2, 3))
    print("Random Array:\n", rand_arr)

if __name__ == "__main__":
    numpy_demo()