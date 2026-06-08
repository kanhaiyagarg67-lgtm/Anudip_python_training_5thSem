# program for employee salary processing
#enter the employees with salary in dictionary
salary = {
    "EMP101": 45000,
    "EMP102": 62000,
    "EMP103": 38000,
    "EMP104": 75000,
    "EMP105": 54000,
    "EMP106": 29000,
    "EMP107": 82000,
    "EMP108": 48000,
    "EMP109": 36000,
    "EMP110": 68000
}

# Display employees earning above 60000
print("Employees earning above ₹60000:")
for emp, sal in salary.items():
    if sal > 60000:
        print(emp, sal)

# Count employees earning below 40000
count = 0
for sal in salary.values():
    if sal < 40000:
        count += 1
print("Employees earning below ₹40000:", count)

# Find highest-paid employee
highest_emp = max(salary, key=salary.get)
print("Highest-paid employee:", highest_emp, salary[highest_emp])

# Employees eligible for bonus
bonus = []
for emp, sal in salary.items():
    if sal > 50000:
        bonus.append(emp)
print("Employees eligible for bonus:", bonus)

# Calculate average salary
total = 0
for sal in salary.values():
    total += sal

average = total / len(salary)
print("Average salary:", average)
