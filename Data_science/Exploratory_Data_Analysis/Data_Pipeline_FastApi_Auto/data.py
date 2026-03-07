import pandas as pd

def load_data():
    excel = "Experimental SALES SUMMARY REPPORT FOR THE YEAR 2024.xlsx"

    df_sales = pd.read_excel(excel, header=4)#Load raw data to the frame
    df_sales = df_sales.dropna(axis=1, how="all").dropna(how="all")# removes empty columns and rows respectively.

    df = df_sales.copy()
    #rename columns
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

    df = df[df["Branch"].notna()]# Ensuring that all values in Brach column(rows) are non-null(has value)

    for col in df.columns[1:]:
        df[col] = pd.to_numeric(df[col], errors="coerce")#Turn all values in all columns that comes after Branch to numeric data type.
    
    #Create a products category table, mapping the corresponding units and sales together. useful as primary key and long format queries
    products = [
        ("Laptops", "Laptops_Unit", "Laptops_Sales"),
        ("Branded Systems", "Branded_Unit", "Branded_Sales"),
        ("Printers", "Printers_Unit", "Printers_Sales"),
        ("Mobile Phones", "Mobile_Unit", "Mobile_Sales"),
        ("Inks", "Inks_Unit", "Inks_Sales"),
        ("Toners", "Toners_Unit", "Toners_Sales"),
        ("Canon", "Canon_Unit", "Canon_Sales"),
    ]
    #create new empty list and iterate through rows with complete values in the products table moved to records list.
    # Rebuilding a new table with same branch, separated products from units and sales columns(Long Format)
    records = []
    for _, row in df.iterrows():
        for product, u_col, s_col in products:
            records.append({
                "Branch": row["Branch"],
                "Product": product,
                "Units": row[u_col],
                "Sales": row[s_col],
            })
    #Load Long format data(records) into DataFrame, clean data and output
    df_long = pd.DataFrame(records)
    df_long = df_long[df_long["Branch"] != "TOTAL"] #prevents summation for Branch column(non-numeric)
    df_long = df_long.dropna(subset=["Sales", "Units"])#remove products whose sales, units columns are empty
    df_long = df_long.drop_duplicates()#remove duplicate table entries.

    return df_long