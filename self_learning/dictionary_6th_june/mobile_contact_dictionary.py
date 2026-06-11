#program for mobile contact dictionary
#enter the name along with mobile number of persons in dictionary
contacts = {
    "Amit": "9876543210",
    "Priya": "9876543211",
    "Rohan": "9876543212",
    "Neha": "9876543213",
    "Anjali": "9876543214",
    "Karan": "9876543215",
    "Pooja": "9876543216",
    "Arjun": "9876543217",
    "Sneha": "9876543218",
    "Rahul": "9876543219"
}

# Display all contact names in alphabetical order
print("Contact names in alphabetical order:")
for name in sorted(contacts):
    print(name)

# Count total number of contacts
print("Total contacts:", len(contacts))

# Search for a given contact name
search_name = input("Enter contact name to search: ")

found = False

# Search contact using break
for name, number in contacts.items():
    if name == search_name:
        print("Contact found:", name, number)
        found = True
        break

if found == False:
    print("Contact not found")

# Contacts whose names start with a vowel
vowel_contacts = []

for name in contacts.keys():
    if name[0] in "AEIOUaeiou":
        vowel_contacts.append(name)

print("Contacts starting with vowel:", vowel_contacts)
