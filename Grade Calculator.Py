# Grade Calculator Program

# Taking marks input
sub1 = float(input("Enter marks for Subject 1: "))
sub2 = float(input("Enter marks for Subject 2: "))
sub3 = float(input("Enter marks for Subject 3: "))
sub4 = float(input("Enter marks for Subject 4: "))
sub5 = float(input("Enter marks for Subject 5: "))

# Total and Percentage
total_marks = sub1 + sub2 + sub3 + sub4 + sub5
percentage = total_marks / 5

# Grade Calculation
if percentage >= 90:
    grade = "A+"
elif percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 50:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "F"

# Pass / Fail (all subjects >= 40)
if sub1 >= 40 and sub2 >= 40 and sub3 >= 40 and sub4 >= 40 and sub5 >= 40:
    result = "PASS"
else:
    result = "FAIL"

# Display Results
print("\n========= RESULT SUMMARY =========")
print(f"Subject 1 Marks : {sub1}")
print(f"Subject 2 Marks : {sub2}")
print(f"Subject 3 Marks : {sub3}")
print(f"Subject 4 Marks : {sub4}")
print(f"Subject 5 Marks : {sub5}")
print(f"Total Marks     : {total_marks} / 500")
print(f"Percentage      : {percentage:.2f}%")
print(f"Grade           : {grade}")
print(f"Result          : {result}")
print("==================================")