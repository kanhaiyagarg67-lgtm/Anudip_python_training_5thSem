#Program for user login
while True:
    password = str(input("Enter Password: "))

    if password == "admin123":
        print("Login Successful.")
        break
    else:
        print("Invalid Password.")
