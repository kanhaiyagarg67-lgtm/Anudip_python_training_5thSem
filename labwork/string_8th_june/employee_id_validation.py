'''1. Employee ID Validation and Analysis System 
Problem Statement 
A company generates employee IDs in the following format: 
EMP2026ANUJ458 
Tasks 
Write a program to: 
1. Count the number of uppercase letters.  
2. Count the number of digits.  
3. Extract the joining year.  
4. Extract the employee name.  
5. Check whether the ID follows these rules:  
o Starts with "EMP"  
o Contains exactly 4 digits for the year  
o Ends with exactly 3 digits  
6. Create a list containing all digits present in the ID.  
7. Find the sum of all digits present in the ID.  
8. Display whether the ID is valid or invalid.  '''


# to display the employee id
emp_id ="EMP2026ANUJ458"
print(" Employee ID :",emp_id)
print("-------------------------")

# 1. Count the number of uppercase letters.
uppercase_count=0
for ch in emp_id:
    if ch >='A'and ch <='Z': # check all the uppercase alphabet from a to z
        uppercase_count = uppercase_count +1
print("Uppercase Letters:",uppercase_count)
print("-------------")

#2.Count the number of digits.  
digit_count=0
for ch in emp_id:
    if ch>='0' and ch<='9': # check all the digits between 0 to 9
        digit_count +=1
print("Digits:", digit_count)
print("------------------")

#3.Extract the joining year.  
n = emp_id[3:7] # index 3 to 6
print("Joining Year:",n)
print("---------------")

#4.Extract the employee name.
m=emp_id[7:11] # index 7 to 10
print("Employee Name:",m)
print("-----------------")

#Check whether the ID follows these rules:  
#o Starts with "EMP"  

rule1= emp_id.startswith("EMP")
print(rule1)

# o Contains exactly 4 digits for the year  
year=emp_id[3:7]
rule2=len(year)==4 and year.isdigit()
print(rule2)

# o Ends with exactly 3 digits
last_digits=emp_id[11:]
rule3=len(last_digits)==3 and last_digits.isdigit()
print(rule3)

print("---------------------------")

# Create a list containing all digits present in the ID.  
list=[]
for ch in emp_id:
   if ch>='0' and ch<='9':
      list.append(int(ch)) # add ch between 0 to 9 in list 
print("Digit List:",list)      
print("-----------------")

#Find the sum of all digits present in the ID. 
sum_digit=0
for digits in list:
    sum_digit=sum_digit + digits
print("Sum of Digits:", sum_digit)    
print("---------------------")

# Display whether the ID is valid or invalid. 
m=emp_id[7:-3]
name = m.isalpha() and m.isupper() 

if rule1 == True and rule2 == True and m.isalpha() and m.isupper() and rule3 == True:
    print("Employee ID ststus:valid")
else:
    print("invalid")

  '''  Sample Output 
Employee ID: EMP2026ANUJ458 
 
Uppercase Letters: 7 
Digits: 7 
 
Joining Year: 2026 
Employee Name: ANUJ 
 
Digit List: [2, 0, 2, 6, 4, 5, 8] 
Sum of Digits: 27 
 
ID Status: Valid '''
