# read user input
budget = float(input())
videocards = int(input())
cpu = int(input())
ram = int(input())

price_videocards = videocards * 250
price_cpu = (price_videocards * 0.35) * cpu
price_ram = (price_videocards * 0.10) * ram

total_price = price_videocards+price_cpu+price_ram
if videocards > cpu:
    discount = total_price * 0.15
    total_price -= discount
left_sum = abs(budget - total_price)
if budget >= total_price:
    print(f"You have {left_sum:.2f} leva left!")
else:
    print(f"Not enough money! You need {left_sum:.2f} leva more!")
