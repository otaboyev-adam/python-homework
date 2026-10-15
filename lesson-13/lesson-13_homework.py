import numpy as np


# task 1

vector = np.arange(10, 50)
print("Task 1:")
print(vector)


# task 2
matrix = np.arange(0, 9).reshape(3, 3)
print("\nTask 2:")
print(matrix)

# task 3

identity = np.eye(3)
print("\nTask 3:")
print(identity)

# task 4

array3d = np.random.random((3, 3, 3))
print("\nTask 4:")

print(array3d)

# task 5
array10 = np.random.random((10, 10))
print("\nTask 5:")
print(array10)
print("Minimum:", array10.min())
print("Maximum:", array10.max())



# task 6
random_vector = np.random.random(30)
print("\nTask 6:")
print(random_vector)
print("Mean:", random_vector.mean())

# task 7
matrix5 = np.random.random((5, 5))
normalized = (matrix5 - matrix5.mean()) / matrix5.std()
print("\nTask 7:")
print("Original matrix:")
print(matrix5)
print("Normalized matrix:")
print(normalized)


# task 8
a = np.random.randint(1, 10, (5, 3))
b = np.random.randint(1, 10, (3, 2))
print("\nTask 8:")
print(a)
print(b)
print("Product:")

print(np.matmul(a, b))

# task 9
m1 = np.random.randint(1, 10, (3, 3))
m2 = np.random.randint(1, 10, (3, 3))
print("\nTask 9:")

print(m1)
print(m2)
print("Dot product:")
print(np.dot(m1, m2))

# task 10

matrix4 = np.arange(1, 17).reshape(4, 4)
print("\nTask 10:")
print(matrix4)

print("Transpose:")
print(matrix4.T)


# task 11

matrix_det = np.array([[2, 0, 1],
                       [1, 3, 2],
                       [1, 1, 4]])
print("\nTask 11:")
print(matrix_det)
print("Determinant:", np.linalg.det(matrix_det))


# task 12
A = np.random.randint(1, 10, (3, 4))
B = np.random.randint(1, 10, (4, 3))
print("\nTask 12:")
print(A)
print(B)
print("A * B:")
print(np.dot(A, B))



# task 13
matrix_r = np.random.randint(1, 10, (3, 3))
column = np.random.randint(1, 10, (3, 1))
print("\nTask 13:")
print(matrix_r)
print(column)

print("Matrix-vector product:")
print(np.dot(matrix_r, column))

# task 14

A = np.array([[2, 1, -1],
              [-3, -1, 2],
              [-2, 1, 2]])
b = np.array([[8], [-11], [-3]])
x = np.linalg.solve(A, b)
print("\nTask 14:")
print("A:")
print(A)
print("b:")
print(b)
print("Solution x:")
print(x)


# task 15
matrix_s = np.random.randint(1, 10, (5, 5))
print("\nTask 15:")
print(matrix_s)
print("Row sums:", matrix_s.sum(axis=1))
print("Column sums:", matrix_s.sum(axis=0))
