'''Problem Statement 
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
• Count employees earning below ₹40,000.'''

#creating employee records

employees = [ 
    ("Rahul", 35000), 
    ("Priya", 55000), 
    ("Amit", 42000), 
    ("Neha", 65000) 
] 

#Task-1 To  display employees earning above ₹50,000.
print("Employees earning above ₹50,000 :")
for earning in employees:
    if(earning[1]>50000):
        print(earning[0])

#Task-2 To Find the highest-paid employee.  

print("Highest-paid Employee")
highest_paid = employees[0]

for employee in employees:
    if employee[1] > highest_paid[1]:
        highest_paid = employee

print(highest_paid[0])

#Task-3 To Calculate total salary expenditure
print("Total salary expenditure")
total_salary=0
for salary in employees:
    total_salary+=salary[1]
print(total_salary)


#Task-4 To Count employees earning below ₹40,000.
print("No. of employees earning below ₹40,000")
count=0 # for counting employees earning below ₹40,000.

for salary in employees:
    if (salary[1]<40000):
        count+=1
print(count)

