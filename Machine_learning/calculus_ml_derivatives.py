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
# Define the grdient descent function
def gradient_descent(X, y, theta, learning_rate, iterations):
    m = len(y)  # number of training examples
    for i in range(iterations):
        predictions = np.dot(X, theta)  # predicted values
        errors = predictions - y     # errors
        gradient = (1/m) * np.dot(X.T, errors)  # compute the gradient
        theta -= learning_rate * gradient  # update parameters
    return theta

# Sample data
X = np.array([[1, 1], [1, 2], [1, 3]])  # feature matrix
y = np.array([2, 2.5, 3.5])  # target values
theta = np.array([0.1, 0.1])  # initial parameters
learning_rate = 0.01
iterations = 1000

# Run gradient descent
optimized_theta = gradient_descent(X, y, theta, learning_rate, iterations)
print("Optimized parameters:", optimized_theta)


# Additional Exercise
"""1. Use SymPy to compute the second-order derivatives of a function(Hessian Matrix)"""
# Define a multivariable function
x, y = sp.symbols('x y')
f = x**2 + y**2
# Compute second-order derivatives
hessian_xx = sp.diff(f, x, x)  # second derivative with respect to x
hessian_yy = sp.diff(f, y, y)  # second derivative with respect to y
hessian_xy = sp.diff(f, x, y)  # mixed second derivative
print("Hessian Matrix:")
print(f"[[{hessian_xx}, {hessian_xy}], [{hessian_xy}, {hessian_yy}]]")


"""2. Implement Gradient Descent with multiple learning rates and compare convergence speeds"""
import numpy as np
import matplotlib.pyplot as plt
def gradient_descent(X, y, theta, learning_rate, iterations):
    m = len(y)
    cost_history = []
    for i in range(iterations):
        predictions = np.dot(X, theta)
        errors = predictions - y
        gradient = (1/m) * np.dot(X.T, errors)
        theta -= learning_rate * gradient
        cost = (1/(2*m)) * np.sum(errors**2)  # compute cost
        cost_history.append(cost)
    return theta, cost_history
# Sample data
X = np.array([[1, 1], [1, 2], [1, 3]])
y = np.array([2, 2.5, 3.5])
initial_theta = np.array([0.1, 0.1])
learning_rates = [0.001, 0.01, 0.1]
plt.figure(figsize=(10, 6))
for lr in learning_rates:
    theta = initial_theta.copy()
    optimized_theta, cost_history = gradient_descent(X, y, theta, lr, 1000)
    plt.plot(cost_history, label=f'Learning Rate: {lr}')
plt.xlabel('Iterations')
plt.ylabel('Cost')
plt.title('Gradient Descent with Different Learning Rates')
plt.legend()
plt.show()


"""3. visualize the gradient descent process on a quadratic function"""
import numpy as np
import matplotlib.pyplot as plt
# Define the quadratic function
def f(x):
    return x**2 + 4*x + 4
# Compute the gradient
def gradient(x):
    return 2*x + 4
# Gradient descent implementation
def gradient_descent(starting_point, learning_rate, iterations):
    x = starting_point
    x_history = [x]
    for _ in range(iterations):
        grad = gradient(x)
        x -= learning_rate * grad
        x_history.append(x)
    return x_history
# Parameters
starting_point = 0.0
learning_rate = 0.1
iterations = 100
# Run gradient descent
x_history = gradient_descent(starting_point, learning_rate, iterations)
# Visualize the function and the gradient descent path
x_values = np.linspace(-10, 2, 400)
y_values = f(x_values)
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label='f(x) = x^2 + 4x + 4')
plt.scatter(x_history, [f(x) for x in x_history], color='red', label='Gradient Descent Path')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Gradient Descent on a Quadratic Function')
plt.legend()
plt.show()


