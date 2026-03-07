# # Broadcasting in Numpy

# #Allows numpy perform arithmetic operations on different shapes

# #Broadcasting rules:
# """1. Right Alignment Dimensions
# 2. Dimension is compatible if:
# - It matches the other array's dimension
# - One of the dimensions is 1"""

import numpy as np

# # Array and Scalar broadcasting
# arr = np.array([1,2,3])
# print(arr + 10)

# matrix = np.array([[1,2,3], [4,5,6]])
# vector = np.array([1,0,1])
# print(matrix + vector)


# # Aggregation Functions
# # Computes Summary statistics for arrays, common ones are:

# arr = np.array([[1,2,3], [4,5,6]])
# print("Sum: ", np.sum(arr))
# print("Mean: ", np.mean(arr))
# print("Max: ", np.max(arr))
# print("Min: ", np.min(arr))
# print("Standard Deviation: ", np.std(arr))
# print("Sum of rows: ", np.sum(arr, axis=1))
# print("Sum of columns: ", np.sum(arr, axis=0))


# # Boolean Indexing and Filtering
# arr = np.array([1,2,3,4,5,6])

# evens = arr[arr % 2 == 0]
# print("Evens: ", evens)

# arr[arr > 3] = 0
# print("Modified Array: ", arr)


# #Random Number Generation and Setting Seeds np.random
# random_array = np.random.rand(3,3)
# print("Random Array: \n", random_array)

# random_integers = np.random.randint(0, 10, size=(2,3))
# print("Random Integers: \n", random_integers)


# Setting Random Seeds
# np.random.seed(n), where n is any number
# This ensures random operations done below it will generate exact result(constant when same function is repeated many times; such as operations in previous page.)

# """1. Broadcasting Operations"""
# matrix = np.array([[1,2,3], [4,5,6], [7,8,9]])
# vector = np.array([1,0,-1])
# result_add = matrix + vector
# print("Add: \n", result_add)

# result_mul = matrix * 2
# print("Multiplication: \n", result_mul)


# """2. Generate and filter a random dataset"""
# dataset = np.random.randint(1,51, size=(5,5))
# print("Original: \n", dataset)

# #filter values > 25 and replace with 0
# dataset[dataset > 25] = 0
# print(dataset)

# #calculate summary stats
# print("Sum: ", np.sum(dataset))
# print("Mean: ", np.mean(dataset))
# print("Standard Deviation: ", np.std(dataset))


#Practice
# """Create a 3D random array and compute statistics along specific axis."""
# # array_3d = np.random.randint(3,4,5)#3D array with shape (3,4,5) - 3 blocks of 4 rows and 5 columns each
# array_3d = np.random.randint(1,10, size=(3,4,5))
# print("3D Array: \n", array_3d)
# print("3D Array Shape: ", array_3d.shape)# displays the dimensions of the array (3,4,5)
# print("Sum along axis 0: ", np.sum(array_3d, axis=0))# sums across the first dimension (3 blocks), resulting in a 4x5 array where each element is the sum of corresponding elements from the 3 blocks
# print("Sum along axis 1: ", np.sum(array_3d, axis=1))# sums across the second dimension (4 rows), resulting in a 3x5 array where each element is the sum of corresponding elements from the 4 rows within each block
# print("Sum along axis 2: ", np.sum(array_3d, axis=2))# sums across the third dimension (5 columns), resulting in a 3x4 array where each element is the sum of corresponding elements from the 5 columns within each block and row

# array_3d = np.random.randint(1, 10, size=(3,4,5))#3D array with shape (3,4,5) - 3 blocks of 4 rows and 5 columns each
# print("3D Array: \n", array_3d)
# print("3D Array Shape: ", array_3d.shape)# displays the dimensions of the array (3,4,5)
# print("Sum along axis 0: ", np.sum(array_3d, axis=0))# sums across the first dimension (3 blocks), resulting in a 4x5 array where each element is the sum of corresponding elements from the 3 blocks
# print("Sum along axis 1: ", np.sum(array_3d, axis=1))# sums across the second dimension (4 rows), resulting in a 3x5 array where each element is the sum of corresponding elements from the 4 rows within each block
# print("Sum along axis 2: ", np.sum(array_3d, axis=2))# sums across the third dimension (5 columns), resulting in a 3x4 array where each element is the sum of corresponding elements from the 5 columns within each block and row


"""Write a program to generate a dataset of random floats and normalize the values btw 0 and 1."""
dataset = np.random.rand(5,5)
print("Original Dataset: \n", dataset)

# # Normalize the dataset to range [0,1]
# normalized_dataset = (dataset - dataset.min()) / (dataset.max() - dataset.min())
# print("Normalized Dataset: \n", normalized_dataset)#


# """Implement conditional replacement to create a binary mask of values above a certain threshold."""
# threshold = 0.5
# binary_mask = dataset > threshold
# print("Binary Mask (values > 0.5): \n", binary_mask)# This creates a boolean array where True indicates values greater than 0.5 and False indicates values less than or equal to 0.5.
