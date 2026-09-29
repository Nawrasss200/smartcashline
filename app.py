from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


# =========================================================
# HOME / LANDING PAGE
# =========================================================

@app.route("/")
def home():
    return render_template("index.html")


# =========================================================
# LOGIN
# =========================================================

@app.route("/login")
def login():
    return render_template("login.html")


# =========================================================
# MAIN SYSTEM
# =========================================================

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


# =========================================================
# INFORMATION PAGES
# =========================================================

@app.route("/about")
def about():
    return render_template("about.html")


# =========================================================
# CONTACT API
# =========================================================

@app.route("/contact", methods=["POST"])
def contact():

    # دعم JSON
    data = request.get_json(silent=True)

    # إذا لم يصل JSON، حاول قراءة بيانات الفورم العادية
    if not data:
        data = request.form

    name = data.get("name", "").strip()
    email = data.get("email", "").strip()
    message = data.get("message", "").strip()

    # التحقق من الحقول
    if not name or not email or not message:
        return jsonify({
            "success": False,
            "message": "يرجى تعبئة جميع الحقول."
        }), 400

    # حاليًا يتم استقبال الرسالة فقط
    # ويمكن لاحقًا ربطها بقاعدة بيانات أو بريد إلكتروني

    return jsonify({
        "success": True,
        "message": "تم استلام رسالتك بنجاح."
    })


# =========================================================
# HEALTH CHECK
# =========================================================

@app.route("/health")
def health():
    return "Smart CashLine is running."


# =========================================================
# ERROR HANDLERS
# =========================================================

@app.errorhandler(404)
def page_not_found(error):
    return jsonify({
        "success": False,
        "message": "الصفحة غير موجودة."
    }), 404


@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({
        "success": False,
        "message": "حدث خطأ داخلي في الخادم."
    }), 500


# =========================================================
# RUN
# =========================================================

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )

🔥 الآن ترتيب المشروع لازم يكون تقريبًا:

smartcashline/
│
├── app.py
├── requirements.txt
│
├── templates/
│   ├── index.html       ← الصفحة الرئيسية
│   ├── login.html       ← تسجيل الدخول
│   ├── dashboard.html
│   ├── accounts.html
│   ├── transfers.html
│   ├── transactions.html
│   ├── customers.html
│   ├── notifications.html
│   ├── settings.html
│   └── about.html
│
└── static/
    ├── style.css
    └── script.js

بعد رفع "app.py" و"index.html" إلى GitHub:

1. اعمل Commit.
2. انتظر Deployment جديد في Railway.
3. افتح رابط الموقع.
4. اعمل تحديث للصفحة.

النتيجة: "/" = الصفحة الرئيسية القديمة، و"/login" = تسجيل الدخول. 🚀