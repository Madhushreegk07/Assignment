# Leap Year Checker with Explanation

year = int(input("Enter a year: "))

# Check leap year with reason
if year % 400 == 0:
    print(f"{year} is a Leap Year ✅")
    print("Reason: Divisible by 400.")

elif year % 100 == 0:
    print(f"{year} is NOT a Leap Year ❌")
    print("Reason: Divisible by 100 but not by 400.")

elif year % 4 == 0:
    print(f"{year} is a Leap Year ✅")
    print("Reason: Divisible by 4 but not by 100.")

else:
    print(f"{year} is NOT a Leap Year ❌")
    print("Reason: Not divisible by 4.")