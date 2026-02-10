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


"""2. Merge two datasets and perform data transformations"""
# Create two sample datasets.
data1 = {'ID': [1, 2, 3], 
         'Name': ['Alice', 'Bob', 'Charlie'],
         'Age': [25, 30, 35]
         }
data2 = {'ID': [1, 2, 3], 
         'Score': [85, 90, 88],
         }
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
print("\nDataFrame 1: \n", df1)
print("\nDataFrame 2: \n", df2)

# Merge the two datasets on the 'ID' column.
merged_df = pd.merge(df1, df2, on='ID', how='outer')
print("\nMerged DataFrame: \n", merged_df)

merged_df["Score_percentage"] = merged_df["Score"] / 100 * 100  # Create a new column 'Score_percentage' by transforming the 'Score' column to percentage.
print("\nDataFrame after adding Score_percentage column: \n", merged_df)


"""3. Drop columns with more than 50% missing values"""
# Create a sample dataset with missing values.
data = {'Name': ['Alice', 'Bob', np.nan, 'David'],
        'Age': [25, np.nan, 30, 35],
        'Score': [85, 90, np.nan, 88],
        'City': ['New York', np.nan, np.nan, np.nan]}
df = pd.DataFrame(data)
print("\nDataFrame with missing values: \n", df)

# Calculate the percentage of missing values in each column.
missing_percentages = (df.isnull().sum() / len(df)) * 100
print("\nMissing value percentages: \n", missing_percentages)

# Drop columns with more than 50% missing values.
columns_to_drop = missing_percentages[missing_percentages > 50].index
df_cleaned = df.drop(columns=columns_to_drop)
print("\nDataFrame after dropping columns with more than 50% missing values: \n", df_cleaned)



"""4. Merge 3 datasets and analyze relationships between them"""
# Create three sample datasets.
data1 = {'ID': [1, 2, 3], 
         'Name': ['Alice', 'Bob', 'Charlie'],
         'Age': [25, 30, 35]
         }
data2 = {'ID': [1, 2, 3], 
         'Score': [85, 90, 88],
         }
data3 = {'ID': [1, 2, 3], 
         'City': ['New York', 'London', 'Tokyo']
         }
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
df3 = pd.DataFrame(data3)
print("\nDataFrame 1: \n", df1)
print("\nDataFrame 2: \n", df2)
print("\nDataFrame 3: \n", df3)

# Merge the three datasets on the 'ID' column.
merged_df = pd.merge(df1, df2, on='ID', how='outer')
merged_df = pd.merge(merged_df, df3, on='ID', how='outer')
print("\nMerged DataFrame: \n", merged_df)

# Analyze relationships between columns.
correlation_matrix = merged_df.corr(numeric_only=True) # Calculate correlation matrix for numeric columns only
print("\nCorrelation Matrix: \n", correlation_matrix)



"""5. Convert categorical data to numerical data using one-hot encoding"""
# Create a sample dataset with categorical data.
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'City': ['New York', 'London', 'Tokyo', 'New York']}
df = pd.DataFrame(data)
print("\nOriginal DataFrame: \n", df)
# Convert the 'City' column to numerical data using one-hot encoding.
one_hot_encoded_df = pd.get_dummies(df, columns=['City'])
print("\nDataFrame after one-hot encoding: \n", one_hot_encoded_df)

# Analyze the relationships between the one-hot encoded columns.
correlation_matrix = one_hot_encoded_df.corr(numeric_only=True) # Calculate correlation matrix for numeric columns only
print("\nCorrelation Matrix for one-hot encoded columns: \n", correlation_matrix)
