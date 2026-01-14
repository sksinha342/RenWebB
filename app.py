from flask import Flask
from flask_cors import CORS
import os
from pages.login import login_bp
from pages.qrgen import qr_bp
from pages.pdfaddpass import pdf_bp

app = Flask(__name__)

# CORS allow karna zaroori hai taaki Vercel frontend access kar sake
CORS(app) 

# Blueprints register karna (aapki folder structure ke hisab se)
app.register_blueprint(login_bp, url_prefix='/auth')
app.register_blueprint(qr_bp, url_prefix='/qr')
app.register_blueprint(pdf_bp, url_prefix='/pdf')

@app.route('/')
def home():
    return {"status": "Backend is running!"}, 200

if __name__ == "__main__":
    # Render automatically PORT environment variable deta hai
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
