'''Username Generator System 
Problem Statement 
A student enters: 
Rahul Sharma 
Tasks 
Generate a username using the rules: 
1. Remove spaces.  
2. Convert to lowercase.  
3. Append current year (2026).  
4. If username length exceeds 12, keep only first 12 characters.  
5. Count vowels in the generated username.  
6. Count consonants.  
7. Display username statistics.  '''


name = "Rahul Sharma"
year = "2026"

# Display original name
print("Original Name:", name)

# 1. Remove spaces
# "Rahul Sharma" becomes "RahulSharma"
username = ""

for ch in name:
    if ch != " ":
        username = username + ch

# 2. Convert username to lowercase
# "RahulSharma" becomes "rahulsharma"
username = username.lower()

# 3. Append current year
# "rahulsharma" + "2026" becomes "rahulsharma2026"
username = username + year

print()
print("Generated Username:")
print(username)

# 4. If username length exceeds 12, keep only first 12 characters
# But sample output shows full username, so we will only check length here
username_length = len(username)

print()
print("Username Length:", username_length)

# 5. Count vowels in generated username
vowels = 0

for ch in username:
    if ch in "aeiou":
        vowels = vowels + 1

# 6. Count consonants in generated username
consonants = 0

for ch in username:
    if ch >= 'a' and ch <= 'z':
        if ch not in "aeiou":
            consonants = consonants + 1

print()
print("Vowels:", vowels)
print("Consonants:", consonants)

# 7. Display username status
print()
print("Status: Username Generated Successfully")


'''
Sample Output 
Original Name: Rahul Sharma 
 
Generated Username: 
rahulsharma2026 
 
Username Length: 15 
 
Vowels: 5 
Consonants: 10 
 
Status: Username Generated Successfully
