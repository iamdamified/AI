# Grouping data by Category and calculating aggregate statistics
import pandas as pd

# groupby operations
# iterate over groups
grouped = df.groupby('Category')
for name, group in grouped:
    print(f"Group: {name}")
    print(group)


# calculate aggregate statistics

#Aggregation functions using groupy:
#grouped.mean()  # Calculate the mean of each group
#grouped.sum()   # Calculate the sum of each group
df.groupby('Category_column')["numeric_column"].mean() # Calculate sum, mean, and count for the 'Value' column in each group/
df.groupby('Category_column').agg({"numeric_column": ['mean', 'max', 'min','count']})

grouped_stats = grouped.agg({
    'Value': ['sum', 'mean', 'count']
})
print("\nAggregate Statistics for each group:")
print(grouped_stats)


#Aggregation functions using pivot_table:
pivot = df.pivot_table(
    values='numeric_column', 
    index='Category_column', 
    aggfunc=['mean', 'max', 'min','count']
    )


#Aggregation functions using custom functions:
def range_func(x):
    return x.max() - x.min()

df.groupby('Category_column')["numeric_column"].agg(range_func) # Apply a custom function to calculate the range of values in each group


#Calculating Summary Statistics for Grouped Data
#common statistics include mean, max, min, median, standard deviation, and count. You can use the agg() function to calculate these statistics for each group.

#Multiple aggregations for multiple columns:
grouped_summary = grouped.agg({
    'Value': ['mean', 'max', 'min', 'std', 'count']
})
print(grouped_summary)

#or, for a single column:
df.groupby('Category_column').agg({
    'numeric_column': ['mean', 'max', 'min', 'std', 'count']
})


#or, individual or specific statistics for a single column:
df.groupby('Category_column')["numeric_column"].describe() # Generate descriptive statistics for each group, including count, mean, std, min, 25th percentile, 50th percentile (median), 75th percentile, and max.
df.groupby('Category_column')["numeric_column"].mean()
df.groupby('Category_column')["numeric_column"].max()
df.groupby('Category_column')["numeric_column"].min()

