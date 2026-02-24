# Multiplication Table Generator

# Take input from user
num = int(input("Enter a number to generate its multiplication table: "))
limit = int(input("Enter the limit: "))

print("\nMultiplication Table for", num)
print("-----------------------------")

for i in range(1, limit + 1):
    print(f"{num} x {i} = {num * i}")