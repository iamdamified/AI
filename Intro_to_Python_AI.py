# Python AI Libraries Introduction
"""1. NumPy: A fundamental package for scientific computing with Python. It provides support for arrays, matrices, and many mathematical functions.
2. Pandas: A powerful data manipulation and analysis library that provides data structures like DataFrames for handling structured data.
3. Matplotlib: A plotting library for creating static, animated, and interactive visualizations in Python.
4. Scikit-learn: A machine learning library that provides simple and efficient tools for data mining and data analysis, built on NumPy, SciPy, and Matplotlib.
5. TensorFlow: An open-source library developed by Google for numerical computation and large-scale machine
6. PyTorch: An open-source machine learning library developed by Facebook's AI Research lab, known for its dynamic computation graph and ease of use. learning and deep learning applications.
7. Keras: A high-level neural networks API, written in Python and capable of running on top of TensorFlow, CNTK, or Theano.
8. OpenCV: An open-source computer vision and machine learning software library that provides tools for real-time image processing.
9. NLTK (Natural Language Toolkit): A library for natural language processing that provides tools for working with human language data (text).
10. SpaCy: An open-source library for advanced natural language processing in Python, designed specifically for production use.
These libraries form the backbone of many AI applications and are widely used in the industry for various tasks such as data analysis, machine learning, deep learning, computer vision, and natural language processing."""

# To begin you need to install these libraries using pip if you haven't already:
# pip install numpy pandas matplotlib seaborn scikit-learn tensorflow torch keras opencv-python nltk spacy
# You can also install Jupyter Notebook or JupyterLab for an interactive coding environment:
# pip install jupyter or pip install jupyter notebook
# optional: pip install jupyterlab, pip install notebook, pip install google-colab, pip install plotly, pip install pillow, pip install scipy, pip install statsmodels, etc.


# Machine Learning Steps
"""1. Data Collection: Gather relevant data from various sources to be used for training and testing the machine learning model.
2. Separate features from target variable: Identify and separate the input features (independent variables) from the target variable (dependent variable) that you want to predict.
3. Data Preprocessing: Clean and preprocess the data to handle missing values, outliers, and categorical variables. This step may also include normalization or standardization of data.
4. Data Splitting: Divide the dataset into training and testing sets to evaluate the model's performance on unseen data.
5. Model Selection: Choose an appropriate machine learning algorithm based on the problem type (classification, regression, clustering, etc.) and the nature of the data.
6. Model Training(Make Predictions): Train the selected model using the training dataset by feeding the input features and target variable to the algorithm.
7. Model Evaluation(Testing on a single dataset): Assess the model's performance using the testing dataset and relevant evaluation metrics (e.g., accuracy, precision, recall, F1-score for classification; mean squared error, R-squared for regression).
8. Hyperparameter Tuning(Determining Accuracy): Optimize the model's hyperparameters to improve its performance using techniques such as grid search or random search.
9. Model Deployment: Deploy the trained model into a production environment where it can make predictions on new, unseen data.
10. Monitoring and Maintenance: Continuously monitor the model's performance in production and update it as needed to ensure it remains accurate and effective over time."""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score


# Neural Network Training Steps
"""1. Tensorflow layers, No of neurons, Activation Function for input, hidden, and output code lines.
2. Compile and train the model with optimizer, loss function, and metrics.
- Using Compile Method, involving Optimizer function-"adam", Loss Function-"binary_crossentropy", Metrics Function-['accuracy]
- Using Fit Function, involving "epochs"/"passes" variable, and "batch_size" variable, "validation_split"/test variable- usually=0.2(20%)
3. Use Model to make predictions on test set.
y_pred_prob = model.predict(X_text) for predicted probabilities
and y_pred = (y_pred_prob > 0.5).astype("int32").flatten() for conversion of probabilities to binary predictions & array flattening.
4. y_test must be a numpy array for accuracy calculation, and avoid indexing issues."""

# y_pred_prob = model.predict(X_test)
# y_pred = (y_pred_prob > 0.5).astype("int32").flatten()
# y_test = np.array(y_test)  # Ensure y_test is a numpy array

# print("\n Predicted vs Actual values:")
# print(f"{'Index':>5}{'Predicted':>10}{'Actual':>10}{'Probability':>12}")
# print("-" * 40)
# # Loop through Test Set
# for i in range(len(X_test)):
#     print(f"{i:>5}{y_pred[i]:>10}{y_test[i]:>10}{y_pred_prob[i][0]:>12.2f}") #run and a table will be displayed


# The above will not run as-is since 'model', 'X_test', and 'y_test' are not defined in this snippet.
# They are placeholders to illustrate the steps involved in neural network training and prediction.
# Ensure to define and train your model, and prepare your test data accordingly before using this code like below.

"""from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris

# Load data
data = load_iris()
X = data.data
y = data.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ✅ DEFINE THE MODEL
model = LogisticRegression(max_iter=200)

# ✅ TRAIN THE MODEL
model.fit(X_train, y_train)

# ✅ PREDICT
y_pred_prob = model.predict(X_test)

print(y_pred_prob)


5. Evaluate the model's performance
y_pred = (model.predict(X_test) > 0.5).astype("int32")

6. Calculate Evaluation Metrics
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")
Accuracy: 95.50%"""


# Computer Vision Libaries and Operations
"""1. OpenCV (Open Source Computer Vision Library): A widely used library for computer vision tasks, including image and video processing, object detection, and facial recognition."""
#First, do "pip install opencv-python matplotlib"
import cv2 #for image processing
from matplotlib import pyplot as plt 
# import matplotlib.pyplot as plt

"""2. Load an image using cv2 path"""
image_path = 'tablesetting_prod.png'  # Replace with your image path
image = cv2.imread(image_path)

"""3. Convert BGR to RGB or Grayscale for displaying correctly with matplotlib"""
# image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

"""4. Apply Gausian blur to image"""
blurred_image = cv2.GaussianBlur(image_gray, (5, 5), 0)

"""5. Detect edges using Canny Edge Detection Algorithm"""
edges = cv2.Canny(blurred_image, 50, 150)

"""6. Display original and processed images using matplotlib"""
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Edge Detected Image')
plt.imshow(edges, cmap='gray')
plt.axis('off')

plt.show()