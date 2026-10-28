
from flask import Flask, jsonify, render_template

app = Flask(__name__)

PRODUCTS = [
    {"id": 1, "name": "Wireless Headphones", "price": 1499.00},
    {"id": 2, "name": "Smart Watch", "price": 2499.00},
    {"id": 3, "name": "Travel Backpack", "price": 999.00},
]


@app.get("/")
def home():
    return render_template("index.html", products=PRODUCTS)


@app.get("/health")
def health():
    return jsonify(status="healthy"), 200


@app.get("/api/products")
def products():
    return jsonify(PRODUCTS), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)

