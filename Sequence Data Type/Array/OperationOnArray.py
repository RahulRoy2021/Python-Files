import array as arr
#  import numpy as arr another way of defining nd array
"""Data types: NumPy arrays can store elements of different data types, \
    while array arrays are limited to storing elements of a single data type. \
    For example, a NumPy array can store integers, floats, and other data types in the same array,\
    while an array array can only store one type of data, such as integers.
Multidimensional support: NumPy arrays support multidimensional arrays, \
    while array arrays are limited to one-dimensional arrays. \
    NumPy arrays can have any number of dimensions, and can be used to represent matrices, \
    tensors, and other multidimensional arrays."""
# creating an array of integers
a = arr.array('i', [1, 2, 3, 4, 5]) #'i 'indicates integer array ;'f indicates float array
print("Array of integers:",a)

# accessing elements of an array using index
print("First element of the array:", a[0])
print("Last element of the array:", a[-1])

# modifying elements of an array using index
a[0] = 10
a[-1] = 50
print("Modified array:", a)

# slicing an array to get a subset of its elements
subset = a[2:4]
print("Subset of the array:", subset)

# appending elements to an array
a.append(6)
print("Array after appending an element:", a)

# inserting elements into an array at a specific index
a.insert(2, 7)
print("Array after inserting an element:", a)

# removing elements from an array by value
a.remove(7)
print("Array after removing an element:", a)

# removing elements from an array by index
a.pop(3)
print("Array after removing an element using index:", a)

# getting the length of an array
print("Length of the array:", len(a))

# iterating over an array using a for loop
for element in a:
    print(element)
