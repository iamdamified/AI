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

y_pred_prob = model.predict(X_test)
y_pred = (y_pred_prob > 0.5).astype("int32").flatten()
y_test = np.array(y_test)  # Ensure y_test is a numpy array

print("\n Predicted vs Actual values:")
print(f"{'Index':>5}{'Predicted':>10}{'Actual':>10}{'Probability':>12}")
print("-" * 40)
# Loop through Test Set
for i in range(len(X_test)):
    print(f"{i:>5}{y_pred[i]:>10}{y_test[i]:>10}{y_pred_prob[i][0]:>12.2f}") #run and a table will be displayed