# Movie Ticket Pricing System

# Input
age = int(input("Enter age: "))
day = input("Enter day of the week: ").strip().lower()
tickets = int(input("Enter number of tickets: "))

# Determine base price based on age
if age < 3:
    base_price = 0
elif 3 <= age <= 12:
    base_price = 150
elif 13 <= age <= 59:
    base_price = 300
else:
    base_price = 200

# Determine discount
if day in ["friday", "saturday", "sunday"]:
    discount_rate = 0.20
else:
    discount_rate = 0

# Calculate discount amount per ticket
discount_amount = base_price * discount_rate
price_after_discount = base_price - discount_amount

# Calculate total amount
total_amount = price_after_discount * tickets

# Output
print("\n----- Ticket Summary -----")
print("Base Price per ticket: ₹", base_price)
print("Discount per ticket: ₹", discount_amount)
print("Price after discount per ticket: ₹", price_after_discount)
print("Total Amount: ₹", total_amount)