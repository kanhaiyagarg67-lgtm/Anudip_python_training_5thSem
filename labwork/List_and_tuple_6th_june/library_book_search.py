'''Problem Statement 
Books available in a library: 
books = [ 
    ("Python Basics", 5), 
    ("Data Science", 0), 
    ("Java Programming", 3), 
    ("Machine Learning", 0) 
] 
Write a program to: 
• Display unavailable books.  
• Find all books with more than 2 copies.  
• Count available books.  
• Stop searching once a requested book is found.'''

# creating records of books
books = [ 
    ("Python Basics", 5), 
    ("Data Science", 0), 
    ("Java Programming", 3), 
    ("Machine Learning", 0) 
]

#Task-1 To Display unavailable books.
print("Unavailable Books")

for book in books:
    if(book[1]==0):
        print(book[0])
print("-------------------------------")

#Task-2 To Find all books with more than 2 copies
print("Books with more than 2 copies")

for copies in books:
    if (copies[1]>2):
        print(copies[0])

print("--------------------------------")

#Task-3 To Count available books.
print("Total available books are ")
count=0# counter  for counting available books

for copies in books:
    if(copies[1]>0):
        count+=1
print(count)
print("-----------------------------------")

#TAsk-4 Stop searching once a requested book is found.

requested_book = input("\nEnter book name to search: ")

for book in books:
    if book[0].lower() == requested_book.lower():
        print("Book Found:", book[0])
        break
