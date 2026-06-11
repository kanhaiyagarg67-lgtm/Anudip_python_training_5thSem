'''3. Chat Message Analytics 
Problem Statement 
A chat application stores a message: 
Python is awesome and Python is easy to learn 
Tasks 
Write a program to: 
1. Count total characters.  
2. Count total words.  
3. Find the longest word.  
4. Find the shortest word.  
5. Count how many times the word "Python" appears.  
6. Create a list of words having more than 4 characters.  
7. Display all words starting with a vowel.  
8. Count the number of vowels and consonants. ''' 


#to display the message 
message="Python is awesome and Python is easy to learn"
print("Message:",message)

#Count total characters.  
char_count= len(message)
print("Total characters:", char_count)    

# Count total words.  
words = message.split()
word_count=len(words)
print("Total words:", word_count)

#Find the longest word.  
longest_word=words[0]
for word in words:
    if len(word)> len(longest_word):
        longest_word=word
print("Longest word:",longest_word)        

#find shortest word
shortest_word = words[0]

for word in words:
    if len(word) < len(shortest_word):
        shortest_word = word

print("Shortest Word:", shortest_word)


# 5. Count how many times Python appears
python_count = 0

for word in words:
    if word == "Python":
        python_count = python_count + 1

print()
print("Occurrences of Python:", python_count)


# 6. Create list of words having more than 4 characters
long_words = []

for word in words:
    if len(word) > 4:
        long_words.append(word)

print()
print("Words Longer Than 4 Characters:")
print(long_words)

# 7. Display all words starting with a vowel
vowel_words = []

for word in words:
    first_letter = word[0]

    if first_letter in "AEIOUaeiou":
        vowel_words.append(word)

print()
print("Words Starting With Vowel:")
print(vowel_words)


# 8. Count vowels and consonants
vowels = 0
consonants = 0

for ch in message:
    if ch in "AEIOUaeiou":
        vowels = vowels + 1

    elif (ch >= 'A' and ch <= 'Z') or (ch >= 'a' and ch <= 'z'):
        consonants = consonants + 1

print()
print("Vowels:", vowels)
print("Consonants:", consonants)

'''Sample Output 
Message: 
Python is awesome and Python is easy to learn 
 
Total Characters: 45 
Total Words: 8 
 
Longest Word: awesome 
Shortest Word: is 
 
Occurrences of Python: 2 
 
Words Longer Than 4 Characters: 
['Python', 'awesome', 'Python', 'learn'] 
 
Vowels: 16 
Consonants: 22'''
