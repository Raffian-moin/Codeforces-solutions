description_number = int(input())
team1_goal = 0
team2_goal = 0
team1 = ''
team2 = ''

for index in range(description_number):
    team = input().upper()
    if index == 0:
        team1 = team
        team1_goal = team1_goal + 1
    elif team1 != team:
        team2 = team
        team2_goal = team2_goal + 1
    elif team1 == team:
        team1_goal = team1_goal + 1
    elif team2 == team:
        team2_goal = team2_goal + 1

if (team1_goal > team2_goal):
    print(team1)
else:
    print(team2)