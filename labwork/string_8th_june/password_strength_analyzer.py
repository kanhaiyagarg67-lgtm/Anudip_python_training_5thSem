'''2. Password Strength Analyzer 
Problem Statement 
A user enters a password. 
Python@2026! 
Tasks 
Write a program to determine whether the password is Strong, Medium, or Weak. 
Rules: 
• Minimum length 8  
• Contains at least:  
o 1 uppercase letter  
o 1 lowercase letter  
o 1 digit  
o 1 special character  
Additionally: 
1. Count uppercase letters.  
2. Count lowercase letters.  
3. Count digits.  
4. Count special characters.  
5. Display all digits separately.  
6. Display all special characters separately.  '''


#to display the password
password ="Python@2026!"
print("Password:",password)
print("_______________")

#1. Count uppercase letters.
uppercase_count=0
for ch in password:
    if ch>='A' and ch<='Z':
        uppercase_count+=1
print("Uppercase Letters :",uppercase_count)        
print("_________________________")

#2. Count lowercase letters.
lowercase_count=0
for ch in password:
    if ch>='a' and ch<='z':
        lowercase_count +=1
print("Lowercase Letters:",lowercase_count)
print("_____________________________________")

#Count digits. 
digit_count=0
for ch in password:
    if ch >='0' and ch<='9':
        digit_count+=1
print("Digits:",digit_count)        
print("________________________________")

#Count special characters.
special_count=0
for ch in password:
    if not ((ch >= 'A' and ch <= 'Z') or (ch >= 'a' and ch <= 'z') or (ch >= '0' and ch <= '9')):
        special_count = special_count + 1
print("Special characters:",special_count)
    

# Display all digits separately.
digits=[]
for ch in password:
    if ch >='0' and ch<='9':
        digits.append(ch)
print("Digits Found:",digits)
print("____________________________")

# Display all special characters separately.  
special=[]
for ch in password:
    if not ((ch >= 'A' and ch <= 'Z') or (ch >= 'a' and ch <= 'z') or (ch >= '0' and ch <= '9')):
        special.append(ch)
print("Special Character found:",special)        
print("_______________________________")

#to determine whether the password is Strong, Medium, or Weak. 
# Rules: 
# • Minimum length 8  
# • Contains at least:  
# o 1 uppercase letter  
# o 1 lowercase letter  
# o 1 digit  
# o 1 special character 

if len(password) >= 8 and uppercase_count>=1 and lowercase_count>=1 and digit_count>=1 and special_count>=1:
    print("Password Strength: Strong")
elif len(password) >=6 and (uppercase_count>=1 or lowercase_count>=1) and digit_count>=1 :
    print("Password Strength: Medium")
else:
    print("Password Strength: Weak")

'''Sample Output 
Password: Python@2026! 
 
Uppercase Letters: 1 
Lowercase Letters: 5 
Digits: 4 
Special Characters: 2 
 
Digits Found: ['2', '0', '2', '6'] 
Special Characters Found: ['@', '!'] 
 
Password Strength: Strong '''
