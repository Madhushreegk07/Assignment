from groq import Groq

# client = Groq(api_key="")

import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def query_api(user_input):
    try:
        api_key = "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"

        if not api_key:
            raise ValueError("API key not found. Check your .env file.")

        client = Groq(api_key=api_key)

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": user_input}]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {e}"


if _name_ == "_main_":
    user_prompt = input("Enter your prompt: ")
    print("Querying Groq...")
    result = query_api(user_prompt)
    print("\nResponse:")
    print(result)