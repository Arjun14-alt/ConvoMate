from flask import Flask, render_template, request, jsonify
from chatbot.engine import get_response

app = Flask(__name__)

history = []


@app.route("/")
def home():
    return render_template("chat.html")


@app.route("/chat", methods=["POST"])
def chat():

    global history

    user_msg = request.json.get("message", "")

    # FORCE STRING SAFETY
    user_msg = str(user_msg)

    history.append({"role": "user", "content": user_msg})

    reply = get_response(history)

    history.append({"role": "assistant", "content": reply})

    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)