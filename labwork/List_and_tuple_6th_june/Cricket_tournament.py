'''2. Cricket Tournament Scorecard 
Problem Statement 
A batsman's scores in different matches are stored in a list. 
scores = [45, 78, 12, 100, 67, 8, 90, 55] 
Write a program to: 
• Count half-centuries and centuries.  
• Find the highest score.  
• Display all scores below 20.  
• Calculate the average score. '''

#creating cricket score data
scores = [45, 78, 12, 100, 67, 8, 90, 55]
#-----------------------------------------  
#Task 1: To count half-centuries and centuries.
half_centuries=0
centuries=0
for record in scores:
    if record>=50 and record<100:
        half_centuries+=1
    elif record>=100:
        centuries+=1
print("Half Centuries : ",half_centuries)
print("Centuries : ",centuries)
print("---------------------------------")
#Task 2: To find the highest score.
max_score=0
for record in scores:
    if record>max_score:
        max_score=record
print("Highest Score :",max_score)
print("---------------------------------")
#Task 3: To display all scores below 20.
print("Scores below 20 : ")
for record in scores:
    if record<20:
     print(record)
print("---------------------------------")
#Task 4: To calculate the average score.
total_score=0
for record in scores:
    total_score+=record
    n=len(scores)
    average_score=total_score/n
print("Average Score :", average_score)
