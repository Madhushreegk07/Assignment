# Simple Calculator Program

# Taking input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
modulus = num1 % num2
exponentiation = num1 ** num2

# Display Results
print("\n===== CALCULATOR RESULTS =====")
print(f"Addition        : {addition}")
print(f"Subtraction     : {subtraction}")
print(f"Multiplication  : {multiplication}")
print(f"Division        : {division}")
print(f"Modulus         : {modulus}")
print(f"Exponentiation  : {exponentiation}")
print("================================")