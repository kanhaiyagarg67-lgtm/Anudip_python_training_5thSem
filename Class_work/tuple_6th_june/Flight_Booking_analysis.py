# Program for the Flight Booking Analysis 
# Problem Statement 
# A flight reservation system stores passenger records as tuples: 
# bookings = ( 
#     ("P101", "Delhi", "Confirmed"), 
#     ("P102", "Mumbai", "Waiting"), 
#     ("P103", "Delhi", "Confirmed"), 
#     ("P104", "Chennai", "Cancelled"), 
#     ("P105", "Mumbai", "Confirmed"), 
#     ("P106", "Delhi", "Waiting") 
# ) 
# Where: 
# • Passenger ID  
# • Destination  
# • Booking Status  
# Tasks 
# Write a Python program to: 
# 1. Display all passengers whose booking status is Confirmed.  
# 2. Count the number of passengers travelling to Delhi.  
# 3. Count Confirmed, Waiting, and Cancelled bookings separately.  
# 4. Create a list containing passenger IDs with Waiting status.  
# 5. Determine which destination has the highest number of bookings.  
# Sample Output 
# Confirmed Passengers: 
# P101 Delhi 
# P103 Delhi 
# P105 Mumbai 
 
# Passengers Travelling to Delhi: 3 
 
# Confirmed: 3 
# Waiting: 2 
# Cancelled: 1 
 
# Waiting List: 
# ['P102', 'P106'] 
 
# Most Booked Destination: 
# Delhi


#Creating booking data
bookings = (
    ("P101", "Delhi", "Confirmed"),
    ("P102", "Mumbai", "Waiting"),
    ("P103", "Delhi", "Confirmed"),
    ("P104", "Chennai", "Cancelled"),
    ("P105", "Mumbai", "Confirmed"),
    ("P106", "Delhi", "Waiting")
)
#-----------------------------------------
#Task 1: To display all passengers whose booking status is Confirmed.
print("Passengers with Confirmed Booking : ")
for record in bookings:
    if record[2]=="Confirmed":
        print(record[0],record[1])
print("---------------------------------")  
#-----------------------------------------
#Task 2: To count the number of passengers travelling to Delhi.
count=0
for record in bookings:
    if record[1]=="Delhi":
        count+=1
print("Passengers travelling to Delhi : ",count)
print("---------------------------------")  
#-----------------------------------------
#Task 3: To count Confirmed, Waiting, and Cancelled bookings separately.    
confirmed=0
waiting=0
cancelled=0
for record in bookings:
    if record[2]=="Confirmed":
        confirmed+=1
    elif record[2]=="Waiting":
        waiting+=1
    else:
        cancelled+=1
print("Confirmed: ",confirmed)
print("Waiting: ",waiting)
print("Cancelled: ",cancelled)
print("---------------------------------")  
#-----------------------------------------      
#Task 4: To create a list containing passenger IDs with Waiting status.
waiting_list = []
for record in bookings:
    if record[2]=="Waiting":
        waiting_list.append(record[0])
print("Waiting List : ")
print(waiting_list)         
print("---------------------------------")
#-----------------------------------------
#Task 5: To determine which destination has the highest number of bookings.
delhi_booking=0
mumbai_booking=0    
chennai_booking=0
for record in bookings:
    if record[1]=="Delhi":
        delhi_booking+=1
    elif record[1]=="Mumbai":
        mumbai_booking+=1
    else:
        chennai_booking+=1

if delhi_booking>mumbai_booking and delhi_booking>chennai_booking:
    print("Most Booked Destination : ")
    print("Delhi")
elif mumbai_booking>delhi_booking and mumbai_booking>chennai_booking:
    print("Most Booked Destination : ")
    print("Mumbai") 
else:    
    print("Most Booked Destination : ")
    print("Chennai")
