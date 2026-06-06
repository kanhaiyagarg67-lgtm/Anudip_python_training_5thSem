'''Create Attendance tracker of 30 students. Ask the user to input roll number of student and also 
input whether student is Present or Absent. Store the data in dictionary where roll number will 
be used as a key and Attendance as Value. 
Display the roll number of students who are Present'''

# Create an empty dictionary to store attendance
attendance = {}

# Loop will run 30 times for 30 students
for i in range(30):

    # Take roll number input from user
    roll_no = int(input("Enter roll number: "))

    # Take attendance status from user
    status = input("Enter attendance Present/Absent: ")

    # Store data as key-value pair
    # roll_no is key and status is value
    attendance[roll_no] = status

# Display the complete attendance dictionary
print("Attendance Dictionary:")
print(attendance)

# Display only those students who are Present
print(Roll numbers of Present students:")

# Traverse dictionary using roll number as key
for roll_no in attendance:

    # Check whether attendance value is Present
    if attendance[roll_no] == "Present":

        # Print roll number of present student
        print(roll_no)
