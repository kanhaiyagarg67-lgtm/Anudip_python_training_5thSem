#program for display players score
#list to store score of players
player_score =[]
#input of score of 11 players
for i in range(11):
    score = int(input("Enter the score of player {}: ".format(i+1)))
    player_score.append(score)
    #display the score of each player
print("------player scores------")    
print("Player Scores:", player_score)    
#find the maximum score
maximum_score = max(player_score)
print("Maximum Score:", maximum_score)
