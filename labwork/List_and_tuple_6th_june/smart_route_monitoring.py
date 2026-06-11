'''
Problem Statement:
Passenger count at each stop:
passengers = [12, 18, 25, 30, 28, 15, 8]

Tasks:
1. Find the busiest stop.
2. Display stops with fewer than 10 passengers.
3. Calculate average passengers.
4. Determine whether any stop exceeded 25 passengers.
'''

# Creating a list that stores the number of passengers at each stop
passengers = [12, 18, 25, 30, 28, 15, 8]

# --------------------------------------------------
# Task 1: Find the busiest stop
# --------------------------------------------------

# Assume the first stop has the maximum passengers initially
max_passengers = passengers[0]

# Traverse the list to find the maximum passenger count
for stop in passengers:

    # Update max_passengers if a larger value is found
    if max_passengers < stop:
        max_passengers = stop

# Display the maximum number of passengers
print("Maximum Passengers:", max_passengers)

# Find the stop number corresponding to the maximum passengers
# Adding 1 because list indexing starts from 0
busiest_stop = passengers.index(max_passengers) + 1

# Display the busiest stop number
print("Busiest Stop:", busiest_stop)

print("-----------------------------------")

# --------------------------------------------------
# Task 2: Display stops with fewer than 10 passengers
# --------------------------------------------------

print("Stops with passengers less than 10:")

# Traverse the list using index positions
for passenger in range(len(passengers)):

    # Check if the passenger count at that stop is less than 10
    if passengers[passenger] < 10:

        # Display the stop number
        print("Stop", passenger + 1)

print("-----------------------------------")

# --------------------------------------------------
# Task 3: Calculate average passengers
# --------------------------------------------------

print("Average passengers are:")

# Variable to store the total passenger count
total_pass = 0

# Add passenger count from each stop
for passenger in passengers:
    total_pass += passenger

# Calculate and display average passengers
# Use / for exact average and // for integer average
print(total_pass / len(passengers))

print("-----------------------------------")

# --------------------------------------------------
# Task 4: Determine whether any stop exceeded
# 25 passengers
# --------------------------------------------------

# Flag variable to track whether a stop exceeds 25 passengers
found = False

# Traverse the passenger list
for passenger in passengers:

    # Check if passenger count is greater than 25
    if passenger > 25:

        # Update flag and stop searching further
        found = True
        break

# Display result based on the flag value
if found:
    print("At least one stop exceeded 25 passengers.")
else:
    print("No stop exceeded 25 passengers.")
