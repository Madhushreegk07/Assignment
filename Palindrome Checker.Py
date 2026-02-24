print("🔎 Palindrome Checker")

user_input = input("Enter word/number: ")

# Store original value
original = user_input

# Convert to lowercase for case-insensitive comparison
processed = user_input.lower()

# Reverse step-by-step
reversed_text = ""
print("\nStep-by-step reversal:")

for char in processed:
    reversed_text = char + reversed_text
    print(f"Adding '{char}' -> {reversed_text}")

print("\nOriginal:", original)
print("Reversed:", reversed_text)

# Check palindrome
if processed == reversed_text:
    print("Result: PALINDROME ✅")
else:
    print("Result: NOT A PALINDROME ❌")