from flask import Flask
from flask_cors import CORS
from pages.login import login_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(login_bp)

@app.route("/")
def home():
    return "Backend Running"
@app.route("/api/ping")
def ping():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run()    
