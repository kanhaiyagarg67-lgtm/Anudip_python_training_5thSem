'''Problem 7: Movie Ticket Booking System 
Problem Statement 
Seat booking status in a cinema hall is stored as follows. 
Sample Data 
tickets = { 
    "A1": "Booked", 
    "A2": "Available", 
    "A3": "Booked", 
    "A4": "Available", 
    "B1": "Booked", 
    "B2": "Available", 
    "B3": "Booked", 
    "B4": "Available", 
    "C1": "Booked", 
    "C2": "Available" 
} 
Tasks 
1. Display available seats.  
2. Count booked and available seats.  
3. Reserve the first available seat.  
4. Save updated booking details to tickets.txt.  
5. Calculate hall occupancy percentage.  '''



# enter the data
tickets = {
    "A1": "Booked",
    "A2": "Available",
    "A3": "Booked",
    "A4": "Available",
    "B1": "Booked",
    "B2": "Available",
    "B3": "Booked",
    "B4": "Available",
    "C1": "Booked",
    "C2": "Available"
}
#Display available seats. 
print("Available Seats:")
for seat, status in tickets.items():
    if status == "Available":
        print(seat)
      
# Count booked and available seats.
booked = list(tickets.values()).count("Booked")
available = list(tickets.values()).count("Available")

print("Booked Seats:", booked)
print("Available Seats:", available)

# Reserve the first available seat.
for seat, status in tickets.items():
    if status == "Available":
        tickets[seat] = "Booked"
        print("Seat", seat, "Reserved Successfully.")
        break
      
# Calculate hall occupancy percentage.  '
booked = list(tickets.values()).count("Booked")
occupancy = booked / len(tickets) * 100

print("Hall Occupancy Percentage:", occupancy, "%")

# Save updated booking details to tickets.txt.  
with open("tickets.txt", "w") as file:
    for seat, status in tickets.items():
        file.write(seat + " : " + status + "\n")

print("Booking Details Saved Successfully.")

'''
Sample Output 
Available Seats: 
A2 
A4 
B2 
B4 
C2 
 
Booked Seats: 5 
Available Seats: 5 
 
Seat A2 Reserved Successfully. 
 
Hall Occupancy Percentage: 60.0% 
 
Booking Details Saved Successfully. '''
