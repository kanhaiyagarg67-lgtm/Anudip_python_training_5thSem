# Reverse number means writing the digits of a number in opposite order
# Example: Reverse of 1234 is 4321

# Palindrome number means original number and reverse number are same
# Example: 1221 reverse is also 1221, so it is a palindrome number

# Take input from user
num = int(input("Enter a number: "))

# Store original number because num will change during reversing
original = num

# Variable to store reverse number
reverse = 0

# Loop to reverse the number
while num > 0:
    # Get the last digit of the number
    digit = num % 10

    # Add digit at the end of reverse number
    reverse = reverse * 10 + digit

    # Remove the last digit from number
    num = num // 10

# Display reverse number
print("Reverse:", reverse)

# Check whether original number and reverse number are same
if reverse == original:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")
