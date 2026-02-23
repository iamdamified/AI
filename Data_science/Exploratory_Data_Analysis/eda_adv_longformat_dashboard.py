
# Additional Practice:
# NEW TASK
""" 1. Use another dataset of your choice and apply the same EDA steps(tast 1-4) to uncover insights.
2. Explore advanced Visualizations like box plots and pair plots in seaborn.
3. Create a dashboard for your findings using Plotly and Dash."""

# For the additional practice, you can choose WESTGATE SALES SUMMARY REPPORT FOR THE YEAR 2024.xlsx from Westgate Data Analysis.


# NEW TASK 1
"""Perform Data Cleaning, Aggregation, and Filtering for this task an excel file dataset is provided"""
import pandas as pd
# Load the Westgate dataset
excel = "Experimental SALES SUMMARY REPPORT FOR THE YEAR 2024.xlsx"
df_sales = pd.read_excel(excel, header=4)  # Adjust header so that it reads from row 4, which contains the column names
df_sales = df_sales.dropna(axis=1, how="all") # remove empty columns "NaN" values
df_sales = df_sales.dropna(how="all") # remove empty rows "NaN" values


# # Inspect raw dataset
print(df_sales.head())
print(df_sales.columns)
print(df_sales.info())
print(df_sales.describe())

# The best usable data starts from row 4, so we set header=3 to read the column names correctly. We also drop any completely empty columns and rows to clean the dataset before analysis.
# Therefore, for best visualization  we must rename the columns to more user-friendly/understandable names by creating a mapping of the original column names to new names and then applying it to the DataFrame.

# Define a mapping of original column names to new, more descriptive names, however, i discovered this rename works when all column names are unique only.
# column_mapping = {
#     "Unnamed: 0": "Branch",
#     "UNIT": "Laptops_Units",
#     "SALES": "Laptops_Sales",
#     "UNIT": "Branded Sys._Units",
#     "SALES": "Branded Sys._Sales",
#     "UNIT": "Printers_Units",
#     "SALES": "Printers_Sales",
#     "UNIT": "Mobile Phones_Units",
#     "SALES": "Mobile Phones_Sales",
#     "UNIT": "Inks_Units",
#     "SALES": "Inks_Sales",
#     "UNIT": "Toners_Units",
#     "SALES": "Toners_Sales",
#     "UNIT": "Canon_Units",
#     "SALES": "Canon_Sales"
    
# }

# # Rename columns using the mapping
# df_sales = df_sales.rename(columns=column_mapping)


# Solution was to copy the excel dataset frame into a new dataframe and then rename columns by index.

# Create a copy of the dataframe with new column names
df = df_sales.copy()

df.columns = [
    "Branch",
    "Laptops_Unit", "Laptops_Sales",
    "Branded_Unit", "Branded_Sales",
    "Printers_Unit", "Printers_Sales",
    "Mobile_Unit", "Mobile_Sales",
    "Inks_Unit", "Inks_Sales",
    "Toners_Unit", "Toners_Sales",
    "Canon_Unit", "Canon_Sales",
]

# Inspect wide-dataset after conversion for analysis and ML by renaming
print(df.head())
print(df.columns)
print(df.info())
print(df.describe())


#Clean or fix wide dataset before converting to long-format for better analysis and ML:
# Remove bad rows
df = df[df["Branch"].notna()]

# Convert numerics
for col in df.columns[1:]:
    df[col] = pd.to_numeric(df[col], errors="coerce")


#Alternatively, you can convert to long-format by separating product column from unit and "sales" columns.
#Long FORMAT BLOCK:
records = []

products = [
    ("Laptops", "Laptops_Unit", "Laptops_Sales"),
    ("Branded Systems", "Branded_Unit", "Branded_Sales"),
    ("Printers", "Printers_Unit", "Printers_Sales"),
    ("Mobile Phones", "Mobile_Unit", "Mobile_Sales"),
    ("Inks", "Inks_Unit", "Inks_Sales"),
    ("Toners", "Toners_Unit", "Toners_Sales"),
    ("Canon", "Canon_Unit", "Canon_Sales"),
]

for _, row in df.iterrows():
    for product, unit_col, sales_col in products:
        records.append({
            "Branch": row["Branch"],
            "Product": product,
            "Units": row[unit_col],
            "Sales": row[sales_col],
        })

df_long = pd.DataFrame(records)



# Clean Long Data:



# Convert numeric safely
df_long["Sales"] = pd.to_numeric(df_long["Sales"], errors="coerce")
df_long["Units"] = pd.to_numeric(df_long["Units"], errors="coerce")

# Remove TOTAL row
df_long = df_long[df_long["Branch"] != "TOTAL"]

df_long = df_long.dropna(subset=["Sales"])
df_long = df_long.dropna(subset=["Units"])



# Fill missing values
# df_long["Sales"] = df_long["Sales"].fillna(df_long["Sales"].median())
df_long["Sales"] = df_long["Sales"].fillna(0)
df_long["Units"] = df_long["Units"].fillna(0)

# Remove duplicates
df_long = df_long.drop_duplicates()


# Inspect long-dataset again after second conversion to long-format to make it best ready for analysis and ML.
print(df_long.head())
print(df_long.columns)
print(df_long.info())
print(df_long.describe())


# Filter data and check: Sales greater than 1000
high_sales = df_long[df_long["Sales"] > 1000]
print(high_sales.head())








# # NEW TASK 2
# """Generate Visualizations to illustrate Key Insights from the dataset. 
# Use libraries such as Matplotlib or Seaborn to create visualizations to highlight trends and patterns in the data."""
import matplotlib.pyplot as plt
import seaborn as sns
# Visualization 1: Sales Distribution (Box Plot)
#This works for Long Format data Visualization:
sns.boxplot(x=df_long["Sales"], color="orange")
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.show()



# # Visualization 2: Sales by Product (Bar Chart)
# #This works for Long Format data Visualization:
sales_by_product = df_long.groupby("Product")["Sales"].sum()
sales_by_product.plot(kind="bar", color="green")
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()




# Visualization 3: Pair Plot of Sales, Quantity, and Discount
#This works for Long Format data Visualization:
sns.pairplot(df_long[["Sales", "Units"]], diag_kind="kde", plot_kws={"alpha": 0.5})
plt.suptitle("Pair Plot of Sales, Unit", y=1.02)
plt.show()


#Because seaborn plot does not work with Dash, then i had to use plotly express to ensure it displays in dashboard.
#Replace sns.pairplot with plotly.express.scatter_matrix
import plotly.express as px

pairplot_fig = px.scatter_matrix(
    df_long,
    dimensions=["Sales", "Units"],
    color="Product",
    title="Sales vs Units by Product Category"
)



# NEW TASK 3
"""Create a dashboard for your findings using Plotly and Dash"""

import dash
from dash import dcc, html, Input, Output
import plotly.express as px

# Initialize Dash app
app = dash.Dash(__name__)
app.title = "Westgate Sales Dashboard"

# KPI
total_sales = df_long["Sales"].sum()

# Layout
app.layout = html.Div(
    style={"padding": "20px", "fontFamily": "Arial"},
    children=[

        html.H1("Westgate 2024 Sales Dashboard", style={"textAlign": "center"}),

        # KPI Card
        html.Div(
            children=[
                html.H3("Total Sales"),
                html.H2(f"₦{total_sales:,.2f}")
            ],
            style={
                "textAlign": "center",
                "marginBottom": "30px",
                "backgroundColor": "#f2f2f2",
                "padding": "20px",
                "borderRadius": "10px"
            }
        ),

        # Product Dropdown
        html.Label("Select Product"),
        dcc.Dropdown(
            id="product-filter",
            options=[
                {"label": product, "value": product}
                for product in sorted(df_long["Product"].unique())
            ],
            value=None,
            placeholder="All Products",
            clearable=True
        ),

        html.Br(),

        # Charts
        dcc.Graph(id="sales-boxplot"),
        dcc.Graph(id="sales-by-product"),
        dcc.Graph(id="sales-units-pairplot", figure=pairplot_fig)
    ]
)

# Callbacks
@app.callback(
    Output("sales-boxplot", "figure"),
    Output("sales-by-product", "figure"),
    Output("sales-units-pairplot", "figure"),
    Input("product-filter", "value")
)
def update_charts(selected_product):

    if selected_product:
        filtered_df = df_long[df_long["Product"] == selected_product]
    else:
        filtered_df = df_long

    # Box plot
    box_fig = px.box(
        filtered_df,
        x="Product",
        y="Sales",
        title="Sales Distribution by Product",
        color="Product"
    )

    # Bar chart
    bar_data = (
        filtered_df
        .groupby("Product", as_index=False)["Sales"]
        .sum()
        .sort_values("Sales", ascending=False)
    )

    bar_fig = px.bar(
        bar_data,
        x="Sales",
        y="Product",
        orientation="h",
        title="Total Sales by Product"
    )

    # ---- Pair Plot (Scatter Matrix) ----
    pairplot_fig = px.scatter_matrix(
        filtered_df,
        dimensions=["Sales", "Units"],
        color="Product",
        title="Sales vs Units by Product Category"
    )

    return box_fig, bar_fig, pairplot_fig


# Run server
if __name__ == "__main__":
    app.run(debug=True)

#Ensure you are in the right directory the excel file is located, then run it: cd Data_Science/Exploratory_Data_Analysis
# run the code in terminal using: python eda_advtask_dashboard.py
#goto http://127.0.0.1:8050/ to view the dashboard in your web browser. 
# You can interact with the dropdown to filter the data by category and see how the charts update accordingly.







# NEW TASK 4
"""Identify and Interpret Patterns and Anomalies using human understanding and interpretation of the graphics and statistical data produced in task1, and particularly in task 2."""
# Interpretation of Visualization 1: Sales Distribution (Box Plot)
# The box plot shows the distribution of sales values. The median line is near the center of the box, indicating a relatively symmetric distribution. 
# There are a few outliers on the higher end, suggesting some sales values are significantly higher than the rest, which may indicate high-value transactions or anomalies in data entry.
# Interpretation of Visualization 2: Sales by Product Category (Bar Chart)
# The bar chart reveals that the "Electronics" category has the highest total sales, followed by "Furniture" and "Office Supplies". This indicates that electronics are the most popular category among customers, contributing significantly to overall sales. The lower sales in "Office Supplies" suggest it may be a less popular category or have lower-priced items.
# Interpretation of Visualization 3: Pair Plot of Sales, Unit

# NEW TASK 5
"""Summarize Findings in a Report"""