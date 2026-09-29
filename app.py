@app.route("/")
def home():
    return """
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <title>Smart CashLine TEST</title>
    </head>
    <body style="background:#08111f;color:white;text-align:center;padding:100px;font-family:Arial;">
        <h1>🚀 SMART CASHLINE TEST</h1>
        <h2>إذا ظهرت هذه الصفحة، Railway يشغل النسخة الجديدة من app.py</h2>
        <p>2026-09-29</p>
    </body>
    </html>
    """