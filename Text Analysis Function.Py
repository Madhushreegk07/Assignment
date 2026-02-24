# Text Analysis Functions Program

def count_characters(text):
    return len(text)


def count_words(text):
    words = text.split()
    return len(words)


def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    return count


def count_consonants(text):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch.isalpha() and ch not in vowels:
            count += 1
    return count


def convert_uppercase(text):
    return text.upper()


def convert_lowercase(text):
    return text.lower()


def text_analysis():
    text = input("Enter a text: ")

    while True:
        print("\n===== TEXT ANALYSIS MENU =====")
        print("1. Count Characters")
        print("2. Count Words")
        print("3. Count Vowels")
        print("4. Count Consonants")
        print("5. Convert to Uppercase")
        print("6. Convert to Lowercase")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            print("Total Characters:", count_characters(text))

        elif choice == "2":
            print("Total Words:", count_words(text))

        elif choice == "3":
            print("Total Vowels:", count_vowels(text))

        elif choice == "4":
            print("Total Consonants:", count_consonants(text))

        elif choice == "5":
            print("Uppercase Text:", convert_uppercase(text))

        elif choice == "6":
            print("Lowercase Text:", convert_lowercase(text))

        elif choice == "7":
            print("Exiting Text Analysis Program. Goodbye!")
            break

        else:
            print("Invalid choice! Please select between 1 and 7.")


# Run the program
text_analysis()