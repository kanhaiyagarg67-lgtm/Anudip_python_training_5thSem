'''Attendance for 15 days is recorded as: 
attendance = ['P', 'P', 'A', 'P', 'A', 'P', 'P', 'P', 'A', 'P', 'P', 'A', 'P', 'P', 'P'] 
Write a program to: 
• Count present and absent days.  
• Calculate attendance percentage.  
• Determine eligibility (minimum 75% attendance).  
• Display positions where the student was absent. '''



#creating record of attendace

attendance = ['P', 'P', 'A', 'P', 'A', 'P', 'P', 'P', 'A', 'P', 'P', 'A', 'P', 'P', 'P'] 
#Task-1 To Count present and absent days 

# Counter for present days
present = 0

# Counter for absent days
absent = 0

# Traverse through the slots list using index
for i in range(len(attendance)):

    # Check if present  in attendance
    if attendance[i] == "P":
        present += 1

    # Check if absent in attendance
    if attendance[i] == "A":
        absent += 1

print("Present days:", present)
print("Absent days: ", absent)
print("----------------------------")

#Task-2 To Calculate attendance percentage.  
print("Attendance Percentage is :")
percentage = ((present / (present + absent)) * 100)
print(percentage)
print("------------------------------")

#Task-3 Determine eligibility (minimum 75% attendance). 
if percentage >= 75:
    print("Student is eligible ")
else:
    print("Student not eligible")
print("--------------------------------")


#Task-4 To Display positions where the student was absent. 
print("days at which students were absent")
positions_absent=[] 
for i in range(len(attendance)):
    if attendance[i]== "A":
        positions_absent.append(i + 1)
print(positions_absent)
