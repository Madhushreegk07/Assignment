from huggingface_hub import InferenceClient

def main():
    # 1. Update this with your NEW token after checking the permissions!
    api_key = "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" 
    
    # 2. Force the standard Inference API instead of the router
    client = InferenceClient(api_key=api_key)

    user_input = input("Enter your prompt: ")

    try:
        print("\nThinking...")
        
        # We use a model that Hugging Face hosts directly to avoid the 403 error
        # 'HuggingFaceH4/zephyr-7b-beta' is a great, smart, and free model
        response = client.chat_completion(
            model="HuggingFaceH4/zephyr-7b-beta",
            messages=[{"role": "user", "content": user_input}],
            max_tokens=200,
        )

        print("\nExplanation:")
        # Print the actual text from the response
        print(response.choices[0].message.content)

    except Exception as e:
        print(f"\nExplanation: {str(e)}")

if _name_ == "_main_":
    main()