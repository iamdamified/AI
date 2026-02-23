
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


# Inspect raw dataset
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

#Alternatively, you can convert to long-format by separating product column from unit and "sales" columns, but for the sake of this task, we will keep it in wide-format and handle it accordingly in the visualizations and analysis.
# Inspect dataset again after cleaning and renaming
print(df.head())
print(df.columns)
print(df.info())
print(df.describe())


# Data Cleaning:

#To drop header rows which may still be existing as headers in the data:
df = df[df["Branch"].notna()]

# Convert numeric columns safely to numeric types, coercing errors to NaN (which can be handled later)
for col in df.columns[1:]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# #Handle missing values: 
#This is used to combine all sales columns into one column(sales_columns) for better handling in the absence of long-format data.
sales_columns = [col for col in df.columns if col.endswith("_Sales")]

for col in sales_columns:
    df[col] = df[col].fillna(df[col].median())

# Remove Duplicate entries
df = df.drop_duplicates()


# Filter data: Sales greater than 1000
for col in sales_columns:
    high_sales = df[df[col] > 1000]
    print(f"Sales greater than 1000 in {col}:\n{high_sales[['Branch', col]]}\n")






# NEW TASK 2
"""Generate Visualizations to illustrate Key Insights from the dataset. 
Use libraries such as Matplotlib or Seaborn to create visualizations to highlight trends and patterns in the data."""
import matplotlib.pyplot as plt
import seaborn as sns


# Visualization 1: Sales Distribution (Box Plot)
# Regular box plot for wide-format data: It involves creating a long-format version of the sales data for better visualization, as box plots are more effective when comparing distributions across categories(products).
df_long = df.melt(id_vars="Branch", value_vars=sales_columns, var_name="Product", value_name="Sales")# Reuse this for other long format visualizations
sns.boxplot(x="Product", y="Sales", data=df_long, color="orange")
plt.xticks(rotation=45)
plt.title("Sales Distribution by Product")
plt.show()


# Visualization 2: Sales by Product (Bar Chart)
# Regular bar chart for wide-format data:
sales_by_product = df_long.groupby("Product", as_index=False)["Sales"].sum()
# sales_by_product = (df_long.groupby("Product")["Sales"].sum().reset_index())
sns.barplot(data=sales_by_product, x="Sales", y="Product", orient="h", color="green")
plt.title("Total Sales by Product")
plt.xlabel("Total Sales")
plt.ylabel("Product Category")
plt.show()


# Visualization 3: Pair Plot of Sales, Units
# Regular Pair Plot for wide-format data:
# You will recall that so far we have sales_columns variable for all product sales, no units_columns, hence we create it.
units_columns = [col for col in df.columns if col.endswith("_Unit")]
df_units = df.melt(id_vars="Branch", value_vars=units_columns, var_name="Product", value_name="Units")# newly created combined units_cloumn
df_units["Product"] = df_units["Product"].str.replace("_Unit", "", regex=False)# Normalize units
df_long = df.melt(id_vars="Branch", value_vars=sales_columns, var_name="Product", value_name="Sales")# recalled comnined sales_column above
df_long["Product"] = df_long["Product"].str.replace("_Sales", "", regex=False)# Normalize sales
df_units_sales_long = pd.merge(df_units, df_long, on=["Branch", "Product"], how="inner") # Merge units and sales long-format data on Branch and Product for pairplot
#display to view results of the merge and the new long-format dataframe for units and sales
print(df_units_sales_long.head())
print(df_units_sales_long.columns)
print(df_units_sales_long.shape)

# Now we can create a pair plot to visualize the relationship between Sales and Units, colored by Product category.
sns.pairplot(df_units_sales_long, vars=["Sales", "Units"], hue="Product", diag_kind="kde", plot_kws={"alpha": 0.6})
plt.suptitle("Sales vs Units by Product Category", y=1.02)
plt.show()



#Because seaborn plot does not work with Dash, then i had to use plotly express to ensure it displays in dashboard.
#Replace sns.pairplot with plotly.express.scatter_matrix
import plotly.express as px

pairplot_fig = px.scatter_matrix(
    df_units_sales_long,
    dimensions=["Sales", "Units"],
    color="Product",
    title="Sales vs Units by Product Category"
)


# NEW TASK 3
"""Create a dashboard for your findings using Plotly, Dash."""
# pip install dash plotly openpyxl

# For creating a dashboard using Plotly and Dash, you would need to set up a Dash application. Below is a simple example of how to create a dashboard with Plotly and Dash to visualize the sales data.
import dash
# import dash_core_components as dcc
# import dash_html_components as htmlimport dash
from dash import dcc, html, Input, Output
import plotly.express as px

# Initialize Dash app
app = dash.Dash(__name__)
app.title = "Experimental Sales Dashboard"

# KPI calculation
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

        # Dropdown filter
        html.Label("Select Product Category"),
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
    # dcc.Graph(id="sales-units-pairplot"),
    Input("product-filter", "value")
)
def update_charts(selected_product):

    # ---- Filter SALES dataframe ----
    if selected_product:
        filtered_sales_df = df_long[df_long["Product"] == selected_product]
        filtered_units_df = df_units_sales_long[
            df_units_sales_long["Product"] == selected_product
        ]
    else:
        filtered_sales_df = df_long
        filtered_units_df = df_units_sales_long

    # Box plot
    box_fig = px.box(
        filtered_sales_df,
        x="Product",
        y="Sales",
        title="Sales Distribution by Product",
        color="Product"
    )

    # Bar chart
    bar_data = (
        filtered_sales_df
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

    # Pair Plot (Scatter Matrix)
    pairplot_fig = px.scatter_matrix(
        filtered_units_df,
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

