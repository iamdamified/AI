#TASK 1
"""Perform Data Cleaning, Aggregation, and Filtering for this task a csv file dataset is provided"""
import pandas as pd
# Load the Titanic dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)
# Inspect dataset
print(df.head())
print(df.info())
print(df.describe())
# Data Cleaning: Handle missing values
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Remove Duplicate entries
df = df.drop_duplicates()
# df = df.dropna(subset=['Age', 'Embarked'])
# Filter data: Passengers in first class
first_class_passengers = df[df["Pclass"] == 1]
print(first_class_passengers.head())



#TASK 2
"""Generate Visualizations to illustrate Key Insights from the dataset. 
Use libraries such as Matplotlib or Seaborn to create visualizations to highlight trends and patterns in the data."""

import matplotlib.pyplot as plt
import seaborn as sns


# Visualization 1: Survival Rate by Passenger Class(Bar Chart)
survival_by_class = df.groupby("Pclass")["Survived"].mean()
survival_by_class.plot(kind="bar", color="skyblue")
plt.title("Survival Rate by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Survival Rate")
plt.xticks(rotation=0)
plt.show()


# Visualization 2: Age Distribution of Passengers (Histogram)
sns.histplot(df["Age"], bins=20, kde=True, color="purple")
plt.title("Age Distribution of Passengers")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()


# Scatter Plot: Age vs Fare colored by Survival
plt.scatter(df["Age"], df["Fare"], c=df["Survived"], cmap="coolwarm", alpha=0.6)
plt.title("Age vs Fare Colored by Survival")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.show()