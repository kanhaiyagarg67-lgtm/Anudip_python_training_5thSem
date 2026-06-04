#program for atm simulation system
# Initial balance in the account
balance = 10000

# Loop will continue until user selects Exit
while True:
    # Display ATM menu
    print("\nATM Menu")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    # Take user's choice
    choice = int(input("Enter your choice: "))

    # Option 1: Check balance
    if choice == 1:
        print("Your current balance is: ₹", balance)

    # Option 2: Deposit money
    elif choice == 2:
        amount = int(input("Enter amount to deposit: "))

        # Add deposited amount to balance
        balance = balance + amount

        print("Amount deposited successfully.")
        print("Updated balance is: ₹", balance)

    # Option 3: Withdraw money
    elif choice == 3:
        amount = int(input("Enter amount to withdraw: "))

        # Check if withdrawal amount is less than or equal to balance
        if amount <= balance:
            balance = balance - amount
            print("Withdrawal successful.")
            print("Updated balance is: ₹", balance)
        else:
            print("Insufficient balance.")
            print("Withdrawal amount cannot exceed balance.")

    # Option 4: Exit from ATM
    elif choice == 4:
        print("Thank you for using ATM.")
        break

    # If user enters wrong choice
    else:
        print("Invalid choice. Please select from 1 to 4.")
