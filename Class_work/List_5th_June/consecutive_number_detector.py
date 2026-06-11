#program for consecutive number detector
# List of numbers
numbers = [4, 5, 6, 10, 11, 15, 16, 17]

# Empty list to store consecutive pairs
consecutive_pairs = []

# Loop from index 0 to second last index
for i in range(len(numbers) - 1):

    # Check if next number is exactly 1 greater than current number
    if numbers[i + 1] == numbers[i] + 1:

        # Display consecutive numbers
        print(numbers[i], "and", numbers[i + 1], "are consecutive")

        # Store pair as tuple in list
        consecutive_pairs.append((numbers[i], numbers[i + 1]))

# Display all consecutive pairs
print("Consecutive Pairs:", consecutive_pairs)
