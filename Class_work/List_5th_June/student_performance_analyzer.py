#program for student performance analyzer
# List of students' marks
marks = [78, 45, 92, 35, 88, 40, 99, 56]

# Empty list to store marks of passed students
passed_students = []

# Variable to count failed students
failed_count = 0

# Empty list to store marks above 75
merit_list = []

# Assume first mark is highest and lowest
highest = marks[0]
lowest = marks[0]

# Loop through each mark in the list
for mark in marks:

    # If mark is 40 or more, student is passed
    if mark >= 40:
        passed_students.append(mark)

    # Otherwise student is failed
    else:
        failed_count += 1

    # Check for highest mark
    if mark > highest:
        highest = mark

    # Check for lowest mark
    if mark < lowest:
        lowest = mark

    # If mark is above 75, add it to merit list
    if mark > 75:
        merit_list.append(mark)

# Display all results
print("Passed Students:", passed_students)
print("Failed Count:", failed_count)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Merit List:", merit_list)
