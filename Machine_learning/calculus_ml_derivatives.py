"""Calculus for machine learning(Derivatives)

- Used for Optimization
- Derivatives measures the rate of change of a function with respect to its input variables
- In machine learning, derivatives are used to optimize the parameters of a model by minimizing a loss function
- The most common optimization algorithm that uses derivatives is Gradient Descent
- For a function f(x), the derivative f'(x) gives the slope of the tangent line to the function at any point x
- Role of Optimization in Machine Learning:
    - Optimization is the process of finding the best parameters for a model to minimize the loss function
- Common Derivatives:
    for f(x) = x**2, f'(x) = 2x
    for f(x) = sin(x), f'(x) = cos(x)"""

import numpy as np
import sympy as sp

x = sp.Symbol('x')
f = x**2
derivatives = sp.diff(f, x)
print(derivatives)  # Output: 2*x


""" Partial Derivatives

- Measure of how a function changes with respect to one variable while keeping other variables constant
- For a function f(x, y), x**2 + y**2, the partial derivatives are:
    - ∂f/∂x = 2x
    - ∂f/∂y = 2y"""


""" Gradients 
- Vector of all partial derivatives, indicating the direction of the steepest ascent of a function
- For a function f(x, y) = x**2 + y**2, the gradient is:
    - ∇f = [∂f/∂x, ∂f/∂y] = [2x, 2y]"""


x, y = sp.symbols('x y')
f = x**2 + y**2
grad_x = sp.diff(f, x)
grad_y = sp.diff(f, y)
print(grad_x)  # Output: 2*x
print(grad_y)  # Output: 2*y


""" Gradient Descent Optimization Algorithm
- Iterative optimization algorithm used to minimize a loss function by updating model parameters in the direction of the negative gradient
- Updates parameters in the direction of the negative gradient to minimize the loss function
- Update Rule: θ = θ - α * ∇J(θ)
    - θ: model parameters
    - α: learning rate/step size
    - ∇J(θ): gradient of the loss function with respect to the model parameters"""




""" Importance of Gradient Descent in Machine Learning----- EXERCISES"""

"""1. Compute derivatives of Basic Functions"""

# Define function
x = sp.Symbol('x')
f = x**3 - 5*x + 7

# Compute the derivative
derivative = sp.diff(f, x)
print(f)
print(derivative)


"""2. Compute Gradients"""

# Define a multivariable function
x, y = sp.symbols('x y')
f = x**2 + 3*y**2 - 4*x*y
# Compute partial derivatives/gradients
grad_x = sp.diff(f, x)
grad_y = sp.diff(f, y)
print("Partial derivative/Gradient with respect to x:", grad_x)
print("Partial derivative/Gradient with respect to y:", grad_y)


"""3. Implement Gradient Descent for a Linear Regression"""
# For this we have a function in numpy.
import numpy as np
