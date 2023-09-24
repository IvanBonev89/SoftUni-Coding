# input

days = int(input())
room = input()
raintg = input()
price = 0
total_price = 0
#logic
if room == 'room for one person':
    price = 18
elif room == 'apartment':
    price = 25
    if days < 10:
        price *= 0.7
    elif 10 <= days <= 15:
        price *= 0.65
    elif days > 15:
        price *= 0.5
elif room == 'president apartment':
    price = 35
    if days < 10:
        price *= 0.9
    elif 10 <= days <= 15:
        price *= 0.85
    elif days > 15:
        price *= 0.8

total_price = (days - 1) * price
if raintg == 'positive':
    total_price *= 1.25
else:
    total_price *= 0.90
#ouput
print(f'{total_price:.2f}')
