# input

percent_fats = int(input())
percent_protein = int(input())
percent_carbo = int(input())
calories = int(input())
water_percent = int(input())

# logic

total_fats = (percent_fats * calories) / 9
total_protein = (percent_protein * calories) / 4
total_carbo = (percent_carbo * calories) / 4

total_food = total_fats + total_protein + total_carbo
calories_food = calories / total_food
water = 100 - water_percent
real_calories = calories_food * water

# output

print(f'{real_calories:.4f}')
