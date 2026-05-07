from groq import Groq
import os

# ✅ SAFE VERSION (no hardcoded key)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def get_response(user_input):
    try:
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "You are a helpful chatbot."},
                {"role": "user", "content": user_input}
            ]
        )
        return completion.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"