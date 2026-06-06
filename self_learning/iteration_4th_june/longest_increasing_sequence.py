# Accept how many numbers user wants to enter
n = int(input("Enter how many numbers: "))

# Take first number separately
first = int(input("Enter number 1: "))

# Current increasing sequence length
current_length = 1

# Longest increasing sequence length
longest_length = 1

# Store first number as previous number
previous = first

# Start loop from second number
for i in range(2, n + 1):

    # Accept current number
    current = int(input("Enter number " + str(i) + ": "))

    # If current number is greater than previous number
    if current > previous:
        current_length = current_length + 1

    # Otherwise sequence breaks
    else:
        current_length = 1

    # Update longest sequence length
    if current_length > longest_length:
        longest_length = current_length

    # Update previous number
    previous = current

# Display result
print("Longest Sequence Length =", longest_length)
