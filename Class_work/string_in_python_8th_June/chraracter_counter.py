'''program to count characters in a string without using built in function'''
sentence = input("Enter a sentence: ")
count = 0
for char in sentence:
    count += 1
print("Number of characters in the sentence:", count)
