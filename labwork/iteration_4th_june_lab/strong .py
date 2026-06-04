# Take input from user
num = int(input("Enter a number: "))

# Store original number in temp variable
temp = num

# Variable to store sum of factorials of digits
sum = 0

# Loop runs until all digits are separated
while temp > 0:
    # Get the last digit of the number
    digit = temp % 10

    # Variable to store factorial of digit
    fact = 1

    # Calculate factorial of digit
    for i in range(1, digit + 1):
        fact = fact * i

    # Add factorial to sum
    sum = sum + fact

    # Remove last digit from number
    temp = temp // 10

# Check whether sum is equal to original number
if sum == num:
    print(num, "is a Strong Number")
else:
    print(num, "is not a Strong Number")
