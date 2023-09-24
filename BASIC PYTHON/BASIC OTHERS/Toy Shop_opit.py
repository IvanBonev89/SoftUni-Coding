# read user input

price_vacation = float(input())
number_puzzle = int(input())
number_dolls = int(input())
number_bears = int(input())
number_minions = int(input())
number_trucks = int(input())
# logical
total_price = number_puzzle*2.60 + number_dolls * 3 + number_bears * 4.10 + number_minions * 8.20 +number_trucks * 2.00
total_numbers = number_puzzle + number_dolls + number_bears + number_minions + number_trucks

if total_numbers >= 50:
    total_price *= 0.75

shop_cost = total_price * 0.1
total_price -= shop_cost
result = abs(total_price - price_vacation)
if total_price >= price_vacation:
    print(f"Yes! {result:.2f} lv left.")
else:
    print(f"Not enough money! {result:.2f} lv needed.")
