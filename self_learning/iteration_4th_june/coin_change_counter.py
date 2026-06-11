# Accept amount from user
amount = int(input("Enter amount: "))

# List of available notes
notes = [500, 200, 100, 50, 20, 10]

# Loop through each note
for note in notes:

    # Find how many notes of current value are needed
    count = amount // note

    # Display only if note is used
    if count > 0:
        print(note, "x", count)

    # Update remaining amount
    amount = amount % note
