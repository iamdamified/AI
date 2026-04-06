"""1. Calculate Determinant and inverse of matrices"""
import numpy as np
A = np.array([[2,3,4], [4,5,6], [7,8,9]])

determinant = np.linalg.det(A)
inverse = np.linalg.inv(A)
print(determinant)
print(inverse)

"""2. Compute Eigenvalues and Eigenvectors"""
A = np.array([[4,-2], [1, 1]])

eigvals, eigvecs = np.linalg.eig(A)
print("Eigenvalues:", eigvals)
print("Eigenvectors:\n", eigvecs)

"""3. Perform Singular Value Decomposition (SVD)"""
A = np.array([[3,1,1], [-1,3,1], [1,1,3]])

U, s, Vt = np.linalg.svd(A)
print("U:\n", U)
print("Singular values:", s)
print("V transpose:\n", Vt)


"""Reconstruct Original Matrix Arrays (A) from SVD Components using Singular Value (s)"""
Sigma = np.zeros((3,3))     #zero array with equivalent
np.fill_diagonal(Sigma, s)  #Apply single value(s)
A_reconstructed = U @ Sigma @ Vt    #Then use new matrix to fetch original
print("Reconstructed A:\n", A_reconstructed)    



#Additional Practice Exercise
"""1. Compute evalues and evectors for larger matrices"""

# METHOD 1: 
# For General Square Matrices(use numpy's linalg.eig function)
# Example: larger random matrix
A = np.random.rand(100, 100)

eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues shape:", eigenvalues.shape)
print("Eigenvectors shape:", eigenvectors.shape)

# eigenvalues[i] corresponds to eigenvectors[:, i]
# Works for non-symmetric matrices
# May return complex numbers


# METHOD 2: 
# Symmetric / Hermitian matrices (Recommended)
# If your matrix is symmetric (real) or Hermitian (complex), use np.linalg.eigh — it is faster and more numerically stable:
# Symmetric matrix
A = np.random.rand(100, 100)
A = (A + A.T) / 2  # make it symmetric

eigenvalues, eigenvectors = np.linalg.eigh(A)

print("Eigenvalues shape:", eigenvalues.shape)
print("Eigenvectors shape:", eigenvectors.shape)

print("Eigenvalues shape:", eigenvalues)
print("Eigenvectors shape:", eigenvectors)

# Eigenvalues are always real
# Better performance for large matrices
# Common in PCA, covariance matrices, physics


# METHOD 3: 
# Very large matrices (Top-k eigenvalues)
# For very large matrices (e.g. 10,000 × 10,000), computing all eigenvalues is inefficient.
# Instead, compute only the largest k eigenvalues.
# Using SciPy (recommended for large-scale work)

from scipy.sparse.linalg import eigs

A = np.random.rand(1000, 1000)
k = 5  # number of eigenvalues

eigenvalues, eigenvectors = eigs(A, k=k)
print("Eigenvalues shape:", eigenvalues.shape)
print("Eigenvectors shape:", eigenvectors.shape)

# For symmetric matrices:

from scipy.sparse.linalg import eigsh

eigenvalues, eigenvectors = eigsh(A, k=5)
print("Eigenvalues shape:", eigenvalues.shape)
print("Eigenvectors shape:", eigenvectors.shape)


# METHOD 4:
# Sparse matrices (memory efficient)

from scipy.sparse import random
from scipy.sparse.linalg import eigs

A_sparse = random(5000, 5000, density=0.001)
eigenvalues, eigenvectors = eigs(A_sparse, k=3)

# Essential for graph algorithms, recommender systems, NLP



"""2. Use Singular Value Decomposition(SVD) to reduce the dimensionality of a dataset"""

# Step 1: Load dataset using numpy tool(e.g., from a CSV file)
# Example dataset: 100 samples, 10 features
np.random.seed(42)
X = np.random.rand(100, 10)

print(X.shape)  # (100, 10)

# Step 2: Center the data (subtract the mean)(VERY IMPORTANT)
# SVD-based dimensionality reduction assumes zero-mean features.
X_centered = X - np.mean(X, axis=0)
print(X_centered.shape)  # (100, 10)

# Step 2: Perform/Apply SVD
U, S, Vt = np.linalg.svd(X_centered, full_matrices=False)

print(U.shape)   # (100, 10) #left singular vectors (samples)
print(S.shape)   # (10,)    #singular values (importance of each dimension)
print(Vt.shape)  # (10, 10) #right singular vectors (principal directions/original features)

# Step 3: Select top k singular values and corresponding vectors
k = 2 # number of dimensions to keep

U_k = U[:, :k]       # (100, 2)
S_k = S[:k]          # (2,)
Vt_k = Vt[:k, :]     # (2, 10)
print(U_k.shape)   # (100, 2)
print(S_k.shape)   # (2,)
print(Vt_k.shape)  # (2, 10)


# Project data onto new lower 2-dimensions(data has now decome 2-dimensional)
X_reduced = U[:, :k] @ np.diag(S[:k])

print(X_reduced.shape)  # (100, 2)



# Explained Variance ratio (Optional)
explained_variance_ratio = (S**2) / np.sum(S**2)
print(explained_variance_ratio[:k])

"""- Why SVD works for dimensionality reduction

SVD finds orthogonal directions of maximum variance
Keeping top k singular values preserves most structure
This is mathematically equivalent to PCA when data is centered

- When to prefer SVD

Large dense datasets
Numerical stability
PCA without covariance matrix
Feature reduction


- Real-world uses
PCA for ML preprocessing
Noise reduction
Image compression
Latent semantic analysis (LSA)
Recommendation systems"""




"""3. Verify the property of evalues: det(A-λI) = 0 (known as characteristic equation)"""
# Define a square matrix A using numpy
A = np.array([[4, 2],
              [1, 3]])
# Compute eigenvalues using numpy
eigenvalues = np.linalg.eigvals(A)
print("Eigenvalues:", eigenvalues)
# Verify the property det(A - λI) = 0 for each eigenvalue
I = np.eye(A.shape[0])  # Identity matrix of the same size as A
for λ in eigenvalues:
    determinant = np.linalg.det(A - λ * I)
    print(f"Determinant of (A - {λ}I): {determinant}")