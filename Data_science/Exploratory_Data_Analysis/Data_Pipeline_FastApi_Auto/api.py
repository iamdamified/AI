#first install all data science tools with pip necessary for manipulation of data, then install fastapi and supports.
# # pip install fastapi uvicorn pydantic

from fastapi import FastAPI, Query
from typing import Optional
import pandas as pd
from data import load_data

app = FastAPI(title="Experimental Sales API")

df_long = load_data()

@app.get("/api/sales")
def get_sales(product: Optional[str] = Query(None)):
    data = df_long

    if product:
        data = data[data["Product"] == product]

    return data.to_dict(orient="records")

@app.get("/api/kpis")
def get_kpis():
    return {
        "total_sales": float(df_long["Sales"].sum()),
        "total_units": int(df_long["Units"].sum())
    }

@app.get("/api/sales-by-product")
def sales_by_product():
    grouped = (
        df_long.groupby("Product")["Sales"]
        .sum()
        .reset_index()
        .sort_values("Sales", ascending=False)
    )
    return grouped.to_dict(orient="records")


# run uvicorn api:app --reload to start the server
# use this http://127.0.0.1:8000 in browser with fast api endpoints in this file to view data
# use this to get Swagger UI documentation: http://127.0.0.1:8000/docs for testing and validation.