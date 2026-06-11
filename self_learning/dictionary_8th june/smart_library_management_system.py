'''Smart Library Management System 
Problem Statement 
Create a digital library management system. 
Example Structure 
library = { 
    "B101": { 
        "title": "Python Basics", 
        "author": "ABC", 
        "copies": 5 
    } 
} 
Maintain records of at least 30 books. 
Requirements 
1. Add a book.  
2. Remove a book.  
3. Search a book by ID.  
4. Search by title.  
5. Update available copies.  
6. Issue a book.  
7. Return a book.  
8. Display books with fewer than 3 copies.  
9. Display books that are unavailable.  
10. Find the most available book.  
11. Generate a restocking report.  
12. Create a separate dictionary of books requiring immediate purchase.  
Challenge 
Generate a complete library summary report.'''


# Smart Library Management System

# Records of 30 books using nested dictionary
library = {
    "B101": {"title": "Python Basics", "author": "ABC", "copies": 5},
    "B102": {"title": "Data Structures", "author": "DEF", "copies": 2},
    "B103": {"title": "Machine Learning", "author": "GHI", "copies": 4},
    "B104": {"title": "Java Programming", "author": "JKL", "copies": 0},
    "B105": {"title": "DBMS", "author": "MNO", "copies": 6},
    "B106": {"title": "Operating Systems", "author": "PQR", "copies": 1},
    "B107": {"title": "Computer Networks", "author": "STU", "copies": 3},
    "B108": {"title": "Cyber Security", "author": "VWX", "copies": 2},
    "B109": {"title": "Cloud Computing", "author": "YZA", "copies": 7},
    "B110": {"title": "Web Development", "author": "BCD", "copies": 0},

    "B111": {"title": "Artificial Intelligence", "author": "EFG", "copies": 5},
    "B112": {"title": "Software Engineering", "author": "HIJ", "copies": 4},
    "B113": {"title": "C Programming", "author": "KLM", "copies": 8},
    "B114": {"title": "C Plus Plus", "author": "NOP", "copies": 2},
    "B115": {"title": "HTML CSS", "author": "QRS", "copies": 6},
    "B116": {"title": "JavaScript", "author": "TUV", "copies": 3},
    "B117": {"title": "React Basics", "author": "WXY", "copies": 1},
    "B118": {"title": "Django Framework", "author": "ZAB", "copies": 4},
    "B119": {"title": "Flask Web App", "author": "CDE", "copies": 0},
    "B120": {"title": "Data Science", "author": "FGH", "copies": 5},

    "B121": {"title": "Big Data", "author": "IJK", "copies": 2},
    "B122": {"title": "Blockchain", "author": "LMN", "copies": 3},
    "B123": {"title": "Internet of Things", "author": "OPQ", "copies": 1},
    "B124": {"title": "Mobile App Development", "author": "RST", "copies": 6},
    "B125": {"title": "Computer Graphics", "author": "UVW", "copies": 0},
    "B126": {"title": "Discrete Mathematics", "author": "XYZ", "copies": 7},
    "B127": {"title": "Compiler Design", "author": "AAA", "copies": 2},
    "B128": {"title": "Theory of Computation", "author": "BBB", "copies": 4},
    "B129": {"title": "Digital Logic", "author": "CCC", "copies": 5},
    "B130": {"title": "OOP with Java", "author": "DDD", "copies": 3}
}


# 1. Add a book
new_id = input("Enter new Book ID: ")
new_title = input("Enter book title: ")
new_author = input("Enter author name: ")
new_copies = int(input("Enter number of copies: "))

library[new_id] = {
    "title": new_title,
    "author": new_author,
    "copies": new_copies
}

print("Book added successfully")


# 2. Remove a book
remove_id = input("\nEnter Book ID to remove: ")

if remove_id in library:
    del library[remove_id]
    print("Book removed successfully")
else:
    print("Book ID not found")


# 3. Search a book by ID
search_id = input("\nEnter Book ID to search: ")

if search_id in library:
    print("Book Found")
    print("Title:", library[search_id]["title"])
    print("Author:", library[search_id]["author"])
    print("Copies:", library[search_id]["copies"])
else:
    print("Book ID not found")


# 4. Search by title
search_title = input("\nEnter book title to search: ")

found = False

for book_id, details in library.items():
    if details["title"] == search_title:
        print("Book Found")
        print("Book ID:", book_id)
        print("Title:", details["title"])
        print("Author:", details["author"])
        print("Copies:", details["copies"])
        found = True

if found == False:
    print("Book title not found")


# 5. Update available copies
update_id = input("\nEnter Book ID to update copies: ")

if update_id in library:
    new_copies = int(input("Enter new number of copies: "))
    library[update_id]["copies"] = new_copies
    print("Copies updated successfully")
else:
    print("Book ID not found")


# 6. Issue a book
issue_id = input("\nEnter Book ID to issue: ")

if issue_id in library:
    if library[issue_id]["copies"] > 0:
        library[issue_id]["copies"] = library[issue_id]["copies"] - 1
        print("Book issued successfully")
    else:
        print("Book is not available")
else:
    print("Book ID not found")


# 7. Return a book
return_id = input("\nEnter Book ID to return: ")

if return_id in library:
    library[return_id]["copies"] = library[return_id]["copies"] + 1
    print("Book returned successfully")
else:
    print("Book ID not found")


# 8. Display books with fewer than 3 copies
print("\nBooks With Fewer Than 3 Copies:")

for book_id, details in library.items():
    if details["copies"] < 3:
        print(book_id, details["title"], "Copies:", details["copies"])


# 9. Display books that are unavailable
print("\nUnavailable Books:")

for book_id, details in library.items():
    if details["copies"] == 0:
        print(book_id, details["title"])


# 10. Find the most available book
book_items = list(library.items())

most_book_id = book_items[0][0]
most_copies = book_items[0][1]["copies"]

for book_id, details in library.items():
    if details["copies"] > most_copies:
        most_book_id = book_id
        most_copies = details["copies"]

print("\nMost Available Book:")
print(most_book_id, library[most_book_id]["title"], "Copies:", most_copies)


# 11. Generate a restocking report
print("\nRestocking Report:")

for book_id, details in library.items():
    if details["copies"] < 3:
        print(book_id, details["title"], "needs restocking")


# 12. Create separate dictionary of books requiring immediate purchase
# Books having 0 or 1 copies require immediate purchase
immediate_purchase = {}

for book_id, details in library.items():
    if details["copies"] <= 1:
        immediate_purchase[book_id] = details

print("\nBooks Requiring Immediate Purchase:")

for book_id, details in immediate_purchase.items():
    print(book_id, details["title"], "Copies:", details["copies"])


# Challenge: Complete library summary report
total_books = len(library)

total_copies = 0
available_books = 0
unavailable_books = 0

for details in library.values():
    total_copies = total_copies + details["copies"]

    if details["copies"] > 0:
        available_books = available_books + 1
    else:
        unavailable_books = unavailable_books + 1

print("\n========== COMPLETE LIBRARY SUMMARY REPORT ==========")

print("Total Book Records:", total_books)
print("Total Copies Available:", total_copies)
print("Available Book Titles:", available_books)
print("Unavailable Book Titles:", unavailable_books)
print("Most Available Book:", library[most_book_id]["title"])
print("Books Requiring Immediate Purchase:", len(immediate_purchase))

print("====================================================")
