import google.generativeai as genai
import os

api_key = "AIzaSyDICiJVgV3E6a2V3ZsggfXEZ0SJR5z2NSw"
genai.configure(api_key=api_key)

def main():
    try:
        model = genai.GenerativeModel(model_name="gemini-2.5-flash")


        user_input = input("Enter your prompt: ")

        response = model.generate_content(user_input)


        print(response.text)


    except Exception as e:
        print("Error:", e)

if _name_ == "_main_":
    main()