import os
from langchain_groq import ChatGroq


def get_llm() -> tuple:
   
    key = os.getenv("GROQ_API_KEY", "").strip()

    if not key:
        return None, (
            "GROQ_API_KEY not found. "
            "Add it to your .env file:\n\nGROQ_API_KEY=gsk_your_key_here\n\n"
            "Get a free key at https://console.groq.com"
        )

    llm = ChatGroq(
        api_key=key,
        model_name="llama-3.1-8b-instant",
        temperature=0.1,
        max_tokens=512,
    )
    return llm, ""