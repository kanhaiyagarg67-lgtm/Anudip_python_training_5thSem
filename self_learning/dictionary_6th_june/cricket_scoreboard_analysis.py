# program for cricket scoreboard analysis
# enter name and score of players in dictionary
scores = {
    "Virat": 78,
    "Rohit": 112,
    "Gill": 45,
    "Rahul": 89,
    "Hardik": 32,
    "Jadeja": 61,
    "Surya": 105,
    "Pant": 95,
    "Bumrah": 18,
    "Shami": 25
}

# Display players who scored 50 or more
print("Players scoring 50 or more:")
for player, run in scores.items():
    if run >= 50:
        print(player, run)

# Count centuries
centuries = 0
for run in scores.values():
    if run >= 100:
        centuries += 1
print("Number of centuries:", centuries)

# Find highest scorer
highest_player = max(scores, key=scores.get)
print("Highest scorer:", highest_player, scores[highest_player])

# Players scoring below 30
below_30 = []
for player, run in scores.items():
    if run < 30:
        below_30.append(player)
print("Players scoring below 30:", below_30)

# Count players scoring between 50 and 99
count = 0
for run in scores.values():
    if run >= 50 and run <= 99:
        count += 1
print("Players scoring between 50 and 99:", count)
