'''
Problem Statement:
1. Display failed product IDs.
2. Count passed and failed products.
3. Calculate pass percentage.
4. Stop checking if 3 failures are found.
'''

# List containing tuples:
# (Product ID, Quality Status)
products = [
    (101, "Pass"),
    (102, "Fail"),
    (103, "Pass"),
    (104, "Fail"),
    (105, "Pass")
]

# -------------------------------------
# Task 1: Display failed product IDs
# -------------------------------------

print("Failed product IDs are:")

# Traverse each tuple in the list
for product in products:

    # Check if status is Fail
    if product[1] == "Fail":

        # Display Product ID
        print(product[0])

print("--------------------------")

# -------------------------------------
# Task 2: Count passed and failed products
# -------------------------------------

print("No. of Passed and Failed products are:")

# Counters for passed and failed products
passed = 0
failed = 0

# Traverse the list
for product in products:

    # Check pass status
    if product[1] == "Pass":
        passed += 1

    # Otherwise count failure
    else:
        failed += 1

# Display counts
print("Passed products are:", passed)
print("Failed products are:", failed)

print("--------------------------")

# -------------------------------------
# Task 3: Calculate pass percentage
# -------------------------------------

print("Pass Percentage is:")

# Formula:
# (Passed Products / Total Products) × 100
percentage = (passed / (passed + failed)) * 100

print(percentage, "%")

print("----------------------------")

# -------------------------------------
# Task 4: Stop checking if 3 failures are found
# -------------------------------------

failure_count = 0

# Traverse products one by one
for product in products:

    # Check if current product failed
    if product[1] == "Fail":

        # Increase failure counter
        failure_count += 1

        # Stop inspection after 3 failures
        if failure_count == 3:
            print("3 failures found. Stopping inspection.")
            break
