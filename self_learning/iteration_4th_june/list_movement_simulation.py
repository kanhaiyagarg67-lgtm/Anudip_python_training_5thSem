# Lift starts at floor 0
current_floor = 0

# Variable to store total floors travelled
total_travelled = 0

# Infinite loop for repeated destination input
while True:

    # Accept destination floor
    destination = int(input("Enter Destination: "))

    # Stop when user enters -1
    if destination == -1:
        break

    # Calculate floors travelled
    if destination > current_floor:
        travelled = destination - current_floor
    else:
        travelled = current_floor - destination

    # Display floors travelled in current trip
    print("Travelled:", travelled, "floors")

    # Add current trip travel to total travel
    total_travelled = total_travelled + travelled

    # Update current floor
    current_floor = destination

# Display total floors travelled
print("Total Travelled:", total_travelled, "floors")
