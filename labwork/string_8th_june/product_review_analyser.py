''' Product Review Analyzer 
Problem Statement 
A customer submits a review: 
This product is excellent excellent excellent and very useful 
Tasks 
Write a program to: 
1. Count total words.  
2. Create a dictionary containing word frequencies.  
3. Find the most frequently used word.  
4. Find all words appearing only once.  
5. Count words having more than 5 characters.  
6. Display words in reverse order.  
7. Create a list of unique words.  '''

review = "This product is excellent excellent excellent and very useful"

# Split review into words
words = review.split()

# 1. Count total words
total_words = len(words)

print("Total Words:", total_words)


# 2. Create dictionary containing word frequencies
word_freq = {}

for word in words:
    if word in word_freq:
        word_freq[word] = word_freq[word] + 1
    else:
        word_freq[word] = 1

print()
print("Word Frequencies:")

for word, count in word_freq.items():
    print(word, "->", count)


# 3. Find the most frequently used word
dict_items = list(word_freq.items())

most_word = dict_items[0][0]
highest_count = dict_items[0][1]

for item in dict_items:
    if item[1] > highest_count:
        most_word = item[0]
        highest_count = item[1]

print()
print("Most Frequent Word:", most_word)


# 4. Find all words appearing only once
once_words = []

for word, count in word_freq.items():
    if count == 1:
        once_words.append(word)

print()
print("Words Appearing Once:")
print(once_words)


# 5. Count words having more than 5 characters
more_than_5 = 0

for word in words:
    if len(word) > 5:
        more_than_5 = more_than_5 + 1

print()
print("Words Having More Than 5 Characters:", more_than_5)


# 6. Display words in reverse order
reverse_words = []

for i in range(len(words) - 1, -1, -1):
    reverse_words.append(words[i])

print()
print("Words in Reverse Order:")
print(reverse_words)


# 7. Create a list of unique words
unique_words = []

for word in words:
    if word not in unique_words:
        unique_words.append(word)

print()
print("Unique Words:")
print(unique_words)
 
'''Sample Output 
Total Words: 8 
 
Word Frequencies: 
This -> 1 
product -> 1 
is -> 1 
excellent -> 3 
and -> 1 
very -> 1 
useful -> 1 
 
Most Frequent Word: excellent 
 
Words Appearing Once: 
['This', 'product', 'is', 'and', 'very', 'useful'] 
 
Unique Words: 
['This', 'product', 'is', 'excellent', 'and', 'very', 'useful']
