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
# plt.scatter(df["Age"], df["Fare"], color="green", alpha=0.5)#original scatter plot
plt.title("Age vs Fare Colored by Survival")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.show()



#TASK 3
"""Identify and Interpret Patterns and Anomalies using human understanding and interpretation
 of the graphics and statistical data produced in task1, and particularly in task 2."""
# Interpretation of Visualization 1: Survival Rate by Passenger Class
# The bar chart shows that passengers in first class (Pclass 1) had a significantly higher survival rate compared to those in second (Pclass 2) and third class (Pclass 3). This suggests that socio-economic status played a crucial role in survival chances during the Titanic disaster, with wealthier passengers having better access to lifeboats and safety measures. 
# Interpretation of Visualization 2: Age Distribution of Passengers
# The histogram reveals that the majority of passengers were between the ages of 20 and 40, with a noticeable peak around the age of 30. This indicates that the Titanic had a relatively young passenger demographic, which may have influenced survival rates, as younger passengers might have been more likely to survive due to better physical condition or being prioritized for lifeboats. 
# Interpretation of Scatter Plot: Age vs Fare colored by Survival
# The scatter plot shows a wide range of fares paid by passengers of different ages, with a noticeable cluster of survivors (colored in red) among those who paid higher fares, particularly in the age range of 20 to 40. This suggests that passengers who paid more for their tickets, likely those in first class, had a higher chance of survival. Additionally, there are some survivors among younger passengers who paid lower fares, indicating that age and fare both played a role in survival chances, but fare (and thus socio-economic status) appears to be a stronger predictor of survival. 


#TASK 4
"""Summarize Findings in a Report"""
# Summary of Findings: To create a report as a Data Scientist:
"""Open an editor e.g. VSCODE,Notepad, MSWord, PDF etc.

Title: Exploratory Data Analysis of the Titanic Dataset

1. Overview:
- Dataset contains 891 rows and 12 columns.
- Missing values handled for 'Age'(filled with median) and 'Embarked'(filled with mode) columns.

2. Key Insights:
- Survival rates are highest for first class passengers(62% survival rate), and lowest
for third class passengers(24% survival rate), indicating socio-economic status influenced survival chances.
- The majority of passengers were between 20 and 40 years old, with a peak around age 30, suggesting a relatively young demographic on board.
- A positive correlation exists between fare paid and survival, with higher fares (associated with first class) 
correlating with higher survival rates, while younger passengers with lower fares also had some chances of survival, indicating that both age and socio-economic status played roles in survival outcomes.

3. Visual Insights:
- Screenshots of the bar chart, histogram, and scatter plot are included to visually represent the findings.

4. Conclusion:
- The analysis of the Titanic dataset reveals significant patterns in survival rates based on passenger class, age, and fare paid. 
These insights highlight the importance of socio-economic factors in survival outcomes during the disaster, as well as the demographic characteristics of the passengers on board. 
Further analysis could explore additional factors such as gender and family size to gain a more comprehensive understanding of the survival dynamics."""


