# read user input

flowers = input()
number_flowers = int(input())
budget =  int(input())
is_valid = True
# logic

if flowers == 'Roses':
 price = 5
elif flowers == 'Dahlias':
 price = 3.80
elif flowers == 'Tulips':
 price = 2.80
elif flowers == 'Narcissus':
 price = 3.00
elif flowers == 'Gladiolus':
 price = 2.50
else:
    is_valid = False
if flowers == 'Roses':
    if number_flowers > 80:
        price *= 0.9
elif flowers == 'Dahlias':
    if number_flowers > 90:
        price *= 0.85
elif flowers == 'Tulips':
    if number_flowers > 80:
        price *= 0.85
elif flowers == 'Narcissus':
    if number_flowers < 120:
        price *= 1.15
elif flowers == 'Gladiolus':
    if number_flowers < 80:
        price *= 1.20
else:
    is_valid = False

total_cost = price * number_flowers
money = abs(float(total_cost - budget))
#print output
if budget >= total_cost:
    print(f"Hey, you have a great garden with {number_flowers} {flowers} and {money:.2f} leva left.")
else:
    print(f"Not enough money, you need {money:.2f} leva more.")
