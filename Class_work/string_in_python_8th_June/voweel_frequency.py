'''Program to display frequency of each vowel present in the given sentence'''
sentence = input("Enter a sentence: ")
#-------------------------------------
#to count frequency of each vowel in the sentence
a = 0
e = 0
i = 0
o = 0   
u = 0
for char in sentence:
    if char == 'a' or char == 'A':
        a += 1
    elif char == 'e' or char == 'E':
        e += 1
    elif char == 'i' or char == 'I':
        i += 1
    elif char == 'o' or char == 'O':
        o += 1
    elif char == 'u' or char == 'U':
        u += 1
#-------------------------------------
if(a>0):
    print("Frequency of vowel a/A is:", a)
if(e>0):
    print("Frequency of vowel e/E is:", e)
if(i>0):
    print("Frequency of vowel i/I is:", i)
if(o>0):
    print("Frequency of vowel o/O is:", o)
if(u>0):
    print("Frequency of vowel u/U is:", u)
#-------------------------------------
'''Output:
Enter a sentence: Hello World
Frequency of vowel e/E is: 1    
Frequency of vowel o/O is: 2
'''
