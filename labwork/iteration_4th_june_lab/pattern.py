# Take number of rows from user
rows = int(input("Enter number of rows: "))

# Print normal number pyramid
print("Number Pyramid:")

# Outer loop controls rows
for i in range(1, rows + 1):

    # Inner loop prints numbers from 1 to i
    for j in range(1, i + 1):
        print(j, end="")

    # Move to next line after each row
    print()

# Print reverse number pyramid
print("Reverse Pattern:")

# Outer loop starts from rows and goes down to 1
for i in range(rows, 0, -1):

    # Inner loop prints numbers from 1 to i
    for j in range(1, i + 1):
        print(j, end="")

    # Move to next line after each row
    print()
