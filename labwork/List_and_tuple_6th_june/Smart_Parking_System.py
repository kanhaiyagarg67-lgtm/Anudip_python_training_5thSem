'''3. Smart Parking System 
Problem Statement 
Parking slots are represented as: 
slots = [1, 0, 1, 1, 0, 0, 1, 0] 
Where: 
• 1 = Occupied  
• 0 = Available  
Write a program to: 
• Count occupied and available slots.  
• Find the first available slot.  
• Display all available slot numbers.  
• Check whether parking occupancy exceeds 75%.'''

 #creating parking slot data
slots = [1, 0, 1, 1, 0, 0, 1, 0]
#-----------------------------------------
#Task 1: To count occupied and available slots.
occupied_slots=0
available_slots=0
for record in slots:
    if record==1:
        occupied_slots+=1
    else:
        available_slots+=1
print("Occupied Slots :", occupied_slots)
print("Available Slots :", available_slots)    
print("---------------------------------")
#Task 2: To find the first available slot.
available_slot_number=0
for i in range(len(slots)):
    if slots[i]==0:
        available_slot_number=i+1
        break
print("First Available Slot:",available_slot_number)
print("---------------------------------")
#Task 3: To display all available slot numbers.

print("Available Slot Numbers : ")
available_slot_numbers=[]
for i in range(len(slots)):
    if slots[i]==0:
        available_slot_numbers.append(i+1)
print(available_slot_numbers)
print("---------------------------------")
#Task 4: To check whether parking occupancy exceeds 75%.
occupancy_percentage=(occupied_slots/len(slots))*100
if occupancy_percentage>75:
    print("Parking occupancy exceeds 75%")
else:
    print("Parking occupancy does not exceed 75%")
print("---------------------------------")

