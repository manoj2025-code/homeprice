from flask import Flask, render_template, request

app = Flask(__name__)

# Approx price per sq.ft (₹) – sample data
AREA_PRICE_MAP = {
    "Whitefield": 7500,
    "Electronic City": 5500,
    "Marathahalli": 8000,
    "Indiranagar": 12000,
    "Jayanagar": 9500,
    "Yelahanka": 6000,
    "Hebbal": 8500,
    "Sarjapur Road": 7000,
    "BTM Layout": 7800,
    "Banashankari": 8200
}

@app.route("/", methods=["GET", "POST"])
def index():
    price = None

    if request.method == "POST":
        area = request.form["area"]
        sqft = float(request.form["sqft"])
        bhk = int(request.form["bhk"])
        bath = int(request.form["bath"])

        base_price = AREA_PRICE_MAP.get(area, 6000)

        # Simple pricing logic
        price = (
            sqft * base_price +
            (bhk * 300000) +
            (bath * 150000)
        )

        price = round(price / 100000, 2)  # in Lakhs

    return render_template(
        "index.html",
        areas=AREA_PRICE_MAP.keys(),
        price=price
    )

if __name__ == "__main__":
    app.run(debug=True)
