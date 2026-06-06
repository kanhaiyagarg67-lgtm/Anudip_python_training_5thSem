# Accept electricity units from user
units = int(input("Enter electricity units: "))

# Calculate bill according to slab
if units <= 100:

    # First 100 units charged at ₹5 per unit
    bill = units * 5

elif units <= 200:

    # First 100 units at ₹5
    # Remaining units at ₹7
    bill = (100 * 5) + ((units - 100) * 7)

else:

    # First 100 units at ₹5
    # Next 100 units at ₹7
    # Remaining units at ₹10
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

# Add 10% surcharge if bill exceeds ₹5000
if bill > 5000:
    surcharge = bill * 0.10
    bill = bill + surcharge

# Display final bill
print("Final Payable Amount: ₹", bill)
