# Accept number from user
num = int(input("Enter a number: "))

# Store number in temporary variable
temp = num

# Variable to count digits
digits = 0

# Count number of digits
while temp > 0:
    digits = digits + 1
    temp = temp // 10

# Mirror number must have even number of digits
if digits % 2 != 0:
    print("Not a Mirror Number")

else:
    # Find half length
    half = digits // 2

    # Divisor helps to split number into two halves
    divisor = 10 ** half

    # Get left half of number
    left_half = num // divisor

    # Get right half of number
    right_half = num % divisor

    # Compare both halves
    if left_half == right_half:
        print("Mirror Number")
    else:
        print("Not a Mirror Number")
