import pandas as pd

def load_data():
    excel = "Experimental SALES SUMMARY REPPORT FOR THE YEAR 2024.xlsx"

    df_sales = pd.read_excel(excel, header=4)
    df_sales = df_sales.dropna(axis=1, how="all").dropna(how="all")

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

    df = df[df["Branch"].notna()]

    for col in df.columns[1:]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    products = [
        ("Laptops", "Laptops_Unit", "Laptops_Sales"),
        ("Branded Systems", "Branded_Unit", "Branded_Sales"),
        ("Printers", "Printers_Unit", "Printers_Sales"),
        ("Mobile Phones", "Mobile_Unit", "Mobile_Sales"),
        ("Inks", "Inks_Unit", "Inks_Sales"),
        ("Toners", "Toners_Unit", "Toners_Sales"),
        ("Canon", "Canon_Unit", "Canon_Sales"),
    ]

    records = []
    for _, row in df.iterrows():
        for product, u_col, s_col in products:
            records.append({
                "Branch": row["Branch"],
                "Product": product,
                "Units": row[u_col],
                "Sales": row[s_col],
            })

    df_long = pd.DataFrame(records)
    df_long = df_long[df_long["Branch"] != "TOTAL"]
    df_long = df_long.dropna(subset=["Sales", "Units"])
    df_long = df_long.drop_duplicates()

    return df_long