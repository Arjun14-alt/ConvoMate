from flask import Flask, render_template, request, jsonify
from chatbot.engine import get_response

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_message = request.json["message"]
        reply = get_response(user_message)
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"reply": f"Server error: {str(e)}"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)