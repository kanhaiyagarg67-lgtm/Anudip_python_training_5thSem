''' Email Address Validator 
Problem Statement 
A user enters an email address: 
rahul.sharma2026@gmail.com 
Tasks 
Write a program to: 
1. Extract username.  
2. Extract domain name.  
3. Extract extension.  
4. Count digits present in username.  
5. Count special characters.  
6. Check whether:  
o Exactly one '@' exists.  
o At least one '.' exists after '@'.  
7. Display Valid Email or Invalid Email.  '''
email = "rahul.sharma2026@gmail.com"

# Display the email entered by user
print("Email:", email)


# Step 1: Count how many times '@' is present in email
# A valid email should contain exactly one '@'
at_count = 0

for ch in email:
    if ch == "@":
        at_count = at_count + 1


# Step 2: Check if exactly one '@' is present
# If '@' is not present or more than one '@' is present, email is invalid
if at_count == 1:

    # Step 3: Split email into two parts using '@'
    # Example:
    # rahul.sharma2026@gmail.com
    # parts[0] = rahul.sharma2026
    # parts[1] = gmail.com
    parts = email.split("@")

    username = parts[0]       # Part before '@'
    domain_part = parts[1]    # Part after '@'

    # Step 4: Check whether '.' exists after '@'
    # Example: gmail.com contains '.'
    if "." in domain_part:

        # Step 5: Split domain part using '.'
        # Example:
        # gmail.com
        # domain_parts[0] = gmail
        # domain_parts[1] = com
        domain_parts = domain_part.split(".")

        domain = domain_parts[0]        # Domain name
        extension = domain_parts[1]     # Extension

        # Display extracted parts
        print()
        print("Username:", username)
        print("Domain:", domain)
        print("Extension:", extension)


        # Step 6: Count digits present in username
        # Example username: rahul.sharma2026
        # Digits are 2, 0, 2, 6
        digit_count = 0

        for ch in username:
            if ch >= '0' and ch <= '9':
                digit_count = digit_count + 1

        print()
        print("Digits Found:", digit_count)


        # Step 7: Count special characters in complete email
        # Special characters are characters other than alphabets and digits
        # Example: '.', '@' are special characters
        special_count = 0

        for ch in email:
            if not (
                (ch >= 'A' and ch <= 'Z') or
                (ch >= 'a' and ch <= 'z') or
                (ch >= '0' and ch <= '9')
            ):
                special_count = special_count + 1

        print("Special Characters Found:", special_count)


        # Step 8: If all above checks are correct, email is valid
        print()
        print("Email Status: Valid")

    else:
        # This block runs when '.' is not present after '@'
        print()
        print("Email Status: Invalid")

else:
    # This block runs when '@' is not exactly one
    print()
    print("Email Status: Invalid")

'''Sample Output 
Email: rahul.sharma2026@gmail.com 
 
Username: rahul.sharma2026 
Domain: gmail 
Extension: com 
 
Digits Found: 4 
Special Characters Found: 2 
 
Email Status: Valid
