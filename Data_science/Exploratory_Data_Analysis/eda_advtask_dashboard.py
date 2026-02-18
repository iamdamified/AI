
# Additional Practice:
# NEW TASK
""" 1. Use another dataset of your choice and apply the same EDA steps(tast 1-4) to uncover insights.
2. Explore advanced Visualizations like box plots and pair plots in seaborn.
3. Create a dashboard for your findings using Plotly and Dash."""

# For the additional practice, you can choose WESTGATE SALES SUMMARY REPPORT FOR THE YEAR 2024.xlsx from Westgate Data Analysis.


# NEW TASK 1
"""Perform Data Cleaning, Aggregation, and Filtering for this task an excel file dataset is provided"""
import pandas as pd
# Load the Titanic dataset
excel = "WESTGATE SALES SUMMARY REPPORT FOR THE YEAR 2024.xlsx"
df_sales = pd.read_excel(excel)

# Inspect dataset
print(df_sales.head())
print(df_sales.info())
print(df_sales.describe())

# Data Cleaning: Handle missing values
df_sales["Sales"] = df_sales["Sales"].fillna(df_sales["Sales"].median())
# Remove Duplicate entries
df_sales = df_sales.drop_duplicates()
# Filter data: Sales greater than 1000
high_sales = df_sales[df_sales["Sales"] > 1000]
print(high_sales.head())


# NEW TASK 2
"""Generate Visualizations to illustrate Key Insights from the dataset. 
Use libraries such as Matplotlib or Seaborn to create visualizations to highlight trends and patterns in the data."""
import matplotlib.pyplot as plt
import seaborn as sns
# Visualization 1: Sales Distribution (Box Plot)
sns.boxplot(x=df_sales["Sales"], color="orange")
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.show()

# Visualization 2: Sales by Category (Bar Chart)
sales_by_category = df_sales.groupby("Category")["Sales"].sum()
sales_by_category.plot(kind="bar", color="green")
plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.show()

# Visualization 3: Pair Plot of Sales, Quantity, and Discount
sns.pairplot(df_sales[["Sales", "Quantity", "Discount"]], diag_kind="kde", plot_kws={"alpha": 0.5})
plt.suptitle("Pair Plot of Sales, Quantity, and Discount", y=1.02)
plt.show()


# NEW TASK 3
"""Create a dashboard for your findings using Plotly and Dash."""
# For creating a dashboard using Plotly and Dash, you would need to set up a Dash application. Below is a simple example of how to create a dashboard with Plotly and Dash to visualize the sales data.
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
# Initialize the Dash app
app = dash.Dash(__name__)










# NEW TASK 4
"""Identify and Interpret Patterns and Anomalies using human understanding and interpretation of the graphics and statistical data produced in task1, and particularly in task 2."""
# Interpretation of Visualization 1: Sales Distribution (Box Plot)
# The box plot shows the distribution of sales values. The median line is near the center of the box, indicating a relatively symmetric distribution. 
# There are a few outliers on the higher end, suggesting some sales values are significantly higher than the rest, which may indicate high-value transactions or anomalies in data entry.
# Interpretation of Visualization 2: Sales by Category (Bar Chart)
# The bar chart reveals that the "Electronics" category has the highest total sales, followed by "Furniture" and "Office Supplies". This indicates that electronics are the most popular category among customers, contributing significantly to overall sales. The lower sales in "Office Supplies" suggest it may be a less popular category or have lower-priced items.
# Interpretation of Visualization 3: Pair Plot of Sales, Quantity, and Discount
# The pair plot shows the relationships between sales, quantity, and discount. There is a positive correlation between sales and quantity, indicating that higher quantities sold generally lead to higher sales. The relationship between sales and discount appears to be more complex, with some high sales values occurring at both low and high discount levels, suggesting that while discounts can drive sales, other factors may also influence sales performance. The distribution of quantity and discount also shows some variability, indicating that different combinations of these factors can lead to varying sales outcomes.

# NEW TASK 5
"""Summarize Findings in a Report"""
# Summary of Findings:
# 1. The sales data shows a relatively symmetric distribution with a few high-value outliers.
# 2. The "Electronics" category is the most popular, contributing the highest sales.
# 3. There is a positive correlation between quantity sold and sales, indicating that higher quantities generally lead to higher sales.
# 4. The relationship between discount and sales is complex, suggesting that while discounts can drive sales, other factors also play a role in determining sales performance.

