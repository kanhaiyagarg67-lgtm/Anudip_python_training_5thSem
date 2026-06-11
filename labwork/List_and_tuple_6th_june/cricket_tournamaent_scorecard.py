
'''A batsman's scores in different matches are stored in a list. 
scores = [45, 78, 12, 100, 67, 8, 90, 55] 
Write a program to: 
• Count half-centuries and centuries.  
• Find the highest score. 
• Display all scores below 20.  
• Calculate the average score.  '''

# creating a list of score of batsman
scores = [45, 78, 12, 100, 67, 8, 90, 55] 

# Task-1 To Count half-centuries and centuries.  
half_centuries=0
centuries=0
for score in scores:
    if(score>=50 and score<100):
        half_centuries+=1
    if(score>=100):
        centuries+=1
print("Half_Centuries", half_centuries)
print("Centuries", centuries)
print("---------------------------")

#Task-2 To Find the highest score. 
highest_score=scores[0]
for score in scores:
    if(highest_score<score):
        highest_score= score
print("Highest score is:")
print(highest_score)
print("--------------------------")

#TAsk- 3 To Display all scores below 20.  
print("Scores below 20 :")
for score in scores:
    if(score<20):
        print(score)
print("------------------------------")

#Task-4 To Calculate the average score

sum=0
for score in scores:
    sum+=score
print("Average score is :")
print(sum/len(scores))
