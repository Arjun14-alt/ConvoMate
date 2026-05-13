from flask import Flask, render_template, request, jsonify
from chatbot.engine import get_response

import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

conversation_history = []


@app.route("/")
def landing():
    return render_template("landing.html")


@app.route("/chatpage")
def chatpage():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    global conversation_history

    user_message = request.json["message"]

    conversation_history.append({
        "role": "user",
        "content": user_message
    })

    # memory limit
    conversation_history = conversation_history[-12:]

    reply = get_response(conversation_history)

    conversation_history.append({
        "role": "assistant",
        "content": reply
    })

    return jsonify({
        "reply": reply
    })


@app.route("/upload", methods=["POST"])
def upload():

    file = request.files["file"]

    filepath = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    file.save(filepath)

    return jsonify({
        "message": f"{file.filename} uploaded successfully"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)