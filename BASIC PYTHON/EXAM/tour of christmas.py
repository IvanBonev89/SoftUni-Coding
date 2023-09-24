days = int(input())
sport = ''
is_valid = False
budget_day = 0
win = 0
lose = 0
win_total = 0
lose_total = 0
budget = 0
# logic
for i in range(1, days + 1):
    sport = input()
    while sport != 'Finish':
        result = input()
        if result == 'win':
            win += 1
            win_total += 1
            budget_day += 20
        else:
            lose += 1
            lose_total += 1
        sport = input()
    if win > lose:
        budget_day *= 1.10
        budget += budget_day
        win = 0
        lose = 0
        budget_day = 0
if win_total > lose_total:
    budget *= 1.20
# print
print(f"You won the tournament! Total raised money: {budget:.2f}")

if win_total < lose_total:
    print(f"You lost the tournament! Total raised money: {budget:.2f}")
