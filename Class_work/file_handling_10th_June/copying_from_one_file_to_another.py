# Program to copy entire content from one file into another

# Open the source file in read mode
filev = open('sentence.txt', 'r')

# Check whether the file is opened successfully
# (This check is unnecessary because open() raises an exception if the file is not found)
if not filev:
    exit("Error opening the file.")

# Read the complete content of the source file
content = filev.read()

# Open the destination file in write mode
# If the file does not exist, it will be created
# If it already exists, its old content will be overwritten
filev1 = open('sentence1.txt', 'w')

# Write the copied content into the destination file
filev1.write(content)

# Display success message
print("Data successfully written into the file")

# Close destination file
filev1.close()

# Close source file
filev.close()
