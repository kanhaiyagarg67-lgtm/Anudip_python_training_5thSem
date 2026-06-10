'''. License Key Verification System 
Problem Statement 
A software license key is entered: 
ABCD-EFGH-IJKL-MNOP 
Tasks 
Write a program to: 
1. Verify there are exactly 4 groups.  
2. Verify each group contains exactly 4 characters.  
3. Count total letters.  
4. Count vowels.  
5. Remove hyphens and display the merged key.  
6. Create a list containing all groups.  
7. Display whether the key format is valid.  '''

license_key = "ABCD-EFGH-IJKL-MNOP"

print("License Key:")
print(license_key)

# 1. Create a list containing all groups
# split("-") breaks the key wherever hyphen is present
groups = license_key.split("-")

print()
print("Groups:")
print(groups)

# 2. Verify there are exactly 4 groups
number_of_groups = len(groups)

print()
print("Number of Groups:", number_of_groups)

# 3. Verify each group contains exactly 4 characters
group_length_correct = True

for group in groups:
    if len(group) != 4:
        group_length_correct = False


# 4. Count total letters
total_letters = 0

for ch in license_key:
    if ch >= 'A' and ch <= 'Z':
        total_letters = total_letters + 1

print()
print("Total Letters:", total_letters)


# 5. Count vowels
total_vowels = 0

for ch in license_key:
    if ch in "AEIOUaeiou":
        total_vowels = total_vowels + 1

print("Total Vowels:", total_vowels)


# 6. Remove hyphens and display merged key
merged_key = ""

for ch in license_key:
    if ch != "-":
        merged_key = merged_key + ch

print()
print("Merged Key:")
print(merged_key)


# 7. Display whether the key format is valid
# Valid rules:
# - There should be exactly 4 groups
# - Each group should contain exactly 4 characters
# - All characters inside groups should be alphabets

all_letters = True

for group in groups:
    for ch in group:
        if not ((ch >= 'A' and ch <= 'Z') or (ch >= 'a' and ch <= 'z')):
            all_letters = False

print()

if number_of_groups == 4 and group_length_correct == True and all_letters == True:
    print("License Key Status: Valid")
else:
    print("License Key Status: Invalid")

'''
Sample Output 
License Key: 
ABCD-EFGH-IJKL-MNOP 
 
Groups: 
['ABCD', 'EFGH', 'IJKL', 'MNOP'] 
 
Number of Groups: 4 
 
Total Letters: 16 
Total Vowels: 4 
 
Merged Key: 
ABCDEFGHIJKLMNOP 
 
License Key Status: Valid
