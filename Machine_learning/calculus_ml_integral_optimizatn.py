"""Calculus for Machine Learning(Integrals and Optimization)"""

"""Integrals
- Compute the area under a curve, representing accumulation
- The definite integral of a function f(x) from a to b is denoted as ∫[a, b] f(x) dx


- Application in Machine Learning:
  - Probability distributions
  - Cost functions"""

import sympy as sp
x = sp.Symbol('x')
f = x**2
definite_integral = sp.integrate(f, (x, 0, 2))
print(definite_integral)  # Output: 8/3
indefinite_integral = sp.integrate(f, x)
print(indefinite_integral)  # Output: x**3/3



""" Optimization
- Local vs. Global Minima
    - Local Minimum(sometimes suffices)
    - Global Minimum(major essential calculation in optimization)

- Convex Functions
    - f(λx1 + (1-λ)x2) ≤ λf(x1) + (1-λ)f(x2) for all x1, x2 and λ in [0, 1]
    - Ensure that any local minimum is also a global minimum, simplifying optimization

- Non-convex Functions in ML: Neural networks, complex loss landscapes
    -most neural network loss functions are non-convex, leading to multiple local minima and saddle points, making optimization challenging"""




"""Stochastic Gradient Descent (SGD) and its Variants
- Optimization Algorithm that uses random subsets(mini-batches) of the data to compute gradients and update model parameters, improving efficiency and convergence in large datasets
- Why Use SGD?
    - For variants of SGD, the purposes are: 
        Mini-batch SGD: Balances efficiency and convergence by using small batches of data, reducing noise in gradient estimates compared to pure SGD while still being faster than full-batch gradient descent.
        Momentum: Accelerates convergence by adding a fraction of the previous update to the current update, helping to navigate ravines and avoid local minima.
        Adam: Combines the benefits of Momentum and RMSProp by maintaining adaptive learning rates for each parameter, improving convergence and performance in training deep learning models."""


#Exercises:
"""1. Calculate Integrals of Simple Functions"""
# Define the variable and function
x = sp.Symbol('x')
f = sp.exp(-x) 
# Compute the indefinite integral
indefinite_integral = sp.integrate(f, x)
print("Indefinite Integral:", indefinite_integral)
# Compute the definite integral from 0 to infinity
definite_integral = sp.integrate(f, (x, 0, sp.oo))
print("Definite Integral:", definite_integral)  


"""2. Implement Stochastic Gradient Descent (SGD) for a Linear Model"""
import numpy as np
# Generate synthetic data
np.random.seed(42)
X = 2 *np.random.randn(100, 1)
y = 4 + 3 * X + 1 + np.random.randn(100, 1)
# Add bias term to X
X_b = np.c_[np.ones((100, 1)), X]  # add bias term (intercept)
# SGD implementation
def stochastic_gradient_descent(X, y, learning_rate=0.01, n_epochs=