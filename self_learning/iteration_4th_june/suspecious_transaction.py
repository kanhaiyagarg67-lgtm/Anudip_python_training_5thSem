# Count transactions above ₹50,000
above_50000 = 0

# Count transactions below ₹1,000
below_1000 = 0

# Store total transaction amount
total_amount = 0

# Infinite loop to accept transactions continuously
while True:

    # Accept transaction amount
    amount = int(input("Enter transaction amount: "))

    # Stop when user enters -1
    if amount == -1:
        break

    # Add amount to total
    total_amount = total_amount + amount

    # Check transaction above ₹50,000
    if amount > 50000:
        above_50000 = above_50000 + 1

    # Check transaction below ₹1,000
    if amount < 1000:
        below_1000 = below_1000 + 1

# Display results
print("Transactions above ₹50000:", above_50000)
print("Transactions below ₹1000:", below_1000)
print("Total Transaction Amount:", total_amount)
