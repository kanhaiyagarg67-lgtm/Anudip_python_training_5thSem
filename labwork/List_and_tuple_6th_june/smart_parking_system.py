'''Parking slots are represented as: 
slots = [1, 0, 1, 1, 0, 0, 1, 0] 
Where: 
• 1 = Occupied  
• 0 = Available  
Write a program to: 
• Count occupied and available slots.  
• Find the first available slot.  
• Display all available slot numbers.  
• Check whether parking occupancy exceeds 75%. '''

#creating list of slots in parking

slots = [1, 0, 1, 1, 0, 0, 1, 1, 1, 0]

#Task-1 To Count occupied and available slots. 

# Counter for occupied slots
occupied = 0

# Counter for available slots
available = 0

# List to store available seat numbers
available_slots = []

# Traverse through the slots list using index
for i in range(len(slots)):

    # Check if slots is booked
    if slots[i] == 1:
        occupied += 1

    # Check if slots is available
    else:
        available += 1

        # Store slots number (index + 1)
        available_slots.append(i + 1)

print("Booked Slots:", occupied)
print("Available Slots:", available)
print("----------------------------")

#Task-2 Find the first available slot.  
# Find first available slot
for i in range(len(slots)):
    if slots[i] == 0:
        s = i + 1
        break
print("First Available Slot:", s)
print("---------------------------")

#Task-3 To Display all available slot numbers. 
available_slots_number=[] 
for i in range(len(slots)):
    if slots[i]== 1:
        available_slots_number.append(i + 1)

print("Available slots no. :")
print(available_slots_number)
print("----------------------------")


#Task -4  Check whether parking occupancy exceeds 75%.
occupancy = ((occupied / (occupied + available)) * 100)
if occupancy < 75:
    print("Status: Not More Than 75% Occupied")
