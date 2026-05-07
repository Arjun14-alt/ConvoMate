import os
from groq import Groq

# 🔑 MUST BE SET IN RENDER ENV VARIABLES
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def get_response(user_input):

    try:
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "system",
                    "content": "You are ConvoMate, a smart, friendly, conversational AI assistant built by Arjun Mondal."
                },
                {
                    "role": "user",
                    "content": user_input
                }
            ]
        )

        return completion.choices[0].message.content

    except Exception as e:
        return f"AI error: {str(e)}"