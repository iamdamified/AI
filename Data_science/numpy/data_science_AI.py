# Into to Numpy for Numerical Computing
# Advanced NumPy Operations

#Advantages- performance, ease of use, integration

# creating and manipulating numpy arrays below:

import numpy as np

#creating array from a List
arr = np.array([1, 2, 3, 4])
print(arr)

#using built-in functions
zeroes = np.zeros((3, 3))
print(zeroes)

ones = np.ones((2, 4))
print(ones)

#for processing range of values
range_array = np.arange(1, 10, 2)# count 1 to 10 with step of 2
print(range_array)

range_array = np.arange(1, 10, 3)# count 1 to 10 with step of 3
print(range_array)

#for line space division
linspace_array = np.linspace(0, 1, 5) # 5 values between 0 and 1 equally spaced
print(linspace_array)
linspace_array = np.linspace(0, 10, 5) # 5 values between 0 and 10 equally spaced
print(linspace_array)
linspace_array = np.linspace(0, 10, 4) # 4 values between 0 and 10 equally spaced
print(linspace_array)
linspace_array = np.linspace(0, 10, 3) # 4 values between 0 and 10 equally spaced
print(linspace_array)