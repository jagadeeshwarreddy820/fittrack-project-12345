
# Input Collection
player_name = input("Enter your name: ")
games_played = int(input("Enter number of games you played: "))
total_score = int(input("Enter your score: "))

# Computation
if games_played != 0:
    average_score = total_score / games_played
else:
    average_score = 0

# Output Display
print("\nPlayer:", player_name)
print("Games Played:", games_played)
print("Total Score:", total_score)
print("Average Score: {:.2f}".format(average_score))
