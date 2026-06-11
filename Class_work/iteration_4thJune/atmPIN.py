#program for atm pin 
while True:
    pin = int(input("Enter PIN: "))

    if pin == 1234:
        print("Access Granted.")
        break
    else:
        print("Incorrect PIN. Try Again.")
        print()
        
