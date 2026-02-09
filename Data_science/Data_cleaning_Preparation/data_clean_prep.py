#Data cleaning and preparation is a crucial step in the data analysis process. 
#It involves handling missing values, removing duplicates, and transforming data to ensure it is in a suitable format for analysis. 
#Below are some common techniques for data cleaning and preparation using pandas.

"""1. Handling Missing Values Methods
- dropna(): Removes rows or columns with missing values.
- fillna(): Fills missing values with a specified value or method (e.g., forward fill, backward fill).
- isna(): Identifies missing values in the DataFrame.(Interpolation)"""
import pandas as pd
import numpy as np

df = df.dropna()  # Remove rows with missing values
df = df.dropna(axis=1)  # Remove columns with missing values
df['column_name'] = df['column_name'].fillna(0)  # Fill missing values with a specified value e.g mean, median, or mode

# then followed by the method to fill missing values using forward fill or backward fill
df.fillna(method='ffill')
df.fillna(method='bfill')
df['column_name'] = df['column_name'].fillna(method='ffill')  # Fill missing values using forward fill method
df['column_name'] = df['column_name'].fillna(method='bfill')  # Fill missing values using backward fill method

df["column_name"] = df["column_name"].interpolate(method='linear')  # Fill missing values using linear interpolation or empty function for default method


#Data Transformation Methods:
# Renaming columns
df.rename(columns={'old_name': 'new_name'}, inplace=True)
# Changing data types
df['column_name'] = df['column_name'].astype('int') # Convert to integer
df['column_name'] = df['column_name'].astype('float') # Convert to float
# Creating new columns based on existing ones
df['new_column'] = df['existing_column'] * 2  # Example: creating a new column by multiplying an existing column by 2
# Converting date columns to datetime format
df["column_name"] = pd.to_datetime(df["column_name"], format='%Y-%m-%d')  # Convert to datetime format



"Adcanced Data Cleaning and Preparation Methods:"
# Normalizing data
df['normalized_column'] = (df['column_name'] - df['column_name'].min()) / (df['column_name'].max() - df['column_name'].min())
# Standardizing data
df['standardized_column'] = (df['column_name'] - df['column_name'].mean()) / df['column_name'].std()
# Removing duplicates
df = df.drop_duplicates()  # Remove duplicate rows
# Removing outliers using Z-score
from scipy import stats
z_scores = stats.zscore(df['column_name'])
df = df[abs(z_scores) < 3]  # Remove rows with Z-score greater than 3 (outliers)




#Combining and Merging DataFrames:
# Concatenating DataFrames
combined_df = pd.concat([df1, df2], axis=0)  # Combine DataFrames vertically (stacking rows)
combined_df = pd.concat([df1, df2], axis=1)  # Combine DataFrames horizontally (stacking columns)
# Merging DataFrames
merged_df = pd.merge(df1, df2, on='common_column')  # Merge DataFrames based on a common column
merged_df = pd.merge(df1, df2, on='common_column', how='inner')  # Inner join (default)
merged_df = pd.merge(df1, df2, on='common_column', how='outer')  # Outer join
merged_df = pd.merge(df1, df2, on='common_column', how='left')  # Left join
merged_df = pd.merge(df1, df2, on='common_column', how='right')  # Right join
# Joining DataFrames
joined_df = df1.join(df2, how='inner') # Join DataFrames based on index (inner join)
joined_df = df1.join(df2, how='outer') # Join DataFrames based on index (outer join)
joined_df = df1.join(df2, how='left') # Join DataFrames based on index (left join)
joined_df = df1.join(df2, how='right') # Join DataFrames based on index (right join)




