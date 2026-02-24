import requests
import pandas as pd
import dash
from dash import dcc, html, Input, Output
import plotly.express as px

API_BASE = "http://127.0.0.1:5000/api"

# ---------------------------
# Helper functions
# ---------------------------

def fetch_sales(product=None):
    params = {"product": product} if product else {}
    response = requests.get(f"{API_BASE}/sales", params=params)
    return pd.DataFrame(response.json())

def fetch_products():
    response = requests.get(f"{API_BASE}/sales")
    df = pd.DataFrame(response.json())
    return sorted(df["Product"].unique())

def fetch_kpis():
    return requests.get(f"{API_BASE}/kpis").json()

# ---------------------------
# App setup
# ---------------------------

app = dash.Dash(__name__)
app.title = "Experimental Sales Dashboard"

kpis = fetch_kpis()
products = fetch_products()

# ---------------------------
# Layout
# ---------------------------

app.layout = html.Div(
    style={"padding": "20px", "fontFamily": "Arial"},
    children=[

        html.H1("Experimental 2024 Sales Dashboard", style={"textAlign": "center"}),

        html.H2(f"Total Sales: ₦{kpis['total_sales']:,.2f}", style={"textAlign": "center"}),

        html.Label("Select Product"),
        dcc.Dropdown(
            id="product-filter",
            options=[{"label": p, "value": p} for p in products],
            placeholder="All Products",
            clearable=True
        ),

        html.Br(),

        dcc.Graph(id="sales-boxplot"),
        dcc.Graph(id="sales-by-product"),
        dcc.Graph(id="sales-units-pairplot"),
    ]
)

# ---------------------------
# Callback
# ---------------------------

@app.callback(
    Output("sales-boxplot", "figure"),
    Output("sales-by-product", "figure"),
    Output("sales-units-pairplot", "figure"),
    Input("product-filter", "value")
)
def update_charts(selected_product):

    df = fetch_sales(selected_product)

    if df.empty:
        return {}, {}, {}

    # Box Plot
    box_fig = px.box(
        df,
        x="Product",
        y="Sales",
        title="Sales Distribution by Product",
        color="Product"
    )

    # Bar Chart (AGGREGATED)
    bar_df = (
        df.groupby("Product", as_index=False)["Sales"]
        .sum()
        .sort_values("Sales", ascending=False)
    )

    bar_fig = px.bar(
        bar_df,
        x="Sales",
        y="Product",
        orientation="h",
        title="Total Sales by Product"
    )

    # Pair Plot
    pairplot_fig = px.scatter_matrix(
        df,
        dimensions=["Sales", "Units"],
        color="Product",
        title="Sales vs Units by Product"
    )

    return box_fig, bar_fig, pairplot_fig

# ---------------------------
# Run app
# ---------------------------

if __name__ == "__main__":
    app.run(debug=True)

#KEY LESSON (VERY IMPORTANT)
# Dash callbacks must always receive clean, structured data (DataFrames) as seen above, not raw API JSON.

# run python dashboard.py to start the server
# use this http://127.0.0.1:8050/ in browser to view the interactive visualization 
# while the api.py is running in the other terminal concurrently