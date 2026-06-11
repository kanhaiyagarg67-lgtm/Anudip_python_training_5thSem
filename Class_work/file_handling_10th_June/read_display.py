'''
Classwork : To read the data from file and display:
1. Number of vowels in the file.
2. Number of characters in the file.
3. Number of lines in the file.
'''

# Open the file in read mode
filev = open('sentence.txt', 'r')

# Check whether the file is opened successfully
if not filev:
    exit("Error opening the file.")

# Read the complete file content as a string
content = filev.read()

# Initialize vowel counter
count_vowel = 0

# Traverse each character in the file
for ch in content:

    # Check if the character is a vowel
    if ch in "aeiouAEIOU":
        count_vowel += 1

# Display total number of vowels
print("No. of vowels =", count_vowel)

# Display total number of characters
print("No. of characters =", len(content))

# Close the file after reading
filev.close()

# Reopen the file to count lines
filev = open("sentence.txt", "r")

# Read all lines into a list
lines = filev.readlines()

# Display total number of lines
print("No. of lines =", len(lines))

# Close the file
filev.close()
