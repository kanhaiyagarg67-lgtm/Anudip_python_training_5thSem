''' Cricket Tournament Statistics 
Problem Statement 
Runs scored by players in a tournament: 
runs = { 
    "Virat": 645, 
    "Rohit": 512, 
    "Gill": 698, 
    "Rahul": 435, 
    "Hardik": 278, 
    "Pant": 534, 
    "Surya": 389, 
    "Jadeja": 301, 
    "Iyer": 455, 
    "KL": 410 
} 
Tasks 
1. Display players scoring more than 500 runs.  
2. Find the Orange Cap winner.  
3. Find the lowest scorer.  
4. Calculate total runs scored.  
5. Create a list of players scoring below 400.  
6. Count players scoring between 400 and 600 runs.  '''


runs = {
    "Virat": 645,
    "Rohit": 512,
    "Gill": 698,
    "Rahul": 435,
    "Hardik": 278,
    "Pant": 534,
    "Surya": 389,
    "Jadeja": 301,
    "Iyer": 455,
    "KL": 410
}

# 1. Display players scoring more than 500 runs
print("Players Scoring More Than 500 Runs:")

for player, run in runs.items():
    if run > 500:
        print(player)


# Convert dictionary items into list
dict_items = list(runs.items())


# 2. Find the Orange Cap winner
# First player ko Orange Cap winner maan liya
orange_cap = dict_items[0][0]
highest_runs = dict_items[0][1]

for item in dict_items:
    if item[1] > highest_runs:
        orange_cap = item[0]
        highest_runs = item[1]

print()
print("Orange Cap Winner:", orange_cap, "(" , highest_runs ,")")


# 3. Find the lowest scorer
# First player ko lowest scorer maan liya
lowest_player = dict_items[0][0]
lowest_runs = dict_items[0][1]

for item in dict_items:
    if item[1] < lowest_runs:
        lowest_player = item[0]
        lowest_runs = item[1]

print()
print("Lowest Scorer:", lowest_player, "(" , lowest_runs , ")")


# 4. Calculate total runs scored
total_runs = 0

for run in runs.values():
    total_runs = total_runs + run

print()
print("Total Tournament Runs:", total_runs)


# 5. Create a list of players scoring below 400
below_400 = []

for player, run in runs.items():
    if run < 400:
        below_400.append(player)

print()
print("Players Scoring Below 400:")
print(below_400)


# 6. Count players scoring between 400 and 600 runs
count = 0

for run in runs.values():
    if run >= 400 and run <= 600:
        count = count + 1

print()
print("Players Between 400 and 600 Runs:", count)


'''Sample Output 
Players Scoring More Than 500 Runs: 
Virat 
Rohit 
Gill 
Pant 
 
Orange Cap Winner: Gill (698) 
 
Lowest Scorer: Hardik (278) 
 
Total Tournament Runs: 4657 
 
Players Scoring Below 400: 
['Hardik', 'Surya', 'Jadeja'] 
 
Players Between 400 and 600 Runs: 5'''
