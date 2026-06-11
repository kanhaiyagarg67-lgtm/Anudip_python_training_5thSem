'''. Vehicle Number Plate Verification 
Problem Statement 
A vehicle number plate is entered: 
MH12AB4589 
Tasks 
Write a program to: 
1. Extract state code.  
2. Extract district code.  
3. Extract vehicle series.  
4. Extract vehicle number.  
5. Count letters and digits separately.  
6. Verify:  
o First 2 characters must be alphabets.  
o Next 2 must be digits.  
o Next 2 must be alphabets.  
o Last 4 must be digits.  
7. Display whether the number plate is valid. '''
#display the number
number_plate = "MH12AB4589"

print("Vehicle Number:", number_plate)

# 1. Extract state code
state_code = number_plate[0:2]

# 2. Extract district code
district_code = number_plate[2:4]

# 3. Extract vehicle series
series = number_plate[4:6]

# 4. Extract vehicle number
vehicle_number = number_plate[6:10]

print("State Code:", state_code)
print("District Code:", district_code)
print("Series:", series)
print("Vehicle Number:", vehicle_number)


# 5. Count letters and digits separately
letter_count = 0
digit_count = 0

for ch in number_plate:
    if ch >= 'A' and ch <= 'Z':
        letter_count = letter_count + 1

    elif ch >= '0' and ch <= '9':
        digit_count = digit_count + 1

print()
print("Total Letters:", letter_count)
print("Total Digits:", digit_count)


# 6. Verify number plate format
# First 2 characters must be alphabets
rule1 = state_code.isalpha()

# Next 2 characters must be digits
rule2 = district_code.isdigit()

# Next 2 characters must be alphabets
rule3 = series.isalpha()

# Last 4 characters must be digits
rule4 = vehicle_number.isdigit()

# Length should be exactly 10
rule5 = len(number_plate) == 10


# 7. Display valid or invalid
if rule1 and rule2 and rule3 and rule4 and rule5:
    print()
    print("Vehicle Number Status: Valid")
else:
    print()
    print("Vehicle Number Status: Invalid")


'''Sample Output 
Vehicle Number: MH12AB4589 
State Code: MH 
District Code: 12 
Series: AB 
Vehicle Number: 4589 
 
Total Letters: 4 
Total Digits: 6 
 
Vehicle Number Status: Valid
