# String Manipulator Program

# Taking input from user
sentence = input("Enter a sentence: ")

# Calculations
original = sentence
total_chars_with_spaces = len(sentence)
total_chars_without_spaces = len(sentence.replace(" ", ""))
total_words = len(sentence.split())
uppercase = sentence.upper()
lowercase = sentence.lower()
title_case = sentence.title()

words = sentence.split()
first_word = words[0] if words else ""
last_word = words[-1] if words else ""

reversed_sentence = sentence[::-1]

# Display Results
print("\n====== STRING MANIPULATOR RESULTS ======")
print(f"Original Sentence            : {original}")
print(f"Total Characters (spaces)    : {total_chars_with_spaces}")
print(f"Characters (no spaces)       : {total_chars_without_spaces}")
print(f"Total Words                  : {total_words}")
print(f"UPPERCASE                    : {uppercase}")
print(f"lowercase                    : {lowercase}")
print(f"Title Case                   : {title_case}")
print(f"First Word                   : {first_word}")
print(f"Last Word                    : {last_word}")
print(f"Reversed Sentence            : {reversed_sentence}")
print("========================================")