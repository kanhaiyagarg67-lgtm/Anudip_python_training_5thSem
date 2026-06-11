# Accept secret code from user
code = int(input("Enter 6 digit code: "))

# Store code in temporary variable
temp = code

# Variable to count digits
count = 0

# Count number of digits
while temp > 0:
    count = count + 1
    temp = temp // 10

# Check whether code has exactly 6 digits
if count == 6:

    # Get last 3 digits
    last3 = code % 1000

    # Get first 3 digits
    first3 = code // 1000

    # Variables to store sum of digits
    sum_first = 0
    sum_last = 0

    # Find sum of first 3 digits
    while first3 > 0:
        sum_first = sum_first + first3 % 10
        first3 = first3 // 10

    # Find sum of last 3 digits
    while last3 > 0:
        sum_last = sum_last + last3 % 10
        last3 = last3 // 10

    # Compare both sums
    if sum_first == sum_last:
        print("Valid Code")
    else:
        print("Invalid Code")

else:
    print("Invalid Code")
