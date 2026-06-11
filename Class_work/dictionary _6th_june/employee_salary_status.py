'''
WAP to create a dictionary that contains the record of 10 employees.

Employee ID is used as the key and salary is used as the value.

Find:
1. Total number of employees having salary greater than 30000.
2. List of employees whose salary is below 20000.
'''

# Create an empty dictionary to store employee records
# Key   -> Employee ID
# Value -> Employee Salary
employees = {}

# Taking input for 10 employees
for i in range(10):

    # Input employee ID from the user
    employee_id = input("Enter the Employee ID: ")

    # Input employee salary from the user
    salary = int(input("Enter the salary of the employee: "))

    # Store employee ID and salary in the dictionary
    employees[employee_id] = salary

# Display the complete employee dictionary
print("Employee Records:")
print(employees)

# Display heading for employees with salary greater than 30000
print("Total No. of Employees having salary greater than 30000")

# Variable to count employees whose salary is above 30000
count = 0

# Traverse only the salary values in the dictionary
for sal in employees.values():

    # Check if salary is greater than 30000
    if sal > 30000:

        # Increment counter if condition is satisfied
        count += 1

# Display the final count
print(count)

# Display heading for employees with salary below 20000
print("List of employees whose salary is below 20000:")

# Traverse both employee ID and salary
for emp_id, sal in employees.items():

    # Check if salary is less than 20000
    if sal < 20000:

        # Display employee ID and salary
        print("Employee ID:", emp_id, "Salary:", sal)
