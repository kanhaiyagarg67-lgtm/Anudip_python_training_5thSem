#program for library book analysis
#enter the book name with number of books available in library
books = {
    "Python Basics": 5,
    "Data Structures": 0,
    "Machine Learning": 3,
    "Java Programming": 2,
    "DBMS": 0,
    "Operating Systems": 6,
    "Networking": 4,
    "Cloud Computing": 1,
    "Cyber Security": 0,
    "Web Development": 7
}

# Display unavailable books
print("Unavailable books:")
for book, copies in books.items():
    if copies == 0:
        print(book)

# Count available books
available = 0
for copies in books.values():
    if copies > 0:
        available += 1
print("Number of available books:", available)

# Find book with maximum copies
max_book = max(books, key=books.get)
print("Book with maximum copies:", max_book, books[max_book])

# Books having less than 3 copies
less_than_3 = []
for book, copies in books.items():
    if copies < 3:
        less_than_3.append(book)
print("Books having less than 3 copies:", less_than_3)

# Total number of books available
total = 0
for copies in books.values():
    total += copies
print("Total books available:", total)
