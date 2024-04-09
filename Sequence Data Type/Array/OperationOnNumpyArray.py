import numpy as np

# Creating arrays
a = np.array([1, 2, 3])
b = np.zeros((3,3))
c = np.ones((2,3))
d = np.array([[4, 5, 6], [7, 8, 9]])
e = np.array([[0, 1, 2], [3, 4, 5]])

# Indexing and Slicing
print(a[0])
print(a[1:3])
print(a[:3])
print(a[2:])
print(a[-1])
print(b[0,1])
print(c[1,:])

# Shape and Size
print(a.shape)
print(b.size)
print(c.ndim)
print(a.dtype)
print(b.itemsize)

# Reshaping
print(b.reshape((1,9)))
print(b.flatten())
print(b.ravel())
print(b.transpose())
print(c.swapaxes(0,1))

# Arithmetic operations
print(a + 2)
print(a - 2)
print(a * 2)
print(a / 2)
print(np.sin(a))
print(np.exp(a))

# Broadcasting
print(a + np.array([1, 2, 3]))
print(a * np.array([[1], [2], [3]]))

# Creating nd arrays
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
c = np.array([[9, 10], [11, 12]])

# Concatenation
print(np.concatenate((a, b), axis=0))
print(np.concatenate((a, b), axis=1))
print(np.vstack((a, b))) # equivalent to axis=0 concatenation
print(np.hstack((a, b))) # equivalent to axis=1 concatenation

# Comparison and Logical operations
print(a > 2)
print(np.logical_and(a < 2, b > 0))
print(np.logical_or(a == 2, c != 0))