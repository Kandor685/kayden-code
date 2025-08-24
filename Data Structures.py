TOTALNUMBEROFPLAYERS = 5

print ("High Scores: ")
highScores = []
player = []
for i in range (TOTALNUMBEROFPLAYERS):
    highScores.append(0)
    
for i in range (TOTALNUMBEROFPLAYERS):
    print ("Enter the high score number", i+1, end= ": ")
    highScores[i] = int(input())

highScores.sort()
highScores.reverse()

print("High Score Leaderboard:")
for i in range (TOTALNUMBEROFPLAYERS):
    print (f"{i+1}.", highScores[i])