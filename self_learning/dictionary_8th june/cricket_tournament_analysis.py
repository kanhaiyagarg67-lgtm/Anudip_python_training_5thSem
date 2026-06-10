'''Cricket Tournament Analytics System 
Problem Statement 
Store statistics of at least 30 cricket players. 
Example Structure 
players = { 
    "Virat": { 
        "runs": 645, 
        "matches": 12, 
        "wickets": 0 
    } 
} 
Requirements 
1. Display all player statistics.  
2. Find highest run scorer.  
3. Find lowest run scorer.  
4. Calculate average runs.  
5. Find player with maximum wickets.  
6. Find all-rounders (runs > 300 and wickets > 5).  
7. Display players scoring above average.  
8. Create categories:  
o Star Performer  
o Good Performer  
o Average Performer  
o Poor Performer  
9. Generate team statistics.  
10. Display top 5 batsmen.  
11. Display top 5 bowlers.  
12. Create a separate dictionary for award winners.  
Challenge 
Generate a tournament report.'''


# Cricket Tournament Analytics System

# Store statistics of 30 cricket players
players = {
    "Virat": {"runs": 645, "matches": 12, "wickets": 0},
    "Rohit": {"runs": 512, "matches": 12, "wickets": 0},
    "Gill": {"runs": 698, "matches": 12, "wickets": 1},
    "Rahul": {"runs": 435, "matches": 11, "wickets": 0},
    "Hardik": {"runs": 278, "matches": 10, "wickets": 12},
    "Pant": {"runs": 534, "matches": 12, "wickets": 0},
    "Surya": {"runs": 389, "matches": 10, "wickets": 0},
    "Jadeja": {"runs": 301, "matches": 12, "wickets": 15},
    "Iyer": {"runs": 455, "matches": 11, "wickets": 0},
    "KL": {"runs": 410, "matches": 10, "wickets": 0},

    "Bumrah": {"runs": 45, "matches": 12, "wickets": 22},
    "Shami": {"runs": 38, "matches": 10, "wickets": 18},
    "Siraj": {"runs": 25, "matches": 11, "wickets": 16},
    "Kuldeep": {"runs": 80, "matches": 10, "wickets": 20},
    "Axar": {"runs": 210, "matches": 9, "wickets": 11},
    "Ashwin": {"runs": 120, "matches": 8, "wickets": 14},
    "Rinku": {"runs": 340, "matches": 9, "wickets": 0},
    "Sanju": {"runs": 295, "matches": 8, "wickets": 0},
    "Tilak": {"runs": 330, "matches": 9, "wickets": 3},
    "Ishan": {"runs": 370, "matches": 10, "wickets": 0},

    "Arshdeep": {"runs": 18, "matches": 9, "wickets": 13},
    "Chahal": {"runs": 22, "matches": 8, "wickets": 12},
    "Washington": {"runs": 260, "matches": 9, "wickets": 8},
    "Dube": {"runs": 355, "matches": 10, "wickets": 7},
    "Shardul": {"runs": 180, "matches": 8, "wickets": 10},
    "Prasidh": {"runs": 15, "matches": 7, "wickets": 9},
    "Umran": {"runs": 10, "matches": 6, "wickets": 6},
    "Deepak": {"runs": 95, "matches": 7, "wickets": 8},
    "Mayank": {"runs": 275, "matches": 8, "wickets": 0},
    "Ruturaj": {"runs": 430, "matches": 10, "wickets": 0}
}


# 1. Display all player statistics
print("All Player Statistics:")

for player, details in players.items():
    print(player, "Runs:", details["runs"], "Matches:", details["matches"], "Wickets:", details["wickets"])


# 2. Find highest run scorer
player_items = list(players.items())

highest_player = player_items[0][0]
highest_runs = player_items[0][1]["runs"]

for player, details in players.items():
    if details["runs"] > highest_runs:
        highest_runs = details["runs"]
        highest_player = player

print()
print("Highest Run Scorer:")
print(highest_player, "Runs:", highest_runs)


# 3. Find lowest run scorer
lowest_player = player_items[0][0]
lowest_runs = player_items[0][1]["runs"]

for player, details in players.items():
    if details["runs"] < lowest_runs:
        lowest_runs = details["runs"]
        lowest_player = player

print()
print("Lowest Run Scorer:")
print(lowest_player, "Runs:", lowest_runs)


# 4. Calculate average runs
total_runs = 0

for details in players.values():
    total_runs = total_runs + details["runs"]

average_runs = total_runs / len(players)

print()
print("Average Runs:", average_runs)


# 5. Find player with maximum wickets
max_wicket_player = player_items[0][0]
max_wickets = player_items[0][1]["wickets"]

for player, details in players.items():
    if details["wickets"] > max_wickets:
        max_wickets = details["wickets"]
        max_wicket_player = player

print()
print("Maximum Wicket Taker:")
print(max_wicket_player, "Wickets:", max_wickets)


# 6. Find all-rounders
# All-rounder condition: runs > 300 and wickets > 5
print()
print("All-Rounders:")

for player, details in players.items():
    if details["runs"] > 300 and details["wickets"] > 5:
        print(player, "Runs:", details["runs"], "Wickets:", details["wickets"])


# 7. Display players scoring above average
print()
print("Players Scoring Above Average:")

for player, details in players.items():
    if details["runs"] > average_runs:
        print(player, "Runs:", details["runs"])


# 8. Create performer categories
star_performer = []
good_performer = []
average_performer = []
poor_performer = []

for player, details in players.items():
    runs = details["runs"]

    if runs >= 500:
        star_performer.append(player)
    elif runs >= 300:
        good_performer.append(player)
    elif runs >= 100:
        average_performer.append(player)
    else:
        poor_performer.append(player)

print()
print("Star Performers:")
print(star_performer)

print()
print("Good Performers:")
print(good_performer)

print()
print("Average Performers:")
print(average_performer)

print()
print("Poor Performers:")
print(poor_performer)


# 9. Generate team statistics
total_matches = 0
total_wickets = 0

for details in players.values():
    total_matches = total_matches + details["matches"]
    total_wickets = total_wickets + details["wickets"]

print()
print("Team Statistics:")
print("Total Runs:", total_runs)
print("Total Wickets:", total_wickets)
print("Total Matches Played By All Players:", total_matches)
print("Average Runs:", average_runs)


# 10. Display top 5 batsmen
# Sort players according to runs in descending order
batting_list = list(players.items())
batting_list.sort(key=lambda x: x[1]["runs"], reverse=True)

print()
print("Top 5 Batsmen:")

for i in range(5):
    player = batting_list[i][0]
    runs = batting_list[i][1]["runs"]
    print(player, "Runs:", runs)


# 11. Display top 5 bowlers
# Sort players according to wickets in descending order
bowling_list = list(players.items())
bowling_list.sort(key=lambda x: x[1]["wickets"], reverse=True)

print()
print("Top 5 Bowlers:")

for i in range(5):
    player = bowling_list[i][0]
    wickets = bowling_list[i][1]["wickets"]
    print(player, "Wickets:", wickets)


# 12. Create separate dictionary for award winners
award_winners = {}

award_winners["Orange Cap"] = {
    "player": highest_player,
    "runs": highest_runs
}

award_winners["Purple Cap"] = {
    "player": max_wicket_player,
    "wickets": max_wickets
}

award_winners["Best All-Rounder"] = {
    "player": "Jadeja",
    "runs": players["Jadeja"]["runs"],
    "wickets": players["Jadeja"]["wickets"]
}

print()
print("Award Winners:")

for award, details in award_winners.items():
    print(award, "->", details)


# Challenge: Generate tournament report
print()
print("========== TOURNAMENT REPORT ==========")

print("Total Players:", len(players))
print("Total Runs:", total_runs)
print("Total Wickets:", total_wickets)
print("Average Runs:", average_runs)
print("Highest Run Scorer:", highest_player)
print("Lowest Run Scorer:", lowest_player)
print("Maximum Wicket Taker:", max_wicket_player)
print("Star Performers Count:", len(star_performer))
print("Good Performers Count:", len(good_performer))
print("Average Performers Count:", len(average_performer))
print("Poor Performers Count:", len(poor_performer))

print("=======================================")
