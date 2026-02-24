# Simple ATM Simulator

balance = 10000
minimum_balance = 500

while True:
    print("\nATM SIMULATOR")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        print(f"Current Balance: ₹{balance}")
    
    elif choice == "2":
        amount = float(input("Enter amount to deposit: ₹"))
        if amount > 0:
            balance += amount
            print("Deposit successful!")
            print(f"Updated Balance: ₹{balance}")
        else:
            print("Invalid deposit amount!")
    
    elif choice == "3":
        amount = float(input("Enter amount to withdraw: ₹"))
        
        if amount <= 0:
            print("Invalid withdrawal amount!")
        elif amount > balance:
            print("Insufficient balance!")
        elif balance - amount < minimum_balance:
            print(f"Minimum balance of ₹{minimum_balance} must be maintained!")
        else:
            balance -= amount
            print("Withdrawal successful!")
            print(f"Updated Balance: ₹{balance}")
    
    elif choice == "4":
        print("Thank you for using ATM. Goodbye!")
        break
    
    else:
        print("Invalid choice! Please select from 1 to 4.")