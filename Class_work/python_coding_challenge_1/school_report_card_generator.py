'''Problem 4: School Report Card Generator 
Problem Statement 
Student marks are stored in marks.txt. 
Sample Input/Data (marks.txt) 
S101,Anuj,92 
S102,Rahul,76 
S103,Priya,88 
S104,Neha,45 
S105,Amit,58 
S106,Sneha,95 
S107,Karan,81 
S108,Pooja,73 
S109,Rohit,39 
S110,Anjali,90 
Tasks 
1. Calculate grades for all students.  
Passed Students: 9 
Failed Students: 1 
2. Generate a report card file report_card.txt.  
3. Display topper details.  
4. Count pass and fail students.  
5. Display students eligible for merit certificates (marks ≥ 90).  '''

# enter the details of students
students = [
    "S101,Anuj,92",
    "S102,Rahul,76",
    "S103,Priya,88",
    "S104,Neha,45",
    "S105,Amit,58",
    "S106,Sneha,95",
    "S107,Karan,81",
    "S108,Pooja,73",
    "S109,Rohit,39",
    "S110,Anjali,90"
]

with open("marks.txt", "w") as file:
    for student in students:
        file.write(student + "\n")

topper_name = ""
topper_marks = 0
passed = 0
failed = 0
merit = []

with open("marks.txt", "r") as file:      
    with open("report_card.txt", "w") as report:   #Generate a report card file report_card.txt.
        for line in file:
            data = line.strip().split(",")

            roll = data[0]
            name = data[1]
            marks = int(data[2])

            if marks >= 90:
                grade = "A"
                merit.append(name)
            elif marks >= 75:
                grade = "B"
            elif marks >= 50:
                grade = "C"
            else:
                grade = "Fail"

            if marks >= 40:
                passed += 1
            else:
                failed += 1
             
            if marks > topper_marks:  #Display topper details.
                topper_marks = marks
                topper_name = name

            report.write(roll + "," + name + "," + str(marks) + "," + grade + "\n")

print("Topper:")
print(topper_name, "(", topper_marks, ")")

#Count pass and fail students. 
print("Passed Students:", passed)
print("Failed Students:", failed)

#Display students eligible for merit certificates (marks ≥ 90). 
print("Merit Certificate Holders:")
for name in merit:
    print(name)

print("Report Cards Generated Successfully.")

'''
Sample Output 
Topper: 
Sneha (95) 
 
Merit Certificate Holders: 
Anuj 
Sneha 
Anjali 
 
Report Cards Generated Successfully.'''
