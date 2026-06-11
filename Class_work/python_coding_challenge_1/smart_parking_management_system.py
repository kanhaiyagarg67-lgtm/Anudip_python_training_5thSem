'''Problem 3: Smart Parking Management System 
Problem Statement 
The parking status of vehicles in a mall is maintained as follows. 
Sample Data 
parking_slots = [ 
    "Occupied", "Vacant", "Occupied", "Vacant", 
    "Occupied", "Occupied", "Vacant", "Occupied", 
    "Vacant", "Occupied" 
] 
Tasks 
1. Display vacant parking slot numbers.  
2. Count occupied and vacant slots.  
3. Allocate the first vacant slot to a new vehicle.  
4. Calculate parking occupancy percentage.  
5. Store updated parking information in parking.txt.  '''


# display the data
parking_slots = [
    "Occupied", "Vacant", "Occupied", "Vacant",
    "Occupied", "Occupied", "Vacant", "Occupied",
    "Vacant", "Occupied"
]

#Display vacant parking slot numbers. 
print("Vacant Parking Slots:")
for i in range(len(parking_slots)): # total length of parking slots
    if parking_slots[i] == "Vacant":
        print(i + 1, end=" ") # end is used to provide space
print("---------------------------------")

# Count occupied and vacant slots.  
occupied = parking_slots.count("Occupied")
vacant = parking_slots.count("Vacant")
print("\nOccupied Slots:", occupied)
print("Vacant Slots:", vacant)
print("---------------------------")


#Calculate parking occupancy percentage.  
for i in range(len(parking_slots)):
    if parking_slots[i] == "Vacant":
        parking_slots[i] = "Occupied"
        print("Vehicle Allocated to Slot", i + 1)
        break

occupied = parking_slots.count("Occupied")
percentage = occupied / len(parking_slots) * 100

print("Occupancy Percentage:", percentage, "%")
print("-------------------------------------")

#Store updated parking information in parking.txt.  

with open("parking.txt", "w") as file:
    for i in range(len(parking_slots)):
        file.write("Slot " + str(i + 1) + " : " + parking_slots[i] + "\n")

print("Parking Details Saved Successfully.")

'''
Sample Output 
Vacant Parking Slots: 
2 4 7 9 
Occupied Slots: 6 
Vacant Slots: 4 
Vehicle Allocated to Slot 2 
Occupancy Percentage: 70.0% 
Parking Details Saved Successfully.'''
