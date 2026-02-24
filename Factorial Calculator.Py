# Factorial Calculator

num = int(input("Enter a number: "))

# Handle negative numbers
if num < 0:
    print("Factorial is not defined for negative numbers.")

# Handle 0
elif num == 0:
    print("0! = 1")

# Handle positive numbers
else:
    factorial = 1
    steps = ""

    for i in range(num, 0, -1):
        factorial *= i
        steps += str(i)
        if i != 1:
            steps += " x "

    print(f"{num}! = {steps} = {factorial}")