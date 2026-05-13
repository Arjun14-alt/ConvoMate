import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_response(user_input):

    system_prompt = """
You are ConvoMate, a smart real-world assistant.

Rules:
- Answer like ChatGPT, not Wikipedia
- Be aware of current events (sports, news, trending topics)
- If question is recent (matches, events), infer latest known info and respond naturally
- Keep answers conversational and updated in tone
- No rigid formatting
- Be confident and slightly opinionated when needed
"""

    try:
        res = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role":"system","content":system_prompt},
                {"role":"user","content":user_input}
            ]
        )

        return res.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"