'''Problem 1: Smart Railway Reservation System 
Problem Statement 
A railway reservation system stores the booking status of seats in a train coach. 
Sample Data 
seats = { 
    1: "Booked", 
    2: "Available", 
    3: "Booked", 
    4: "Available", 
    5: "Booked", 
    6: "Booked", 
    7: "Available", 
    8: "Booked", 
    9: "Available", 
    10: "Booked" 
} 
Tasks 
1. Display all available seat numbers.  
2. Count booked and available seats.  
3. Reserve the first available seat.  
4. Cancel booking for a given seat number.  
5. Store the updated reservation status in reservations.txt.  
6. Display occupancy percentage.  '''


# display the data
seats = { 
    1: "Booked", 
    2: "Available", 
    3: "Booked", 
    4: "Available", 
    5: "Booked", 
    6: "Booked", 
    7: "Available", 
    8: "Booked", 
    9: "Available", 
    10: "Booked" }

# Display all available seat numbers. 
print("Available Seats:")
for seat, status in seats.items():
    if status == "Available":
        print(seat, end=" ")
print("-------------------------------")

# Count booked and available seats.
booked = 0
available = 0

for status in seats.values():
    if status == "Booked":
        booked += 1 # booked seat count increased
    else:
        available += 1 # available seat count increased

print("\nBooked Seats:", booked)
print("Available Seats:", available)
print("----------------------------------")

#Reserve the first available seat. 
for seat, status in seats.items():
    if status == "Available":
        seats[seat] = "Booked"
        print("Seat", seat, "Reserved Successfully.")
        break
print("----------------------------------")

#Cancel booking for a given seat number.  
cancel_seat = int(input("Enter seat number to cancel: "))

if cancel_seat in seats:
    seats[cancel_seat] = "Available"
    print("Seat", cancel_seat, "Cancelled Successfully.")
else:
    print("Invalid seat number")
print("---------------------------------------")

# Display occupancy percentage.
booked = list(seats.values()).count("Booked")
occupancy = booked / len(seats) * 100
print("Occupancy Percentage:", occupancy, "%")

with open("reservations.txt", "w") as file:
    for seat, status in seats.items():
        file.write(str(seat)+" : "+status+"\n")

print("Reservation Details Saved Successfully.")


'''
Sample Output 
Available Seats: 
2 4 7 9 
 
Booked Seats: 6 
Available Seats: 4 
 
Seat 2 Reserved Successfully. 
 
Occupancy Percentage: 70.0% 
 
Reservation Details Saved Successfully.'''
