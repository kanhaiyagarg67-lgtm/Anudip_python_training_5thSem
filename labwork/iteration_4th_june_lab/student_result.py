#program foe student result management system
# Variable to store total marks
total = 0

# Variable to count failed subjects
failed_subjects = 0

# Loop will run 5 times for 5 subjects
for i in range(1, 6):
    # Take marks of each subject
    marks = int(input("Enter marks of subject " + str(i) + ": "))

    # Add marks to total
    total = total + marks

    # Check if marks are less than 40
    # If yes, increase failed subject count
    if marks < 40:
        failed_subjects = failed_subjects + 1

# Calculate percentage
# Total subjects = 5, each subject is out of 100
percentage = total / 5

# Decide grade according to percentage
if percentage >= 90:
    grade = "A+"

elif percentage >= 75:
    grade = "A"

elif percentage >= 60:
    grade = "B"

elif percentage >= 40:
    grade = "C"

else:
    grade = "Fail"

# Display result
print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)
print("Number of Subjects Failed:", failed_subjects)
