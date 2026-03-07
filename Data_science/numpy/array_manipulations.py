# Chnage Shapes of Arrays, and Adding Dimensions
import numpy as np

# reshape
arr = np.array([1,2,3,4,5,6])
reshaped = arr.reshape((2,3)) #reshape is used to define the dimensions of a matrix to be made from an array.
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

a = np.arange(1,6) #arange is used to define a particular range or contents for an array
b = np.arange(6,11)
print(a, b)
print("Add: ", a + b)
print("subtract: ", a - b)
print("multiply: ", a * b)
print("divide: ", a / b)


# Create a 3x3 matrix and perform operations

matrix = np.array([[1,2,3], [4,5,6], [7,8,9]])
print("Original Matrix: \n", matrix)

#Transpose Operation
transpose = matrix.T # .Transpose changes positions/interchange items of each list in an array.
print("Transpose: \n", transpose)


another_matrix = np.array([[9,8,7], [6,5,4], [3,2,1]])
print("Addition: \n", matrix + another_matrix)
print("Multiplication: \n", matrix * another_matrix)


#Practice
"""create 4x4 matrix, calculate sum of rows and columns."""
matrix_4x4 = np.arange(1,17).reshape(4,4)
print("4x4 Matrix: \n", matrix_4x4)
print("Sum of rows: ", np.sum(matrix_4x4, axis=1))
print("Sum of columns: ", np.sum(matrix_4x4, axis=0))

"""A program to normalize an array(scale values between 0 and 1)."""
def normalize(arr):
    min_val = np.min(arr)
    max_val = np.max(arr)
    normalized = (arr - min_val) / (max_val - min_val)
    return normalized
arr = np.array([10, 20, 30, 40, 50])
normalized_arr = normalize(arr)
print("Original array:", arr)
print("Normalized array:", normalized_arr)

"""Generate a random array and find the minimum and maximum values."""
random_arr = np.random.rand(5)
print("Random array:", random_arr)
print("Minimum value:", random_arr.min())# or np.max(random_arr)
print("Maximum value:", np.max(random_arr))
