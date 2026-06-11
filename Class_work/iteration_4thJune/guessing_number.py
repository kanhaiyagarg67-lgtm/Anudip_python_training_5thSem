#program for guessing the number game
while True:
    secret_number=int(input("guess the number :"))
    if secret_number==7:
        print("Congratulations! You guessed the number.")
        break
    else:
        print("Wrong guess. Try again.")
