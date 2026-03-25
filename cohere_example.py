import cohere

# 1. Initialize the client (Required to call the API)
co = cohere.ClientV2(api_key="Y35HGivkJVFjx3gKcCd4ORnEguR5AlJtwY0CluGB")

user_message = input("Enter your question: ")

# 2. Use 'co.chat' instead of just 'chat'
response = co.chat(
    model="command-r-plus-08-2024", 
    messages=[{
        "role": "user",
        "content": user_message
    }]
)

print("\nCohere's Response:")
# 3. Access the first item [0] in the content list
print(response.message.content[0].text)