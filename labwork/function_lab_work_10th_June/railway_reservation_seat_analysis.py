'''Railway Reservation Seat Analyzer 
Problem Statement 
A railway coach has seats represented as follows: 
seats = [ 
    "Booked", "Available", "Booked", "Booked", 
    "Available", "Available", "Booked", "Available", 
    "Booked", "Booked", "Available", "Booked" 
] 
Requirements 
Create the following functions: 
1. count_seats(seats) 
Returns the number of booked and available seats. 
2. first_available(seats) 
Returns the seat number of the first available seat. 
3. occupancy_percentage(seats) 
Returns the percentage of occupied seats. 
4. display_available_seats(seats) 
Displays all available seat numbers. 
'''

seats = [ 
    "Booked", "Available", "Booked", "Booked", 
    "Available", "Available", "Booked", "Available", 
    "Booked", "Booked", "Available", "Booked" 
] 

#function to count seats
def count_seats(seats):
    booked = 0
    available = 0

    for seat in seats:
        if seat == "Booked":
            booked += 1
        else:
            available += 1

    return booked, available

# 1. Count booked and available seats
'''def count_seats(seats):
    booked = seats.count("Booked")
    available = seats.count("Available")

    return booked, available'''

'''2.  function to find first_available(seats) 
Returns the seat number of the first available seat.'''

def first_available(seats):
    return seats.index("Available") + 1


#3. occupancy_percentage(seats) -> Returns the percentage of occupied seats.

#function to find occupancy_percentage

def occupancy_percentage(seats):
    booked = seats.count("Booked")
    available = seats.count("Available")
    occupancy= (booked/(booked+available)*100)
    return occupancy

#4 display_available_seats(seats) ->Displays all available seat numbers. 

def display_available_seats(seats):
    seat_numbers = []

    for i in range(len(seats)):
        if seats[i] == "Available":
            seat_numbers.append(i + 1)

    return seat_numbers


booked, available = count_seats(seats)

print("Booked Seats:", booked)
print("Available Seats:", available)

print("First Available Seat:",first_available(seats))
print("Occupancy Percentage:",occupancy_percentage(seats),"%")

print("Available Seat Numbers ", display_available_seats(seats))
'''Sample Output 
Booked Seats: 7 
Available Seats: 5 
 
First Available Seat: 2 
 
Occupancy Percentage: 58.33% 
 
Available Seat numbers 
2 5 6 8 11'''        
