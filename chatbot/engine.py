import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SYSTEM_PROMPT = """
You are ConvoMate, a helpful AI assistant.
Be natural, conversational, and precise.
Avoid long rigid formatting.
"""


def normalize_content(content):
    """
    Forces everything into a clean string (fixes your error)
    """
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        return " ".join(str(x) for x in content)
    if content is None:
        return ""
    return str(content)


def get_response(history):
    try:
        messages = [{"role": "system", "content": SYSTEM_PROMPT}]

        for msg in history:
            messages.append({
                "role": msg["role"],
                "content": normalize_content(msg["content"])
            })

        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=messages
        )

        return completion.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"