# It is a powerful library for Data Manipulation and Analysis(Series and Data Frame)

import pandas as pd
s = pd.Series([10,20,30], index=["a","b","c"])#user-defined-indexing or id/key stores data in regular tuple form(list and index-label)
print(s)

data = {"Name": ["Alice","Bob"], "Age": [25,30]} #auto-indexing stores data in dictionary form(key and list-value) in a column arrangement
df = pd.DataFrame(data)
print(df)

# Loading Data from CSV, EXcel, Dictionary, and other sources
df = pd.read_csv("data.csv")
df = pd.read_excel("data.xlsx")
df = pd.DataFrame(data)

# Saving data: you must first load the file with the above, then
df.to_csv("data.csv")
df.to_excel("data.xlsx")
df.to_csv("data.csv", index=False)# to remove auto-index label(0,1...)
df.to_csv("data.csv", index=1)# to load a specific index or row in a file

# Viewing Data:
print(df.head())#first 5 rows of data
print(df.tail())#last 5 rows of data
print(df.tail(4))#last 4 rows of data
print(df.info())#view summary info of a Dataframe
print(df.describe())#to see detail statistical information
print(df[["Name", "Age"]])#to see specific columns
print(df[df["Age"] > 25])#fitting a dataset(rows) from a larger dataset
print(df.iloc[0])#first row by position
print(df.iloc[:, 0])#first column by position
print(df.loc[0])#by label first row data
print(df.loc[:, "Name"])#by column name, column data