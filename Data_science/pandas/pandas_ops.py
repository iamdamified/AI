# #1. Load and explore a sample dataset.
# # """data file: https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"""

import pandas as pd
# Load dataset:
csv_url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(csv_url)

# Explore structure:
print("first 5 rows:\n", df.head())
print("\nlast 5 rows:\n", df.tail())
print("\nsummary info:\n", df.info())#data types, non-null counts, memory usage, columns, entries etc.
print("\ndescriptive stats:\n", df.describe())#count, mean, std, min, 25%, 50%, 75%, max for numeric columns
print("\ncolumn names:\n", df.columns)


#2. Select specific columns and filter rows based on conditions.
selected_columns = df[["sepal_length", "species"]]
print("\nselected columns:\n", selected_columns)
filtered_rows = df[(df["sepal_length"] > 5.0) & (df["species"] == "setosa")]
print("\nfiltered rows:\n", filtered_rows)


#Practice

"""Save filtered DataFrame to a new CSV file."""
filtered_rows.to_csv("filtered_iris.csv", index=False)
print("Filtered DataFrame saved to filtered_iris.csv")



"""Load a local Excel file, and explore its structure."""
excel_file = "printer.xlsx" # This file should be in the same directory as this script, or provide the full path to the file.
# excel_file = r"C:\Users\HP\Desktop\AI\Data_science\pandas\printer.xlsx"#This full path helps ensure file is found where it is.
df_excel = pd.read_excel(excel_file)
print("Excel file structure:")
print(df_excel.head())
print(df_excel.info())



"""Create a DataFrame from a dictionary, and add a new calculated column."""
data_dict = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "Salary": [50000, 60000, 70000]
}
df_dict = pd.DataFrame(data_dict)
df_dict["Bonus"] = df_dict["Salary"] * 0.1
print("\nDataFrame from dictionary with bonus column:")
print(df_dict)






