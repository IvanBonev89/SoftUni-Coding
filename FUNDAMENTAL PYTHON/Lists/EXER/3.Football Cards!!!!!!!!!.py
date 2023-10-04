info_cards = input().split()
counter_a = 0
counter_b = 0
team_a = ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11']
team_b = ['B-1', 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11']
#team_a = ["A-" + str(s)for s in range(1,12)]
#team_b = ["B-" + str(s)for s in range(1,12)]


for i in info_cards:
    if i in team_a:
        counter_a += 1
        team_a.remove(i)
    if i in team_b:
        counter_b += 1
        team_b.remove(i)
    if counter_a > 5:
        counter_a -=1
        break
    if counter_b > 5:
        counter_b -= 1
        break
team_a_players = 11 - counter_a
team_b_players = 11 - counter_b

# moje i s len(team_a) < 7
if team_a_players >= 7 and team_b_players >= 7:
    print(f"Team A - {team_a_players}; Team B - {team_b_players}")
else:
    print(f"Team A - {team_a_players}; Team B - {team_b_players}")
    print("Game was terminated")
