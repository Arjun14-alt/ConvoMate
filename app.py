from flask import Flask, render_template, request, jsonify
from chatbot.engine import get_response

app = Flask(__name__)

# -------------------------
# 🏠 Home route (UI page)
# -------------------------
@app.route("/")
def home():
    return render_template("index.html")


# -------------------------
# 💬 Chat API route
# -------------------------
@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_message = data.get("message", "")

        if not user_message:
            return jsonify({"reply": "Send a proper message 😄"})

        bot_reply = get_response(user_message)

        return jsonify({"reply": bot_reply})

    except Exception as e:
        return jsonify({"reply": f"Server error: {str(e)}"})


# -------------------------
# 🚀 Run app
# -------------------------
if __name__ == "__main__":
    app.run(debug=True)