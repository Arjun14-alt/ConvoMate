from flask import Flask, render_template, request, jsonify
from chatbot.engine import get_response

app = Flask(__name__)

# in-memory history
history = []


@app.route("/")
def landing():
    return render_template("landing.html")


@app.route("/chatpage")
def chatpage():
    return render_template("chat.html")


@app.route("/api/chat", methods=["POST"])
def chat():

    global history

    try:
        data = request.get_json()

        if not data:
            return jsonify({"reply": "No input received."})

        user_message = str(data.get("message", "")).strip()

        if not user_message:
            return jsonify({"reply": "Empty message."})

        # store user msg
        history.append({
            "role": "user",
            "content": user_message
        })

        # keep history short
        history = history[-10:]

        # AI response
        reply = get_response(history)

        # store AI msg
        history.append({
            "role": "assistant",
            "content": reply
        })

        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"reply": f"Server error: {str(e)}"})


if __name__ == "__main__":
    app.run(debug=True)