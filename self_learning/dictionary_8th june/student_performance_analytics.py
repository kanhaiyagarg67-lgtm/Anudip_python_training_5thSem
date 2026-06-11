'''
 Student Performance Analytics System 
Problem Statement 
A coaching institute wants to analyze student performance. 
Store details of at least 30 students in a dictionary. 
Example Structure 
students = { 
    "S101": {"name": "Anuj", "marks": 85}, 
    "S102": {"name": "Rahul", "marks": 72} 
} 
Requirements 
1. Display all student records.  
2. Search a student using Student ID.  
3. Add a new student.  
4. Update marks of an existing student.  
5. Delete a student.  
6. Find topper and lowest scorer.  
7. Calculate class average.  
8. Count pass and fail students.  
9. Generate grades:  
o A (90+)  
o B (75–89)  
o C (50–74)  
o F (<50)  
10. Display students scoring above average.  
11. Display top 5 performers.  
12. Create a separate dictionary for scholarship students (marks > 85). '''


# Student Performance Analytics System

# Store details of 30 students in nested dictionary
students = {
    "S101": {"name": "Anuj", "marks": 85},
    "S102": {"name": "Rahul", "marks": 72},
    "S103": {"name": "Priya", "marks": 91},
    "S104": {"name": "Neha", "marks": 66},
    "S105": {"name": "Amit", "marks": 45},
    "S106": {"name": "Rohan", "marks": 88},
    "S107": {"name": "Karan", "marks": 39},
    "S108": {"name": "Pooja", "marks": 76},
    "S109": {"name": "Sneha", "marks": 95},
    "S110": {"name": "Arjun", "marks": 58},

    "S111": {"name": "Diya", "marks": 82},
    "S112": {"name": "Kabir", "marks": 49},
    "S113": {"name": "Isha", "marks": 90},
    "S114": {"name": "Manav", "marks": 61},
    "S115": {"name": "Tanya", "marks": 73},
    "S116": {"name": "Riya", "marks": 87},
    "S117": {"name": "Dev", "marks": 34},
    "S118": {"name": "Meera", "marks": 79},
    "S119": {"name": "Yash", "marks": 55},
    "S120": {"name": "Nisha", "marks": 92},

    "S121": {"name": "Harsh", "marks": 68},
    "S122": {"name": "Simran", "marks": 81},
    "S123": {"name": "Varun", "marks": 47},
    "S124": {"name": "Anaya", "marks": 96},
    "S125": {"name": "Aditya", "marks": 71},
    "S126": {"name": "Sanya", "marks": 89},
    "S127": {"name": "Mohit", "marks": 52},
    "S128": {"name": "Khushi", "marks": 94},
    "S129": {"name": "Nitin", "marks": 43},
    "S130": {"name": "Aarav", "marks": 77}
}


# 1. Display all student records
print("All Student Records:")

for sid, details in students.items():
    print(sid, "->", details["name"], details["marks"])


# 2. Search a student using Student ID
search_id = input("\nEnter Student ID to search: ")

if search_id in students:
    print("Student Found")
    print("Name:", students[search_id]["name"])
    print("Marks:", students[search_id]["marks"])
else:
    print("Student ID not found")


# 3. Add a new student
new_id = input("\nEnter new Student ID: ")
new_name = input("Enter student name: ")
new_marks = int(input("Enter marks: "))

students[new_id] = {"name": new_name, "marks": new_marks}

print("New student added successfully")


# 4. Update marks of an existing student
update_id = input("\nEnter Student ID to update marks: ")

if update_id in students:
    new_marks = int(input("Enter new marks: "))
    students[update_id]["marks"] = new_marks
    print("Marks updated successfully")
else:
    print("Student ID not found")


# 5. Delete a student
delete_id = input("\nEnter Student ID to delete: ")

if delete_id in students:
    del students[delete_id]
    print("Student deleted successfully")
else:
    print("Student ID not found")


# 6. Find topper and lowest scorer
student_items = list(students.items())

topper_id = student_items[0][0]
topper_marks = student_items[0][1]["marks"]

lowest_id = student_items[0][0]
lowest_marks = student_items[0][1]["marks"]

for sid, details in students.items():
    if details["marks"] > topper_marks:
        topper_id = sid
        topper_marks = details["marks"]

    if details["marks"] < lowest_marks:
        lowest_id = sid
        lowest_marks = details["marks"]

print("\nTopper:")
print(topper_id, students[topper_id]["name"], topper_marks)

print("\nLowest Scorer:")
print(lowest_id, students[lowest_id]["name"], lowest_marks)


# 7. Calculate class average
total_marks = 0

for details in students.values():
    total_marks = total_marks + details["marks"]

average = total_marks / len(students)

print("\nClass Average:", average)


# 8. Count pass and fail students
pass_count = 0
fail_count = 0

for details in students.values():
    if details["marks"] >= 50:
        pass_count = pass_count + 1
    else:
        fail_count = fail_count + 1

print("\nPass Students:", pass_count)
print("Fail Students:", fail_count)


# 9. Generate grades
print("\nStudent Grades:")

for sid, details in students.items():
    marks = details["marks"]

    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    else:
        grade = "F"

    print(sid, details["name"], marks, "Grade:", grade)


# 10. Display students scoring above average
print("\nStudents Scoring Above Average:")

for sid, details in students.items():
    if details["marks"] > average:
        print(sid, details["name"], details["marks"])


# 11. Display top 5 performers
# Convert dictionary into list
student_list = list(students.items())

# Sort students according to marks in descending order
student_list.sort(key=lambda x: x[1]["marks"], reverse=True)

print("\nTop 5 Performers:")

for i in range(5):
    sid = student_list[i][0]
    name = student_list[i][1]["name"]
    marks = student_list[i][1]["marks"]

    print(sid, name, marks)


# 12. Create separate dictionary for scholarship students
scholarship_students = {}

for sid, details in students.items():
    if details["marks"] > 85:
        scholarship_students[sid] = details

print("\nScholarship Students:")

for sid, details in scholarship_students.items():
    print(sid, details["name"], details["marks"])
