# openai_test.py
import os
from openai import OpenAI

def main():
    try:
        # ⚠️ Replace this with your actual API key or use .env
        api_key = "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"

        if not api_key:
            raise ValueError("API key not found. Set your API key!")

        # Initialize OpenAI client
        client = OpenAI(api_key=api_key)

        # Get prompt from user
        user_input = input("Enter your prompt: ")

        # Create chat completion
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": user_input}]
        )

        # Print AI response
        print("\nAI Response:")
        print(response.choices[0].message['content'])

    except Exception as e:
        print("Error:", e)

if _name_ == "_main_":
    main()