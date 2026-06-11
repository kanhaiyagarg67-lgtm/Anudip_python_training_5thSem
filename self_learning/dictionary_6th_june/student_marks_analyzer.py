#program for student marks analyzer
#enter student name and marks in dictionary
marks = {
    "Aarav": 78,
    "Diya": 92,
    "Rohan": 45,
    "Ishita": 88,
    "Kabir": 56,
    "Meera": 39,
    "Arjun": 95,
    "Saanvi": 67,
    "Vivaan": 82,
    "Anaya": 51
}

# Display students scoring 80 or above
print("Students scoring 80 or above:")
for name, mark in marks.items():
    if mark >= 80:
        print(name, mark)

# Count failed students
failed = 0
for mark in marks.values():
    if mark < 40:
        failed += 1
print("Failed students:", failed)

# Find highest scorer
highest_student = max(marks, key=marks.get)
print("Highest scorer:", highest_student, marks[highest_student])

# Students scoring between 60 and 75
between_60_75 = []
for name, mark in marks.items():
    if mark >= 60 and mark <= 75:
        between_60_75.append(name)
print("Students scoring between 60 and 75:", between_60_75)

# Assign grades
print("Grades:")
for name, mark in marks.items():
    if mark >= 90:
        grade = "A"
    elif mark >= 75:
        grade = "B"
    elif mark >= 50:
        grade = "C"
    else:
        grade = "F"

    print(name, ":", grade)
