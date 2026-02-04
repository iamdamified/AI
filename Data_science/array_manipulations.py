# Chnage Shapes of Arrays, and Adding Dimensions
import numpy as np

# reshape
arr = np.array([1,2,3,4,5,6])
reshaped = arr.reshape((2,3))
reshaped1 = arr.reshape((3,2))
print(reshaped)
print(reshaped1)

# expansion into new axis
arr = np.array([1,2,3])
expanded = arr[:, np.newaxis]
print(expanded)


# Basic Arrays Operations

# 1. Element-wise
a = np.array([1,2,3])
b = np.array([4,5,6])
print(a+b)
print(a*b)
print(a/b)

# 2. Mathematical
arr = np.array([4,16,25])
print(np.sqrt(arr))
print(np.sum(arr))
print(np.mean(arr))
print(np.max(arr))



# Array Indexing, Slicing, and Reshaping
arr = np.array([10, 20, 30, 40, 50, 60])
print(arr[2])
print(arr[-1])
print(arr[1:4])
print(arr[3:])

reshaped = arr.reshape(2,3)
print(reshaped)


# Exercises
# generate arrays for basic mathematics operations

a = np.arange(1,6)
b = np.arange(6,11)
print("Add: ", a + b)
print("Add: ", a - b)
print("Add: ", a * b)
print("Add: ", a / b)


# Create a 3x3 matrix and perform operations

matrix = np.array([[1,2,3], [4,5,6], [7,8,9]])
print("Original Matrix: \n", matrix)

#Transpose Operation
transpose = matrix.T
print("Transpose: \n", transpose)


another_matrix = np.array([[9,8,7], []])
