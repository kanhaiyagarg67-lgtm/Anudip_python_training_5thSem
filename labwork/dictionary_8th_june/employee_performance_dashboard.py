'''2. Employee Performance Dashboard 
Problem Statement 
Employee performance scores are stored as: 
performance = { 
    "EMP101": 92, 
    "EMP102": 78, 
    "EMP103": 45, 
    "EMP104": 88, 
    "EMP105": 97, 
    "EMP106": 56, 
    "EMP107": 81, 
    "EMP108": 64, 
    "EMP109": 39, 
    "EMP110": 73 
} 
Tasks 
1. Display employees scoring above 80.  
2. Count employees needing improvement (score < 60).  
3. Find the top performer.  
4. Calculate average performance score.  
5. Create separate lists:  
o Excellent (≥ 90)  
o Good (75–89)  
o Average (60–74)  
o Poor (< 60)  
Sample Output 
Employees Scoring Above 80: 
EMP101 
EMP104 
EMP105 
EMP107 
 
Top Performer: EMP105 (97) 
 
Employees Needing Improvement: 3 
 
Average Score: 71.3 
 
Excellent: 
['EMP101', 'EMP105'] 
 
Good: 
['EMP102', 'EMP104', 'EMP107'] 
 
Average: 
['EMP108', 'EMP110'] 
 
Poor: 
['EMP103', 'EMP106', 'EMP109']'''

# Employee Performance Dashboard
performance = {
    "EMP101": 92,
    "EMP102": 78,
    "EMP103": 45,
    "EMP104": 88,
    "EMP105": 97,
    "EMP106": 56,
    "EMP107": 81,
    "EMP108": 64,
    "EMP109": 39,
    "EMP110": 73
}
# Task 1: Display employees scoring above 80.
print("Employees Scoring Above 80:")
for emp_id,score in performance.items():
    if score>80:
        print(emp_id)
print("---------------------------------")
# Task 2: Count employees needing improvement (score < 60).
improvement_count = 0
for score in performance.values():
    if score < 60:
        improvement_count += 1
print(f"Employees Needing Improvement: {improvement_count}")
print("---------------------------------")
# Task 3: Find the top performer.
dict_items = list(performance.items())
top_performer = dict_items[0][0]
top_score = dict_items[0][1]
for item in dict_items:
    if item[1] > top_score:
        top_performer = item[0]
        top_score = item[1]
print("Top Performer:" ,top_performer, top_score)
print("-------------------------------")
#Task 4: Calculate average performance score.
total = 0

for score in performance.values():
    total = total + score

average = total / len(performance)

print()
print("Average Score:", average)
#Task5: Create separate lists:
excellent = []
good = []
average_list = []
poor = []

for emp, score in performance.items():
    if score >= 90:
        excellent.append(emp)
    elif score >= 75 and score <= 89:
        good.append(emp)
    elif score >= 60 and score <= 74:
        average_list.append(emp)
    else:
        poor.append(emp)

print()
print("Excellent:")
print(excellent)

print()
print("Good:")
print(good)

print()
print("Average:")
print(average_list)

print()
print("Poor:")
print(poor)





