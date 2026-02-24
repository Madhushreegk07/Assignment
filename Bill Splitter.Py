# Bill Splitter Program

# Taking inputs
total_bill = float(input("Enter total bill amount: "))
people = int(input("Enter number of people: "))
tax_percent = float(input("Enter tax percentage: "))
tip_percent = float(input("Enter tip percentage: "))

# Calculations
subtotal = total_bill
tax_amount = subtotal * (tax_percent / 100)
bill_after_tax = subtotal + tax_amount
tip_amount = bill_after_tax * (tip_percent / 100)
total_final_bill = bill_after_tax + tip_amount
amount_per_person = total_final_bill / people

# Display Results
print("\n========= BILL SUMMARY =========")
print(f"Subtotal           : ₹{subtotal:.2f}")
print(f"Tax Amount         : ₹{tax_amount:.2f}")
print(f"Bill After Tax     : ₹{bill_after_tax:.2f}")
print(f"Tip Amount         : ₹{tip_amount:.2f}")
print(f"Total Bill         : ₹{total_final_bill:.2f}")
print(f"Amount Per Person  : ₹{amount_per_person:.2f}")
print("================================")