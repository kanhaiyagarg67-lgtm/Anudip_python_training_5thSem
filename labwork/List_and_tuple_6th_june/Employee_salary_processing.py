'''. Employee Salary Processing 
Problem Statement 
Employee data is stored as tuples: 
employees = [ 
    ("Rahul", 35000), 
    ("Priya", 55000), 
    ("Amit", 42000), 
    ("Neha", 65000) 
] 
Write a program to: 
• Display employees earning above ₹50,000.  
• Find the highest-paid employee.  
• Calculate total salary expenditure.  
• Count employees earning below ₹40,000.  '''

#creating employee data
employees = [
    ("Rahul", 35000),
    ("Priya", 55000),
    ("Amit", 42000),
    ("Neha", 65000)
]
#-----------------------------------------
#Task 1: To display employees earning above ₹50,000.
print("Employees earning above ₹50,000:")
for record in employees:
    if record[1]>50000:
        print(record[0],"->",record[1])
print("---------------------------------")
#Task 2: To find the highest-paid employee.
max_salary=0
for record in employees:
    if record[1]>max_salary:
        max_salary=record[1]
        highest_paid_employee=record[0]
print("Highest-paid employee:", highest_paid_employee, "-> ₹", max_salary)
print("---------------------------------")
#Task 3: To calculate total salary expenditure.
total_expenditure=0
for record in employees:
    total_expenditure+=record[1]
print("Total salary expenditure: ₹", total_expenditure)
print("---------------------------------")
#Task 4: To count employees earning below ₹40,000.
count=0
for record in employees:
    if record[1]<40000:
        count+=1
print("Number of employees earning below ₹40,000:", count)
