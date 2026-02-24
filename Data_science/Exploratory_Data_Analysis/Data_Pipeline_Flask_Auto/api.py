from flask import Flask, jsonify, request
from data import load_data

app = Flask(__name__)
df_long = load_data()

@app.route("/api/sales", methods=["GET"])
def get_sales():
    product = request.args.get("product")

    if product:
        data = df_long[df_long["Product"] == product]
    else:
        data = df_long

    return jsonify(data.to_dict(orient="records"))

@app.route("/api/kpis", methods=["GET"])
def kpis():
    return jsonify({
        "total_sales": float(df_long["Sales"].sum()),
        "total_units": int(df_long["Units"].sum())
    })

@app.route("/api/sales-by-product", methods=["GET"])
def sales_by_product():
    grouped = (
        df_long.groupby("Product")["Sales"]
        .sum()
        .reset_index()
        .sort_values("Sales", ascending=False)
    )
    return jsonify(grouped.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(port=5000, debug=True)


# run python api.py to start the server
# use this http://127.0.0.1:5000/ in browser with flask api endpoints in this file to view data