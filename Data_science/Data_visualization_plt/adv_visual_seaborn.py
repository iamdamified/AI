#Seaborn provides high-level interface for drawing attractive and informative statistical data/graphics. 
# It is built on top of Matplotlib and closely integrated with pandas data structures. 
# Seaborn provides a variety of functions for visualizing data, including:

#Heatmaps: Used to visualize the correlation between variables in a dataset.
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Create a sample dataset
data = np.random.rand(10, 10)
# Create a heatmap
sns.heatmap(data, annot=True, cmap='coolwarm')
plt.title("Heatmap Example")
plt.show()


#Pair Plots: Used to visualize the relationships between multiple variables in a dataset.
#1. Create a sample dataset
df = np.random.rand(5, 5)
sns.pairplot(df)
plt.show()

#2. Create a sample dataset
df = pd.DataFrame({
    'A': np.random.rand(100),
    'B': np.random.rand(100),
    'C': np.random.rand(100)
})
# Create a pair plot
sns.pairplot(df)
plt.suptitle("Pair Plot Example", y=1.02)
plt.show()

#Violin Plots: Used to visualize the distribution of a single variable or the relationship between two variables.
#1. Create a sample dataset
df = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'A', 'B', 'C'],
    'Value': [10, 20, 15, 12, 18, 14]
})
# Create a violin plot
sns.violinplot(x='Category', y='Value', data=df)
plt.show()


#Exercises:
"""1. Createbasic plots with matplotlib with customizations and produce different types of plots such as line graphs, bar charts, and scatter plots."""
import matplotlib.pyplot as plt

#Line plot
years = [2010, 2011, 2012, 2013, 2014]
sales = [10, 15, 20, 25, 30]
plt.plot(years, sales, marker='o', label='Sales Trend', color='blue')
plt.title("Sales Trend Over Years")
plt.xlabel("Year")
plt.ylabel("Sales")
plt.legend()
plt.grid()
plt.show()

#Bar chart
categories = ['A', 'B', 'C']
values = [10, 20, 15]
plt.bar(categories, values, color=['red', 'green', 'blue'])
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.show()


#Scatter plot
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.scatter(x, y, color='purple')
plt.title("Scatter Plot Example")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()




"""2. Create a heatmap with seaborn to visualize the correlation between variables in a dataset."""
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the dataset
df = pd.read_csv('filtered_iris.csv')  # Replace with your dataset path
# Calculate the correlation matrix
correlation_matrix = df.corr()
# Create a heatmap
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()
#This would produce a Heatmap except one of the columns in the dataset is non-numeric(data type), so it cannot be included in the correlation matrix. 
# To fix this, you can drop the non-numeric column before calculating the correlation matrix:
# Drop the non-numeric column

df_numeric = df.drop(columns=['species'])  # Replace 'species' with the name of your non-numeric column
#or del df['species']
# Calculate the correlation matrix
correlation_matrix = df_numeric.corr()
# Create a heatmap
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap (Numeric Columns Only)")
plt.show()