from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


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

    # سيتم ربط الرسائل بالبريد الإلكتروني/قاعدة البيانات لاحقًا
    return jsonify({
        "success": True,
        "message": "تم استلام رسالتك بنجاح."
    })


@app.route("/health")
def health():
    return "Smart CashLine is running."


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)