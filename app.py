from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


# =========================================================
# SMARTCASHLINE
# Main Routes
# =========================================================

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/accounts")
def accounts():
    return render_template("accounts.html")


@app.route("/transfers")
def transfers():
    return render_template("transfers.html")


@app.route("/transactions")
def transactions():
    return render_template("transactions.html")


@app.route("/customers")
def customers():
    return render_template("customers.html")


@app.route("/notifications")
def notifications():
    return render_template("notifications.html")


@app.route("/settings")
def settings():
    return render_template("settings.html")


@app.route("/about")
def about():
    return render_template("about.html")


# =========================================================
# Contact API
# =========================================================

@app.route("/contact", methods=["POST"])
def contact():
    data = request.get_json(silent=True) or {}

    name = data.get("name", "").strip()
    email = data.get("email", "").strip()
    message = data.get("message", "").strip()

    if not name or not email or not message:
        return jsonify({
            "success": False,
            "message": "يرجى تعبئة جميع الحقول."
        }), 400

    return jsonify({
        "success": True,
        "message": "تم استلام رسالتك بنجاح."
    })


# =========================================================
# Health Check
# =========================================================

@app.route("/health")
def health():
    return "Smart CashLine is running."


# =========================================================
# Run
# =========================================================

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )