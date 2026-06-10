''' Text Compression Analyzer 
Problem Statement 
A compressed message is given: 
AAABBBCCCDDDAAA 
Tasks 
Write a program to: 
1. Count occurrences of each character.  
2. Create a dictionary of character frequencies.  
3. Display unique characters.  
4. Find the most frequent character.  
5. Create a compressed output:  
A3B3C3D3A3 
6. Calculate compression ratio.  '''

text = "AAABBBCCCDDDAAA"

print("Original Text:")
print(text)

# 1. Count occurrences of each character
# 2. Create dictionary of character frequencies
char_freq = {}

for ch in text:
    if ch in char_freq:
        char_freq[ch] = char_freq[ch] + 1
    else:
        char_freq[ch] = 1

print()
print("Character Frequencies:")

for ch, count in char_freq.items():
    print(ch, "->", count)


# 3. Display unique characters
unique_chars = []

for ch in text:
    if ch not in unique_chars:
        unique_chars.append(ch)

print()
print("Unique Characters:")
print(unique_chars)


# 4. Find the most frequent character
dict_items = list(char_freq.items())

most_char = dict_items[0][0]
highest_count = dict_items[0][1]

for item in dict_items:
    if item[1] > highest_count:
        most_char = item[0]
        highest_count = item[1]

print()
print("Most Frequent Character:", most_char)


# 5. Create compressed output
# Example: AAABBBCCCDDDAAA becomes A3B3C3D3A3
compressed = ""

current_char = text[0]
count = 1

for i in range(1, len(text)):

    # If same character continues, increase count
    if text[i] == current_char:
        count = count + 1

    # If character changes, add previous character and count
    else:
        compressed = compressed + current_char + str(count)

        current_char = text[i]
        count = 1

# Add last character group also
compressed = compressed + current_char + str(count)

print()
print("Compressed Output:")
print(compressed)


# 6. Calculate compression ratio
original_length = len(text)
compressed_length = len(compressed)

compression_ratio = (compressed_length / original_length) * 100

print()
print("Original Length:", original_length)
print("Compressed Length:", compressed_length)

print()
print("Compression Ratio:", round(compression_ratio, 2), "%")



'''
Sample Output 
Original Text: 
AAABBBCCCDDDAAA 
 
Character Frequencies: 
A -> 6 
B -> 3 
C -> 3 
D -> 3 
 
Unique Characters: 
['A', 'B', 'C', 'D'] 
 
Most Frequent Character: A 
 
Compressed Output: 
A3B3C3D3A3 
 
Original Length: 15 
Compressed Length: 10 '''
 
Compression Ratio: 66.67%
