'''Problem 6: Employee Attendance Monitoring System 
Problem Statement 
Employee attendance records are stored in attendance.txt. 
Sample Input/Data (attendance.txt) 
EMP101,P 
EMP102,A 
EMP103,P 
EMP104,P 
EMP105,A 
EMP106,P 
EMP107,P 
EMP108,A 
EMP109,P 
EMP110,P 
Tasks 
1. Count present and absent employees.  
2. Display absent employee IDs.  
3. Calculate attendance percentage.  
4. Generate an absentee report in absent_report.txt.  
5. Display employees eligible for attendance awards (100% attendance).  '''


attendance = [
    "EMP101,P",
    "EMP102,A",
    "EMP103,P",
    "EMP104,P",
    "EMP105,A",
    "EMP106,P",
    "EMP107,P",
    "EMP108,A",
    "EMP109,P",
    "EMP110,P"
]

with open("attendance.txt", "w") as file:
    for record in attendance:
        file.write(record + "\n")

#Count present and absent employees.  
present = 0
absent = 0
absent_ids = []  # Display absent employee IDs.  

with open("attendance.txt", "r") as file:
    for line in file:
        data = line.strip().split(",")

        emp_id = data[0]
        status = data[1]

        if status == "P":
            present += 1
        else:
            absent += 1
            absent_ids.append(emp_id)  # add id in list

print("Present Employees:", present)
print("Absent Employees:", absent)

print("Absent Employee IDs:")
for emp in absent_ids:
    print(emp)

percentage = present / (present + absent) * 100
print("Attendance Percentage:", percentage, "%")
print("----------------------------------")

#Generate an absentee report in absent_report.txt.

with open("absent_report.txt", "w") as file:
    for emp in absent_ids:
        file.write(emp + "\n")

print("Absentee Report Generated Successfully.")
print("------------------------------------")
#Display employees eligible for attendance awards (100% attendance). 

print("Attendance Award Eligibility:")
if absent == 0:
    print("All employees eligible")
else:
    print("Not Applicable")

'''
Sample Output 
Present Employees: 7 
 
Absent Employees: 3 
 
Absent Employee IDs: 
EMP102 
EMP105 
EMP108 
 
Attendance Percentage: 70.0% 
 
Absentee Report Generated Successfully. 
 
Attendance Award Eligibility: 
Not Applicable '''
