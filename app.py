from flask import Flask, render_template, request, jsonify
from chatbot.engine import get_response

app = Flask(__name__)

history = []


@app.route("/")
def landing():
    return render_template("landing.html")


@app.route("/chat")
def chat_page():
    return render_template("chat.html")


@app.route("/api/chat", methods=["POST"])
def chat():

    global history

    msg = request.json["message"]

    history.append({"role": "user", "content": msg})
    history = history[-12:]

    reply = get_response(history)

    history.append({"role": "assistant", "content": reply})

    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)