'''5. Library Book Search 
Problem Statement 
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
• Stop searching once a requested book is found. '''

#creating book data
books = [
    ("Python Basics", 5),
    ("Data Science", 0),
    ("Java Programming", 3),
    ("Machine Learning", 0)
]
#-----------------------------------------
#Task 1: To display unavailable books.
print("Unavailable books:")
for record in books:
    if record[1]==0:
        print(record[0])
print("---------------------------------")
#Task 2: To find all books with more than 2 copies.
print("Books with more than 2 copies:")
for record in books:
    if record[1]>2:
        print(record[0], "->", record[1], "copies")
print("---------------------------------")
#Task 3: To count available books.
available_count=0
for record in books:
    if record[1]>0:
        available_count+=1
print("Number of available books:", available_count)
print("---------------------------------")
#Task 4: To stop searching once a requested book is found.
requested_book=input("Enter the name of the book you want to search: ")
for record in books:
    if record[0]==requested_book and record[1]>1:
        print("Book Found:", record[0], "->", record[1], "copies")
        break
    else:
        print("Book not found.")
        break
