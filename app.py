from flask import Flask, render_template, request, jsonify
from chatbot.engine import get_response
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

last_file_content = ""


@app.route("/")
def home():
    return render_template("chat.html")


@app.route("/chat", methods=["POST"])
def chat():

    global last_file_content

    user_message = request.json["message"]

    if last_file_content:
        user_message = f"""
User question: {user_message}

Context from uploaded file:
{last_file_content}
"""

    reply = get_response(user_message)

    return jsonify({"reply": reply})


@app.route("/upload", methods=["POST"])
def upload():

    global last_file_content

    file = request.files["file"]
    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)

    # read file (TXT only for now - safe + stable)
    try:
        with open(path, "r", encoding="utf-8") as f:
            last_file_content = f.read()
    except:
        last_file_content = "File uploaded but not readable (maybe binary like image/pdf)."

    return jsonify({"file": file.filename})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)