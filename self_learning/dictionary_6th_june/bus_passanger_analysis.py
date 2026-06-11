#program for bus route passanger analysis
#enter bus route stops and passangers at stops in dictionary
passengers = {
    "Stop1": 12,
    "Stop2": 25,
    "Stop3": 18,
    "Stop4": 32,
    "Stop5": 9,
    "Stop6": 28,
    "Stop7": 14,
    "Stop8": 7,
    "Stop9": 21,
    "Stop10": 16
}

# Display stops having more than 20 passengers
print("Stops having more than 20 passengers:")
for stop, passenger in passengers.items():
    if passenger > 20:
        print(stop, passenger)

# Count stops with fewer than 10 passengers
count = 0
for passenger in passengers.values():
    if passenger < 10:
        count += 1
print("Stops with fewer than 10 passengers:", count)

# Find busiest stop
busiest = max(passengers, key=passengers.get)
print("Busiest stop:", busiest, passengers[busiest])

# Stops requiring extra bus
extra_bus = []
for stop, passenger in passengers.items():
    if passenger > 25:
        extra_bus.append(stop)
print("Stops requiring extra bus:", extra_bus)

# Average number of passengers
total = 0
for passenger in passengers.values():
    total += passenger

average = total / len(passengers)
print("Average number of passengers:", average)
