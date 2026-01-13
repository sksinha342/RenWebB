from flask import Blueprint, request, jsonify
import cloudinary.uploader
import psycopg2, os

login_bp = Blueprint("login", __name__)

conn = psycopg2.connect(
    host=os.getenv("PG_HOST"),
    database=os.getenv("PG_DB"),
    user=os.getenv("PG_USER"),
    password=os.getenv("PG_PASS"),
    port=os.getenv("PG_PORT"),
    sslmode="require"
)

@login_bp.route("/api/login", methods=["POST"])
def login():
    username = request.form.get("username")
    file = request.files.get("profile")

    upload = cloudinary.uploader.upload(file, folder="profiles")
    url = upload["secure_url"]

    cur = conn.cursor()
    cur.execute(
        "INSERT INTO users(username,image) VALUES(%s,%s)",
        (username, url)
    )
    conn.commit()

    return jsonify({"username": username, "image": url})