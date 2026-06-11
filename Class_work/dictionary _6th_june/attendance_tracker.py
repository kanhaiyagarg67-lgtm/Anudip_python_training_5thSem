# Create an empty dictionary to store attendance

attendance = {}

# taking  attendance record of 30 students
for i in range(30):
    # Key = Roll Number, Value = Attendance Status
    # Take roll number as input
    roll_no = int(input("Enter Roll Number: "))

    # Take attendance status (P for Present, A for Absent)
    status = input("Present or Absent (P/A): ").upper()

    # Store attendance in dictionary As roll no. and attendance status
    if status == "P":
        attendance[roll_no] = "Present"
    else:
        attendance[roll_no] = "Absent"

# Displaying the complete attendance record
print("Attendance Record:")
print(attendance)

# Displaying roll numbers of students who are present
print("Roll Numbers of Present Students:")

# Traverse the dictionary
present_roll_no=[]
for roll_no, status in attendance.items():

    # Check if the student is present
    if status == "Present":

        # Print the roll number of present student
        present_roll_no.append(roll_no)
        print(present_roll_no)
