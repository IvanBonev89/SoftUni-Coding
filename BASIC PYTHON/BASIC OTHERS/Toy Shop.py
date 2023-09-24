price_holiday = float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

total_sum = puzzles * 2.60 + dolls * 3 + bears * 4.10 + minions * 8.20 + trucks * 2
total_toys = puzzles+dolls+bears+minions+trucks
if total_toys >= 50:
    total_sum *= 0.75
total_sum *= 0.90

budget = abs(total_sum - price_holiday)

if total_sum >= price_holiday:
    print(f"Yes! {budget:.2f} lv left.")
else:
    print(f"Not enough money! {budget:.2f} lv needed.")


