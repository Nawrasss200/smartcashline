from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


# =========================================================
# HOME
# =========================================================

@app.route("/")
def home():
    # =====================================================
    # TEST MODE
    # إذا ظهرت هذه الصفحة على Railway فهذا يعني أن Railway
    # يشغّل هذا الملف فعلًا.
    # =====================================================

    return """
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <title>Smart CashLine - Test</title>

        <style>
            * {
                box-sizing: border-box;
            }

            body {
                margin: 0;
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;

                background:
                    radial-gradient(
                        circle at top right,
                        #16345c 0%,
                        #08111f 45%,
                        #030812 100%
                    );

                color: white;
                font-family: Arial, sans-serif;
            }

            .box {
                width: min(90%, 650px);
                padding: 50px 35px;
                text-align: center;

                background: rgba(255,255,255,0.06);
                border: 1px solid rgba(255,255,255,0.12);
                border-radius: 25px;

                box-shadow:
                    0 25px 80px rgba(0,0,0,0.45),
                    inset 0 1px 0 rgba(255,255,255,0.08);

                backdrop-filter: blur(15px);
            }

            .logo {
                width: 80px;
                height: 80px;
                margin: 0 auto 25px;

                display: flex;
                align-items: center;
                justify-content: center;

                border-radius: 22px;

                background: linear-gradient(
                    135deg,
                    #d9b86c,
                    #9b7732
                );

                color: #07101d;
                font-size: 38px;
                font-weight: 900;

                box-shadow: 0 15px 40px rgba(217,184,108,0.25);
            }

            h1 {
                margin: 0 0 15px;
                font-size: 32px;
            }

            p {
                color: #b8c4d6;
                line-height: 1.8;
                margin: 8px 0;
            }

            .success {
                display: inline-block;
                margin-top: 25px;
                padding: 12px 22px;

                border-radius: 999px;

                background: rgba(46, 204, 113, 0.12);
                border: 1px solid rgba(46, 204, 113, 0.3);

                color: #6ee7a0;
                font-weight: bold;
            }

            .date {
                margin-top: 20px;
                font-size: 13px;
                color: #718096;
            }
        </style>
    </head>

    <body>

        <div class="box">

            <div class="logo">
                S
            </div>

            <h1>
                Smart CashLine
            </h1>

            <p>
                🚀 تم تشغيل النسخة الجديدة من app.py
            </p>

            <p>
                إذا كنت ترى هذه الصفحة، فإن Railway
                يشغّل الكود الجديد بنجاح.
            </p>

            <div class="success">
                ✓ RAILWAY CONNECTION OK
            </div>

            <div class="date">
                29 September 2026
            </div>

        </div>

    </body>
    </html>
    """


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
# CONTACT
# =========================================================

@app.route("/contact", methods=["POST"])
def contact():

    data = request.get_json(silent=True)

    if not data:
        data = request.form

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
# HEALTH CHECK
# =========================================================

@app.route("/health")
def health():
    return "Smart CashLine is running."


# =========================================================
# 404
# =========================================================

@app.errorhandler(404)
def page_not_found(error):
    return jsonify({
        "success": False,
        "message": "الصفحة غير موجودة."
    }), 404


# =========================================================
# 500
# =========================================================

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

الآن مهم جدًا ⚠️

ارفع هذا الملف نفسه إلى:

app.py

على GitHub واعمل Commit changes.

ثم Railway لازم يعمل Deployment جديد.

بعدها افتح الموقع.

إذا ظهرت لك:

«🚀 تم تشغيل النسخة الجديدة من app.py
✓ RAILWAY CONNECTION OK»

فمعناها عرفنا أن الاتصال صحيح، وبعدها أعطيك النسخة النهائية التي ترجع "index.html".

إذا بقي التصميم القديم حتى مع هذا الملف، لا تغيّر أي شيء ثاني؛ وقتها المشكلة في إعدادات Railway/المستودع وليست في Flask.