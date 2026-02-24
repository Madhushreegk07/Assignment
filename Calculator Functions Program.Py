# Calculator Functions Program

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b


def modulus(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a % b


def power(a, b):
    return a ** b


def calculator():
    while True:
        print("\n========= CALCULATOR MENU =========")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Power")
        print("7. Exit")
        print("==================================")

        choice = input("Enter your choice (1-7): ")

        if choice == "7":
            print("Calculator closed. Goodbye!")
            break

        if choice in ["1", "2", "3", "4", "5", "6"]:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numbers only.")
                continue

            if choice == "1":
                result = add(num1, num2)
            elif choice == "2":
                result = subtract(num1, num2)
            elif choice == "3":
                result = multiply(num1, num2)
            elif choice == "4":
                result = divide(num1, num2)
            elif choice == "5":
                result = modulus(num1, num2)
            elif choice == "6":
                result = power(num1, num2)

            print("Result:", result)
        else:
            print("Invalid choice! Please select between 1 and 7.")


# Run the calculator
calculator()