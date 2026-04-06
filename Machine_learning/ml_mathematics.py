# Linear Algebra Fundamentals
"""1. Vectors and Matrices"""
# vector is an array representing quantity and direction
#vector: [2,3,4]
#matrix: [[2, -3, 1]
        # [2, 0, -1]
        # [1, 4, 5]
        #]

"""Matrix Operations"""
import numpy as np

A = np.array([[1,2], [3,4]])
B = np.array([[5,6], [7,8]])

# Addition and Subtraction of matrices
print(A + B)
print("subtraction: ", A - B)

# Scalar Multiplication
C = 2 * A
print(C)

# Matrix multiplication
result = np.dot(A,B)
print(result)
#note: rows are cross multiplying with columns, and A rows multiplied by B columns

# Special Matrices
"""A. Identity Matrix(I) - I.A = A"""
I = np.eye(3)
print(I)
# note: run print repeatedly to get matrix changes(increase)

"""B. Zero Matrix(0)"""
Z = np.zeros((2,3))
print(Z)

"""C. Diagonal Matrix"""
D = np.diag([1,2,3])
print(D)



# Advanced Linear Algebra Concepts: Determinants and Inverse of a Matrix
"""1. Determinants of a Matrix
- A Scalar value that provides info about a matrix properties
- Only for Square Matrices
- det(A) = 0, the matrix A is singular
- det(A) != 0, A is invertible
- Geometric Interpretation:
i for a 2x2 matrix, the determinant represents the scaling factor of the area formed by it's column vectors
ii formula for 2x2 matrix- det([[a,b], [c,d]])= ad - bc"""

# Example:
A = np.array([[2,3], [1,4]])
determinant = np.linalg.det(A)
print(A)

"""2. Inverse of a Matrix
- Denoted as A-inverse
- Product of a matrix and it's inverse is the identity matrix: A x A-inverse = 1
- Matrix is invertible only if det(A) not= 0
- Formula for 2x2 2x2 matrix: A-inverse = 1/det(A)[[d, -b], [c, a]]"""

# Example
inverse = np.linalg.inv(A)
print("inverse of A: \n", inverse)




# EigenValues and EigenVectors
"""Eigen Vectors are vectors that doesn't change direction during transformation.
- Geometric Interpretation:
i Eigenvectors point in the direction where the matrix transformation stretches or compresses vectors
ii Eigenvalues indicate the factor of stretching or compression
- Properties:
i matrix of size nxn has nN eigenvalues and eigenvectors
ii Eigenvalues can be real or complex
iii For a symmetric matrix, eigenvalues are always real."""

# Computing Eigenvalues and Eigenvectors in NumPy: 
eigenvalues, eigenvectors = np.linalg.eig(A)
print(eigenvalues)
print(eigenvectors)


B = np.array([[4,2], [1,1]])
eigval, eigvec = np.linalg.eig(B)
print(eigval)
print(eigvec)




# Matrix Decomposition
"""Process of breaking a matrix into simpler components to analyze or solve problems.
1. Singular Value Decomposition(SVD)
decomposes a matrix A A into 3 matrices: A = U.E.Vt
U - Left singular vectors(orthogonal matrix)
E - Diagonal matrix of singular values(non-negative)
Vt - Right singular vectors(Orthogonal matrix)."""



# Applications of SVD

A = np.array([[2,3], [1,4]])
U, S, Vt = np.linalg.svd(A)
print("U: \n", U)
print("Singular Values: \n", S)
print("V Transpose: \n", Vt)

