#Excercises:
import pandas as pd
import numpy as np
"""1. Clean a dataset by handling missing values, removing columns"""

# Create a sample dataset.
data = {'Name': ['Alice', 'Bob', np.nan, 'David'],
        'Age': [25, np.nan, 30, 35],
        'Score': [85, 90, np.nan, 88]}
df = pd.DataFrame(data)
print("Original DataFrame or dataset: \n", df)

# Handle missing values by filling them with the mean of the respective columns.
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Score'] = df['Score'].interpolate()  # Fill missing values using linear interpolation
print("\nDataFrame after handling missing values: \n", df)

df = df.rename(columns={"Name": "Student_Name", "Score": "Exam_Score"})  #drop to remove and rename to rename the 'Name' column to 'Student_Name' and 'Score' column to 'Exam_Score'
print("\nDataFrame after renaming columns: \n", df)


