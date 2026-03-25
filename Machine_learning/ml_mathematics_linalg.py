import numpy as np
"""1. create vectors and matrices using NumPy"""
# create matrices:
A = np.array([[1,2], [3,4]])
B = np.array([[9,8], [7,6]])

# Addition
print(A + B)

# Subtraction
print(A - B)

# Scalar Multiplication
print(3 * A)




"""2. Implement Matrix-Vector multiplication"""
# create matrix and vector
M = np.array([[1,2,3], [4,5,6], [7,8,9]])
V = np.array([1,0,-1])

# M-V Multiplication
result = np.dot(M, V)
print(result)




"""Explore Special Matrices"""
# a.  Identity Matrix
I = np.eye(3)
A = np.array([[1,2,3], [4,5,6], [7,8,9]])
print("A x I: \n", np.dot(A, I))

#note: I multiplied by A = A in an Identity matrix.


# b. Diagonal and Zero Matrix

D = np.diag([1,7,9])
Z = np.zeros((3,3))
print(D)
print(Z)


# Additional Exercise
"""1. Compute the determinant and inverse of a 2x2 matrix using NumPy"""
# 2x2 matrix
A = np.array([[4, 7],
              [2, 6]])

# compute the determinant
determinant = np.linalg.det(A)
print("Determinant:", determinant)

# compute the inverse with a conditional statement(if determinant not= 0)
if determinant != 0:
    inverse = np.linalg.inv(A)
    print(inverse)
else:
    print("Singular matrix has no inverse")



"""2. Verify properties of matrix multiplication"""
# matrix setup

A = np.array([[1,2],
              [3,4]])
B = np.array([[5,6],
              [7,8]])
C = np.array([[2,0],
              [1,2]])

# Associative Property (A.B).C = A.(B.C)
left = (A @ B) @ C
right = A @ (B @ C)
print(np.allclose(left, right))

# Distributive Porperty A.(B+C) = A.B + A.C
left = A @ (B + C)
left = (A @ B) + (A @ C)
print(np.allclose(left, right))

# Non-Commutative Property A · I = I · A = A
AB = A @ B
BA = B @ A
print("A @ B:\n", AB)
print("A @ B:\n", BA)
print("Are they equal?", np.array_equal(AB, BA))

# Identity Property
I = np.eye(2)

print(np.allclose(A @ I, A))
print(np.allclose(I @ A, A))

# Zero Matrix Property A . 0 = 0 . A = 0
Z = np.zeros((2, 2))
print(np.allclose(A @ Z, Z))
print(np.allclose(Z @ A, Z))



"""3. Create a block diagonal matrix using NumPy"""
# Using SciPy
from scipy.linalg import block_diag

A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6, 7],
              [8, 9, 10]])
C = np.array([[11]])

block_matrix = block_diag(A, B, C)
print(block_matrix)

# Using Numpy Only(Manual Construction)
A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])
block_matrix = np.zeros((4, 4), dtype=int)
block_matrix[:2, :2] = A
block_matrix[:2, :2] = B
print(block_matrix)

# Using np.block()(Flexible)
A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5]])
Z1 = np.zeros((2, 1))
Z2 = np.zeros((1, 2))

block_matrix = np.block([[A, Z1],
                         [Z2, B]])
print(block_matrix)