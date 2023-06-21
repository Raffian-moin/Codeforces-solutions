players = input()

first_team_count = 0
second_team_count = 0
for index, player in enumerate(players):
    if player == '0':
        first_team_count = first_team_count + 1
        if first_team_count == 7:
            break
        if index > 0 and second_team_count != 0:
            second_team_count = 0
    elif player == '1':
        second_team_count = second_team_count + 1
        if second_team_count == 7:
            break
        if index > 0 and first_team_count != 0:
            first_team_count = 0

if first_team_count == 7 or second_team_count == 7:
    print('YES')
else:
    print('NO')
