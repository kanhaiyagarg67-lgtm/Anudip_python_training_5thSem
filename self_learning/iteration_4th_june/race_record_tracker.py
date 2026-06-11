# Accept number of racers
n = int(input("Enter number of racers: "))

# Accept lap time of first racer
time = int(input("Enter lap time of racer 1: "))

# Assume first racer is fastest and slowest
fastest_time = time
slowest_time = time

# Store fastest and slowest racer positions
fastest_position = 1
slowest_position = 1

# Loop for remaining racers
for i in range(2, n + 1):

    # Accept lap time of current racer
    time = int(input("Enter lap time of racer " + str(i) + ": "))

    # Smaller time means faster racer
    if time < fastest_time:
        fastest_time = time
        fastest_position = i

    # Greater time means slower racer
    if time > slowest_time:
        slowest_time = time
        slowest_position = i

# Calculate difference between slowest and fastest time
difference = slowest_time - fastest_time

# Display results
print("Fastest Racer Position:", fastest_position)
print("Slowest Racer Position:", slowest_position)
print("Difference:", difference)
