#program for bus seat reservation analyzer
# List of bus seats
# 1 means seat is booked
# 0 means seat is available
seats = [1, 0, 1, 1, 0, 0, 1, 1, 1, 0]

# Variables to count booked and available seats
booked_count = 0
available_count = 0

# Variable to store first available seat
first_available = 0

# Empty list to store all available seat numbers
available_seat_numbers = []

# Loop through all seats
for i in range(len(seats)):

    # Seat number starts from 1, but index starts from 0
    seat_number = i + 1

    # If seat value is 1, seat is booked
    if seats[i] == 1:
        booked_count = booked_count + 1

    # If seat value is 0, seat is available
    else:
        available_count = available_count + 1

        # Add available seat number to list
        available_seat_numbers.append(seat_number)

# Find first available seat and stop immediately
for i in range(len(seats)):

    # If seat is available
    if seats[i] == 0:
        first_available = i + 1

        # Stop searching immediately
        break

# Calculate bus occupancy percentage
occupancy = (booked_count / len(seats)) * 100

# Display results
print("Booked Seats:", booked_count)
print("Available Seats:", available_count)
print("First Available Seat:", first_available)
print("Available Seat Numbers:", available_seat_numbers)
print("Bus Occupancy:", str(int(occupancy)) + "%")

# Check whether bus is more than 70% occupied
if occupancy > 70:
    print("Status: More Than 70% Occupied")
else:
    print("Status: Not More Than 70% Occupied")
