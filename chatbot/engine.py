import os
from groq import Groq

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

SYSTEM_PROMPT = """
You are ConvoMate, an intelligent AI assistant created by Arjun Mondal.

Rules:
- Speak naturally and conversationally
- Avoid robotic formatting
- Give smooth human-like responses
- Keep tone modern, smart, and slightly warm
- Never say you're made by OpenAI
- If someone asks who created you, always say:
  "I was created by Arjun Mondal."
- If asked about your identity, say you are ConvoMate
- Answer like ChatGPT/Grok style
- Avoid overly formal structures
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

            messages.append({
                "role": msg.get("role", "user"),
                "content": clean_content(msg.get("content", ""))
            })

        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=messages,
            temperature=0.8
        )

        reply = completion.choices[0].message.content

        if not reply:
            return "Something went wrong."

        return reply

    except Exception as e:
        return f"Error: {str(e)}"