
#Take units consumed from user
units = int(input("Enter Units Consumed: "))

# Calculate bill using slab rates
if units <= 100:
    bill = units * 5
    category = "Low Consumption"

elif units <= 200:
    bill = (100 * 5) + (units - 100) * 7
    category = "Medium Consumption"

else:
    bill = (100 * 5) + (100 * 7) + (units - 200) * 10
    category = "High Consumption"

# Display result
print("Units Consumed:", units)
print("Total Bill: ₹", bill)
print("Category:", category)
