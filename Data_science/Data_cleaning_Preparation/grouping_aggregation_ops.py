"""1. Group data by a categorical column"""
import pandas as pd
# data = {
#     "Class": ["A", "B", "A", "B", "c", "C"],
#     "Score": [85, 90, 88, 72, 95, 88],
#     "Age": [15, 16, 15, 17, 16, 15],
# }
# df = pd.DataFrame(data)
# print("Original DataFrame: \n", df)

# grouped = df.groupby('Class').mean()
# print("\nGrouped DataFrame (mean): \n", grouped)



# """2. Calculate Summary aggregate statistics for each group data"""
# grouped_stats = df.groupby('Class').agg({
#     'Score': ['mean', 'max', 'min', 'std', 'count'],
#     'Age': ['mean', 'max', 'min', 'std', 'count']
# })
# print("\nAggregate Statistics for each group: \n", grouped_stats)






# #More Examples of Grouping and Aggregation Operations in Pandas
"""1. Create a dataset of sales data and group it by region and product category"""
sales_data = {
    "Region": ["North", "South", "East", "West", "North", "South", "East", "West"],
    "Product": ["A", "A", "B", "B", "A", "B", "A", "B"],
    "Sales": [100, 150, 200, 250, 120, 180, 130, 220],
    "Profit": [20, 30, 40, 50, 25, 35, 28, 45],
}
sales_df = pd.DataFrame(sales_data)
print("\nSales DataFrame: \n", sales_df)

# grouped_sales = sales_df.groupby(['Region', 'Product']).sum()
# print("\nGrouped Sales by Region and Product: \n", grouped_sales)

# """2. Use pivot_table to calculate the total and average sales for each region, product category, and per year"""
# pivot_sales = sales_df.pivot_table(
#     values='Sales',
#     index=['Region', 'Product'],
#     aggfunc=['sum', 'mean']
# )
# print("\nPivot Table of Sales: \n", pivot_sales)

"""3. Create a custom aggregation function to calculate the variance for each group"""
def variance_func(x):
    return x.var()
grouped_variance = sales_df.groupby('Region')['Sales'].agg(variance_func)
print("\nVariance of Sales by Region: \n", grouped_variance)




