# Age Calculator Program

# Get birth year from user
birth_year = int(input("Enter your birth year: "))

# Current year (you can change if needed)
current_year = 2026

# Calculations
age_years = current_year - birth_year
age_months = age_years * 12
age_days = age_years * 365      # approx
age_hours = age_days * 24
age_minutes = age_hours * 60
years_until_100 = 100 - age_years

# Display Results
print("\n====== AGE CALCULATOR ======")
print(f"Current Age        : {age_years} years")
print(f"Age in Months      : {age_months} months")
print(f"Age in Days        : {age_days} days")
print(f"Age in Hours       : {age_hours} hours")
print(f"Age in Minutes     : {age_minutes} minutes")
print(f"Years until 100    : {years_until_100} years")
print("=============================")