import random

# Generate secret number between 1 and 50
secret_number = random.randint(1, 50)

# Variable to count attempts
attempts = 0

# Loop will run until correct guess
while True:
    guess = int(input("Enter your guess: "))

    # Increase attempt count
    attempts = attempts + 1

    if guess > secret_number:
        print("Too High")

    elif guess < secret_number:
        print("Too Low")

    else:
        print("Correct Guess")
        print("Total Attempts:", attempts)
        break
