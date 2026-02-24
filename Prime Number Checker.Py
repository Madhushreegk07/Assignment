# -------- Prime Number Checker --------

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


# -------- Part 1: Single Number Check --------
num = int(input("Enter a number: "))

if is_prime(num):
    print(f"{num} is a PRIME number")
else:
    print(f"{num} is NOT a prime number")


# -------- Part 2: Prime Numbers in Range --------
start = int(input("Enter start range: "))
end = int(input("Enter end range: "))

print("Prime numbers:", end=" ")

prime_list = []

for n in range(start, end + 1):
    if is_prime(n):
        prime_list.append(str(n))

print(", ".join(prime_list))