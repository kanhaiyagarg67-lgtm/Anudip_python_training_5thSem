#program for atm transaction history analyzer
# List of transactions
# Positive values = deposits
# Negative values = withdrawals
transactions = [5000, -2000, 3000, -1000, -500, 7000]

# Variable to store current balance
balance = 0

# Variables to count deposits and withdrawals
deposit_count = 0
withdrawal_count = 0

# Empty lists to store deposits and withdrawals separately
deposits = []
withdrawals = []

# Variables to find largest deposit and largest withdrawal
largest_deposit = 0
largest_withdrawal = 0

# Loop through each transaction
for amount in transactions:

    # Add every transaction to balance
    balance = balance + amount

    # If amount is positive, it is a deposit
    if amount > 0:
        deposits.append(amount)
        deposit_count = deposit_count + 1

        # Check largest deposit
        if amount > largest_deposit:
            largest_deposit = amount

    # If amount is negative, it is a withdrawal
    elif amount < 0:
        withdrawals.append(amount)
        withdrawal_count = withdrawal_count + 1

        # Check largest withdrawal
        # -2000 is larger withdrawal than -1000
        if amount < largest_withdrawal:
            largest_withdrawal = amount

# Display all results
print("Current Balance:", balance)
print("Total Deposits:", deposit_count)
print("Total Withdrawals:", withdrawal_count)
print("Largest Deposit:", largest_deposit)
print("Largest Withdrawal:", largest_withdrawal)
print("Deposits List:", deposits)
print("Withdrawals List:", withdrawals)
