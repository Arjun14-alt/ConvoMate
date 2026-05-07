import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def get_response(user_input):

    try:
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",

            messages=[
                {
                    "role": "system",
                    "content": """
You are ConvoMate, an intelligent assistant built by Arjun Mondal.

You are NOT Wikipedia and NOT a textbook.

RULES:
- First give a short direct answer (1–2 lines)
- Then explain in structured format only if needed:
    * Definition / Direct explanation
    * Context / Why it matters
    * Example (if useful)
    * Final insight or opinion
- Be conversational, not robotic
- Keep responses clean and easy to read
- For casual talk, respond naturally
- Avoid long paragraphs

Your style: smart, slightly opinionated, helpful assistant.
"""
                },
                {
                    "role": "user",
                    "content": user_input
                }
            ]
        )

        return completion.choices[0].message.content

    except Exception as e:
        return f"AI Error: {str(e)}"