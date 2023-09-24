# read user input

budget = int(input())
season = input()
numbers = int(input())
price = 0
is_valid = True
#logic

if season == 'Spring':
    price = 3000
elif season == 'Autumn' or season == 'Summer':
    price = 4200
elif season == 'Winter':
    price = 2600
else:
    is_valid = False

if numbers <= 6:
    price *= 0.90
elif 7 <= numbers <= 11:
    price *= 0.85
elif numbers >= 12:
    price *= 0.75
else:
    is_valid = False

if numbers % 2 == 0 and season != 'Autumn':
    price *= 0.95
else:
    price *= 1

money = abs(budget - price)
#print output
if budget >= price:
    print(f"Yes! You have {money:.2f} leva left.")
else:
    print(f"Not enough money! You need {money:.2f} leva.")
