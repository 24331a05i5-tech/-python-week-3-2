import numpy as np
a = np.ndarray(shape=(2,2), dtype=int)
a[:] = [[1,2],[4,5]]
print("Matrix 1 elements are:\n", a)
print("Dimension of matrix 1 is:", a.ndim)
b = np.ndarray(shape=(2,2), dtype=int)
b[:] = [[1,3],[2,5]]
print("Matrix 2 elements are:\n", b)
print("Dimension of matrix 2 is:", b.ndim)
print("Addition of 2 matrices:\n", np.add(a, b))
print("Subtraction of 2 matrices:\n", np.subtract(a, b))
print("Division of 2 matrices:\n", np.divide(a, b))
print("Matrix multiplication of 2 matrices:\n", np.dot(a, b))
