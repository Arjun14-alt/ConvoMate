import os
from groq import Groq

# 🔥 YOUR API KEY HERE
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

SYSTEM_PROMPT = """
You are ConvoMate, a modern AI assistant.

Rules:
- Speak naturally
- Avoid robotic formatting
- Be conversational and smart
- Answer like ChatGPT/Grok
- Be concise when needed
"""


def clean_content(content):

    if isinstance(content, str):
        return content

    if isinstance(content, list):
        return " ".join(str(x) for x in content)

    return str(content)


def get_response(history):

    try:

        messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ]

        for msg in history:

            role = msg.get("role", "user")
            content = clean_content(msg.get("content", ""))

            messages.append({
                "role": role,
                "content": content
            })

        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=messages,
            temperature=0.7
        )

        reply = completion.choices[0].message.content

        if not reply:
            return "I couldn't generate a response."

        return reply

    except Exception as e:
        return f"Error: {str(e)}"