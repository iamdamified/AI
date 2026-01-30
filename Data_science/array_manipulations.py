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
