import random

best_score = None  # Track minimum attempts used

while True:
    number = random.randint(1, 100)
    attempts = 7
    used_attempts = 0

    print("\n🎯 Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100.")
    print("You have 7 attempts to guess it.")

    while attempts > 0:
        try:
            guess = int(input("\nEnter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        used_attempts += 1
        attempts -= 1

        if guess == number:
            print(f"🎉 Congratulations! You guessed it in {used_attempts} attempts.")

            if best_score is None or used_attempts < best_score:
                best_score = used_attempts
                print("🏆 New best score!")

            break

        elif guess < number:
            print("Too low!")
        else:
            print("Too high!")

        # Bonus hint (within 5)
        if abs(guess - number) <= 5:
            print("🔥 Very close!")

        print(f"Attempts remaining: {attempts}")

    else:
        print(f"\n❌ Game over! The number was {number}.")

    # Show best score if exists
    if best_score is not None:
        print(f"🥇 Best score so far: {best_score} attempts")

    # Play again option
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! 👋")
        break