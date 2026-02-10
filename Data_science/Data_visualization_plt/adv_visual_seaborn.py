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

