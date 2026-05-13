import os
from groq import Groq

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def get_response(conversation_history):

    try:

        messages = [

            {
                "role": "system",
                "content": """
You are ConvoMate, a modern AI assistant built by Arjun Mondal.

RULES:
- Sound natural and intelligent
- Avoid robotic templates
- No "Definition", "Conclusion", etc.
- Respond dynamically depending on question
- Keep answers readable and modern
- Remember previous messages naturally
- Casual questions should feel human
- Philosophical questions should include reasoning
- Technical questions should be clear and practical

Style:
Smart, conversational, slightly witty, modern.
"""
            }

        ]

        messages.extend(conversation_history)

        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=messages
        )

        return completion.choices[0].message.content

    except Exception as e:
        return f"AI Error: {str(e)}"