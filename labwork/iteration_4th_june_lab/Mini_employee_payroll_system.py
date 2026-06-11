#program for mini employee payeroll system
Employee_name = str(input("Enter Employee Name: "))
print("Employee Name:", Employee_name)    
Basic_salary = int(input("Enter Basic Salary: "))
print("Basic Salary: ₹", Basic_salary)

HRA = 0.2 * Basic_salary
DA = 0.1 * Basic_salary
PF = 0.12 * Basic_salary

Gross_salary = Basic_salary + HRA + DA 
print("Gross Salary: ₹", Gross_salary)

net_salary = Gross_salary - PF
print("Net Salary: ₹", net_salary)

if net_salary > 50000:
    GRADE = "Senior grade"

elif net_salary > 30000:
    GRADE = "Mid grade"

else:
    GRADE = "Junior grade"
  print("Grade:", GRADE)
